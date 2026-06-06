# 📈 G-Research Quant Preparation Master File

This document compiles the core theory, proofs, and "Quant shortcuts" developed for the **G-Research Assessment**.

---

## 1. Probability Distributions: The "Family Tree"
In quant tests, these aren't separate ideas; they are a progression of the same logic.

### **The Bernoulli (The Atom)**
* **Concept:** A single trial with two outcomes: Success ($p$) or Failure ($q = 1-p$).
* **Key Formula:** $Var(X) = p(1-p)$.
* **Intuition:** A single light switch (On/Off).

### **The Binomial (The Chain)**
* **Concept:** $n$ independent Bernoulli trials.
* **Key Formula:** $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$.
* **Quant Hint:** Use this when you have a **fixed number of attempts** ($n$).

### **The Poisson (The Stream)**
* **Concept:** Events occurring at a constant rate ($\lambda$) over a continuous interval.
* **Key Formula:** $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$.
* **The "Magic" Property:** $E[X] = Var(X) = \lambda$.
* **Thinning Property:** If a Poisson stream $\lambda$ is split into two types ($p$ and $1-p$), the resulting streams are **independent** Poisson processes with rates $\lambda p$ and $\lambda(1-p)$.

---

## 2. The Gaussian (Normal) Distribution
The cornerstone of Financial Risk Management (VaR).

### **The PDF Formula**
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$
* **The $\sqrt{2\pi}$:** Normalization constant (ensures total area = 1).
* **The $2\sigma^2$:** Calibration factor (ensures the calculated variance equals exactly $\sigma^2$).

### **The Gaussian Integral Proof**
To prove $\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$:
1. **Square it:** $I^2 = \int \int e^{-(x^2+y^2)} dx dy$.
2. **Polar Change:** $dx dy \to r \, dr \, d\theta$ and $x^2 + y^2 = r^2$.
3. **Solve:** $I^2 = \int_{0}^{2\pi} d\theta \int_{0}^{\infty} r e^{-r^2} dr = 2\pi \cdot \frac{1}{2} = \pi$.
4. **Root:** $I = \sqrt{\pi}$.

### **The 68-95-99.7 Rule (Z-Scores)**
* **$\pm 1\sigma$:** 68% of data.
* **$\pm 2\sigma$:** 95% of data.
* **Z-index:** $Z = \frac{x-\mu}{\sigma}$.
* **One-Tailed 5% Risk (VaR):** $Z = 1.645$ (leaves 5% in one tail).
* **One-Tailed 1% Risk:** $Z = 2.33$.

---

## 3. Statistical Tools & Linear Regression
### **Variance & Covariance**
* **Independence:** If $X, Y$ are independent, $Var(X \pm Y) = Var(X) + Var(Y)$. **(Uncertainty always adds up!)**
* **Covariance Formula:** $Cov(X, Y) = E[XY] - E[X]E[Y]$.
* **Linearity:** $Cov(A+B, C) = Cov(A, C) + Cov(B, C)$.

### **Simple Linear Regression ($Y = \alpha + \beta X + \epsilon$)**
* **The Slope ($\beta$):** $\beta = \rho \frac{\sigma_Y}{\sigma_X} = \frac{Cov(X,Y)}{Var(X)}$.
* **Scaling:** If you double both $X$ and $Y$, $\beta$ remains the **same**.

---

## 4. Geometric Probability & Order Statistics
### **The "Broken Stick" / $L/(n+1)$ Rule**
If a stick of length $L$ is broken at $n$ random points:
* Expected length of **any** resulting segment is $\frac{L}{n+1}$.
* *Example:* 2 breaks on a 12cm stick $\to$ 3 segments of 4cm each.

### **Geometric Area Method**
* **$P(X+Y < k)$:** Draw a $1 \times 1$ square. The probability is the **area** of the triangle where the condition is met.
* *Example:* $P(X+Y < 0.5) = \text{Area of triangle with base 0.5} = \frac{1}{2}(0.5)(0.5) = 0.125$.

---

## 5. Decision Theory & Bayesian Logic
### **Bayes' Theorem**
$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$
* **Coin Toss Shortcut:** If you see $k$ heads in a row and wonder if the coin is double-headed ($p=1$) vs fair ($p=0.5$):
  $$P(\text{Double-Headed}) = \frac{1}{1 + (0.5)^k}$$

### **Expected Price/Value**
* **Optionality:** If you have the *option* to play/buy, a