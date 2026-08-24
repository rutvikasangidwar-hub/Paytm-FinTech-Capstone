import numpy as np
import pandas as pd
from stock_universe import STOCK_UNIVERSE, RISK_FREE_RATE, MARKET_RETURN

# Illustrative assumptions, all amounts in INR crore.
EBIT = 120.0
TAX_RATE = 0.25
DA = 20.0
CAPEX = 30.0
DELTA_NWC = 10.0
BASE_FCF = EBIT * (1 - TAX_RATE) + DA - CAPEX - DELTA_NWC

BASE_GROWTH = 0.10
TERMINAL_GROWTH = 0.03

BETA = STOCK_UNIVERSE["PAYRETAIL"]["beta"]
COST_OF_EQUITY = RISK_FREE_RATE + BETA * (MARKET_RETURN - RISK_FREE_RATE)
PRETAX_COST_OF_DEBT = 0.08
AFTER_TAX_COST_OF_DEBT = PRETAX_COST_OF_DEBT * (1 - TAX_RATE)

EQUITY_WEIGHT = 0.70
DEBT_WEIGHT = 0.30
WACC = EQUITY_WEIGHT * COST_OF_EQUITY + DEBT_WEIGHT * AFTER_TAX_COST_OF_DEBT

EBITDA = 150.0
EV_EBITDA_MULTIPLE = 12.0

def project_fcff(base_fcf=BASE_FCF, growth=BASE_GROWTH, years=5):
    # Growth fades linearly from the base growth rate to terminal growth.
    growth_rates = np.linspace(growth, TERMINAL_GROWTH, years)
    fcfs = []
    previous = base_fcf
    for g in growth_rates:
        previous *= (1 + g)
        fcfs.append(previous)
    return growth_rates, fcfs

def dcf_value(discount_rate=WACC, terminal_growth=TERMINAL_GROWTH):
    growth_rates, fcfs = project_fcff()
    pv_fcfs = sum(fcf / ((1 + discount_rate) ** year)
                  for year, fcf in enumerate(fcfs, start=1))
    terminal_value = fcfs[-1] * (1 + terminal_growth) / (discount_rate - terminal_growth)
    pv_terminal = terminal_value / ((1 + discount_rate) ** 5)
    return pv_fcfs + pv_terminal, fcfs, terminal_value

def sensitivity_table():
    rows = []
    for wacc in [WACC - 0.01, WACC, WACC + 0.01]:
        row = []
        for tg in [TERMINAL_GROWTH - 0.01, TERMINAL_GROWTH, TERMINAL_GROWTH + 0.01]:
            value, _, _ = dcf_value(wacc, tg)
            row.append(value)
        rows.append(row)
    return pd.DataFrame(
        rows,
        index=[f"WACC {w:.2%}" for w in [WACC - .01, WACC, WACC + .01]],
        columns=[f"g {g:.2%}" for g in [TERMINAL_GROWTH - .01, TERMINAL_GROWTH, TERMINAL_GROWTH + .01]]
    )

if __name__ == "__main__":
    if WACC - TERMINAL_GROWTH < 0.03:
        raise ValueError("Base WACC must exceed terminal growth by at least 3 percentage points.")

    worst_gap = (WACC - 0.01) - (TERMINAL_GROWTH + 0.01)
    if worst_gap < 0.01:
        raise ValueError("Worst-case sensitivity cell violates WACC > terminal growth by 1pp.")

    value, fcfs, terminal_value = dcf_value()
    multiple_value = EBITDA * EV_EBITDA_MULTIPLE

    print("Base FCFF:", f"INR {BASE_FCF:.2f} crore")
    print("Cost of equity:", f"{COST_OF_EQUITY:.2%}")
    print("After-tax cost of debt:", f"{AFTER_TAX_COST_OF_DEBT:.2%}")
    print("WACC:", f"{WACC:.2%}")
    print("Terminal growth:", f"{TERMINAL_GROWTH:.2%}")
    print("5-year FCFF:", [round(x, 2) for x in fcfs])
    print("Terminal value:", f"INR {terminal_value:.2f} crore")
    print("DCF enterprise value:", f"INR {value:.2f} crore")
    print("EV/EBITDA cross-check:", f"INR {multiple_value:.2f} crore")
    print("\nSensitivity table (INR crore):")
    print(sensitivity_table().round(2))
