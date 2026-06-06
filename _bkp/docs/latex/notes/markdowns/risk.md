# Comprehensive Guide to Risk, Performance, and Alpha

## 1. Risk and Performance Measures
Performance measures are ratios used to determine if a return was "earned" or if the investor just took excessive risks.

* **Standard Deviation:** Measures how much an asset's price swings away from its average. 
* **Sharpe Ratio:** Measures excess return per unit of total risk ($\sigma$).
* **Sortino Ratio:** A variation of Sharpe that only penalizes downward volatility.

---

## 2. Coherent Risk Measures
A "coherent" risk measure must follow four mathematical properties (Artzner et al., 1999):
1. **Monotonicity:** If Portfolio A > Portfolio B, Risk(A) < Risk(B).
2. **Subadditivity:** $Risk(A+B) \leq Risk(A) + Risk(B)$. (Diversification reduces risk).
3. **Homogeneity:** Doubling the position doubles the risk.
4. **Translational Invariance:** Adding cash reduces risk by that exact amount.

> **Note:** **Value at Risk (VaR)** is NOT coherent because it fails **Subadditivity**. **Expected Shortfall (ES)** is a coherent alternative.

---

## 3. Alpha ($\alpha$) and Beta ($\beta$)
In the **Capital Asset Pricing Model (CAPM)**:
$$R_i = R_f + \beta_i(R_m - R_f) + \alpha$$

* **Beta ($\beta$):** The measure of systematic (market) risk.
  * Formula: $\beta = \frac{Cov(R_i, R_m)}{Var(R_m)}$
  * **Portfolio Beta:** A simple weighted average: $\beta_p = \sum w_i \beta_i$.
* **Alpha ($\alpha$):** The "value add" or return above what is expected given the risk taken. 
  * "Owning an Alpha" in practice means having a repeatable, proprietary edge (data, speed, or logic).

---

## 4. Portfolio Volatility ($\sigma_p$)
Unlike Beta, Volatility is NOT a simple weighted average due to correlation ($\rho$).
**Two-Asset Formula:**
$$\sigma_p = \sqrt{w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \sigma_A \sigma_B \rho_{AB}}$$

* **Linearity:** This formula mimics the law of cosines. If correlation is low, total risk is reduced.

---

## 5. XVA (Valuation Adjustments)
XVA represents the "hidden" costs of derivative trades beyond the market price:
* **CVA (Credit):** Cost of the counterparty defaulting.
* **DVA (Debit):** Adjustment for the bank's own default risk.
* **FVA (Funding):** Cost of funding collateral/margin.
* **KVA (Capital):** Cost of regulatory capital held against the trade.

---

## 6. Advanced Volatility: VIX and Volga
* **VIX:** The "Fear Gauge." Market expectation of 30-day volatility derived from S&P 500 options.
* **Volga:** A second-order Greek. It measures the sensitivity of **Vega** to changes in implied volatility.
  * **Formula:** $Volga = \frac{\partial^2 \text{Price}}{\partial \sigma^2}$
  * High Volga means option prices "accelerate" faster as market panic increases.