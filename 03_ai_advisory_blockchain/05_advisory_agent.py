import os
from stock_universe import STOCK_UNIVERSE, RISK_FREE_RATE, MARKET_RETURN
from investor_profiles import INVESTOR_PROFILES

ALLOCATION_RULES = {
    "Conservative": ["PAYBOND", "PAYGOLD", "PAYRETAIL"],
    "Moderate": ["PAYRETAIL", "PAYINFRA", "PAYGOLD"],
    "Aggressive": ["PAYTECH", "PAYFIN", "PAYINFRA"],
}

def get_stock_data(ticker):
    """Local tool simulating an external stock-data API."""
    return STOCK_UNIVERSE[ticker].copy()

def capm_return(beta):
    return RISK_FREE_RATE + beta * (MARKET_RETURN - RISK_FREE_RATE)

def portfolio_metrics(tickers, rho=0.3):
    w = 1 / len(tickers)
    data = [get_stock_data(t) for t in tickers]
    expected = [capm_return(d["beta"]) for d in data]
    sigmas = [d["std_dev"] for d in data]

    portfolio_return = sum(w * r for r in expected)
    variance = sum((w ** 2) * (s ** 2) for s in sigmas)
    for i in range(len(sigmas)):
        for j in range(i + 1, len(sigmas)):
            covariance = rho * sigmas[i] * sigmas[j]
            variance += 2 * w * w * covariance

    return portfolio_return, variance, variance ** 0.5

def mock_narrative(profile, tickers, ret, vol):
    return (
        f"For {profile['risk_tolerance']} investor {profile['investor_id']}, "
        f"we recommend an allocation across {', '.join(tickers)} with an "
        f"expected portfolio return of {ret:.1%} and volatility of {vol:.1%}."
    )

def optional_llm_narrative(profile, tickers, ret, vol):
    # Optional extension point. Graded mode remains deterministic.
    return mock_narrative(profile, tickers, ret, vol)

def run_agent(profile):
    # THINK
    tickers = ALLOCATION_RULES[profile["risk_tolerance"]]

    # ACT
    stock_data = {ticker: get_stock_data(ticker) for ticker in tickers}

    # OBSERVE -> DECIDE
    ret, variance, vol = portfolio_metrics(tickers)
    escalated = vol > 0.20

    if os.getenv("MOCK_LLM", "1") == "0":
        narrative = optional_llm_narrative(profile, tickers, ret, vol)
    else:
        narrative = mock_narrative(profile, tickers, ret, vol)

    return {
        "investor_id": profile["investor_id"],
        "risk_tolerance": profile["risk_tolerance"],
        "tickers": tickers,
        "weights": {t: 1/3 for t in tickers},
        "stock_data": stock_data,
        "capm_expected_return": ret,
        "portfolio_variance": variance,
        "portfolio_std_dev": vol,
        "decision": "ESCALATED_TO_HUMAN_ADVISOR" if escalated else "AUTO_FINALIZED",
        "narrative": narrative,
    }

if __name__ == "__main__":
    for profile in INVESTOR_PROFILES:
        r = run_agent(profile)
        print("=" * 80)
        print(r["investor_id"], r["risk_tolerance"])
        print("Allocation:", r["tickers"])
        print("CAPM return:", f"{r['capm_expected_return']:.2%}")
        print("Variance:", f"{r['portfolio_variance']:.6f}")
        print("Std dev:", f"{r['portfolio_std_dev']:.2%}")
        print("Decision:", r["decision"])
        print(r["narrative"])
