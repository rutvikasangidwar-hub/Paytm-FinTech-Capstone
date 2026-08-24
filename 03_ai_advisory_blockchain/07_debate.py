from stock_universe import STOCK_UNIVERSE

TICKER = "PAYTECH"

def bull_argument(ticker):
    d = STOCK_UNIVERSE[ticker]
    return (
        f"With an expected return of {d['analyst_expected_return']:.1%} "
        f"against a beta of {d['beta']:.2f}, {ticker} offers attractive "
        f"risk-adjusted upside if the higher market sensitivity is rewarded."
    )

def bear_argument(ticker):
    d = STOCK_UNIVERSE[ticker]
    return (
        f"{ticker} carries a standard deviation of {d['std_dev']:.1%} and a "
        f"beta of {d['beta']:.2f}, indicating substantial market and volatility risk."
    )

def synthesizer(ticker, bull, bear):
    return (
        f"{ticker} has a potentially attractive {STOCK_UNIVERSE[ticker]['analyst_expected_return']:.1%} "
        f"reference return, but its {STOCK_UNIVERSE[ticker]['std_dev']:.1%} volatility and "
        f"beta of {STOCK_UNIVERSE[ticker]['beta']:.2f} require caution. "
        "The balanced view is to consider it only when the investor's risk tolerance and horizon "
        "can absorb the higher volatility."
    )

if __name__ == "__main__":
    bull = bull_argument(TICKER)
    bear = bear_argument(TICKER)
    summary = synthesizer(TICKER, bull, bear)
    print("BULL:", bull)
    print("BEAR:", bear)
    print("SYNTHESIZER:", summary)
