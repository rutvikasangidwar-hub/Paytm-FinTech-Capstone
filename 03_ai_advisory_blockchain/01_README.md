# Part 3 — AI-Augmented FinTech Advisory & Blockchain Risk

This implementation follows the Part 3 specification from the capstone brief. The graded baseline uses deterministic mock logic with `MOCK_LLM` unset or set to `1`; no API key or network connection is required.

## Files

- `stock_universe.py` — prescribed fictional stock data and market constants.
- `investor_profiles.py` — five required investor profiles.
- `disclosure_snippets.py` — six exact disclosure snippets.
- `advisory_agent.py` — Think → Act → Observe portfolio agent.
- `extract_disclosure.py` — deterministic disclosure signal extraction.
- `debate.py` — bull/bear/synthesizer debate.
- `dcf_calculator.py` — FCFF DCF, WACC, terminal value, sensitivity and EV/EBITDA cross-check.
- `blockchain_risk_note.md` — required 600–900 word conceptual appendix.

## Run

From this directory:

```bash
python advisory_agent.py
python extract_disclosure.py
python debate.py
python dcf_calculator.py
```

Optional mock setting:

```bash
# Linux/macOS
export MOCK_LLM=1

# Windows PowerShell
$env:MOCK_LLM="1"
```

`MOCK_LLM=0` is intentionally not required for the graded submission.

## Design decisions

### Portfolio agent

The allocation is exactly the prescribed equal-weight lookup:
- Conservative → PAYBOND, PAYGOLD, PAYRETAIL
- Moderate → PAYRETAIL, PAYINFRA, PAYGOLD
- Aggressive → PAYTECH, PAYFIN, PAYINFRA

CAPM uses only beta: `Rf + beta * (Rm - Rf)`. Portfolio variance uses equal weights and pairwise correlation `rho = 0.3`. Volatility above 20% triggers `ESCALATED_TO_HUMAN_ADVISOR`.

### Disclosure extraction

The mock extractor uses keyword/regex rules for litigation, regulatory issues, customer concentration, hedging phrases, and confident/cautious sentiment. This makes the required baseline deterministic.

### Debate

PAYTECH is used for the demonstration. Bull, bear and synthesizer outputs reference the actual beta, analyst expected return and standard deviation from the supplied universe.

### DCF

Illustrative assumptions are stated directly in `dcf_calculator.py`. FCFF is:
`EBIT × (1 − tax) + D&A − CapEx − ΔNWC`.

The discount rate is a WACC built from CAPM cost of equity and an illustrative after-tax debt cost. Terminal growth is deliberately conservative so that the complete ±1 percentage-point sensitivity grid remains valid.

## Expected portfolio pattern

The prescribed inputs should produce approximately:
- INV01 Conservative: 8.44% volatility — no escalation.
- INV02 Moderate: 12.57% volatility — no escalation.
- INV03 Aggressive: 20.58% volatility — escalation.
- INV04 Moderate: 12.57% volatility — no escalation.
- INV05 Aggressive: 20.58% volatility — escalation.

Run the scripts and commit the actual terminal output/transcript to the repository if your instructor requires recorded outputs.
