from key import FREDKEY
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from fredapi import Fred

# --- Config ---
sigma_s = 0.15       # annualized volatility
T_years = 10         # years of simulation
steps_per_year = 12  # monthly steps
window_sizes = [3, 6, 12]  # moving average windows for plotting

# Constraints
max_up_1y = 2.0      # max 100% growth in 1 year
max_down_2y = 0.1    # min 10% of original in 2 years

fred = Fred(api_key=FREDKEY)

if __name__ == "__main__":
    # --- Query FRED ---
    m1 = fred.get_series("M1SL")
    m2 = fred.get_series("M2SL")
    df_money = pd.concat([m1, m2], axis=1)
    df_money.columns = ["M1", "M2"]
    df_money["M_total"] = df_money["M1"] + df_money["M2"]

    # Take last T_years of data
    N = T_years * steps_per_year
    df_money = df_money[-N:]
    dates = df_money.index

    # --- Simulate stock price ---
    np.random.seed(int(time.time()))
    dt = 1 / steps_per_year   # monthly fraction of year
    price = np.zeros(N)
    price[0] = 100  # starting index

    alpha = 0.5
    mu0 = 0.07
    M_total = df_money["M_total"].values

    for i in range(1, N):
        money_growth = (M_total[i] - M_total[i-1]) / M_total[i-1]
        mu_t = mu0 * dt + alpha * money_growth

        epsilon = np.random.randn()
        price_next = price[i-1] * (1 + mu_t + sigma_s * np.sqrt(dt) * epsilon)

        # --- Apply constraints ---
        if i >= steps_per_year:
            max_allowed = price[i-steps_per_year] * max_up_1y
            price_next = min(price_next, max_allowed)
        if i >= 2*steps_per_year:
            min_allowed = price[i-2*steps_per_year] * max_down_2y
            price_next = max(price_next, min_allowed)

        price[i] = price_next

    # --- Create DataFrame ---
    df_price = pd.DataFrame({"Price": price}, index=dates)
    df = df_price.join(df_money, how="inner")
    df["Price_normalized"] = df["Price"] / df["M_total"]

    # --- Plot ---
    fig, ax = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

    # Panel 1: Simulated Price
    ax[0].plot(df.index, df["Price"], label="Simulated Price", color="blue")
    ax[0].set_title("Simulated Stock Price")
    ax[0].set_ylabel("Price")
    ax[0].legend()
    ax[0].grid(True)

    # Panel 2: Money Supply
    ax[1].plot(df.index, df["M_total"], label="M1+M2 (billions)", color="green")
    ax[1].set_title("Money Supply")
    ax[1].set_ylabel("M1+M2")
    ax[1].legend()
    ax[1].grid(True)

    # Panel 3: Price normalized by money supply
    ax[2].plot(df.index, df["Price_normalized"], label="Price / (M1+M2)", color="purple")
    ax[2].set_title("Price Normalized by Money Supply")
    ax[2].set_ylabel("Price / M")
    ax[2].set_xlabel("Date")
    ax[2].legend()
    ax[2].grid(True)

    plt.tight_layout()
    plt.show()
