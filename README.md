
# 🎲 Dice Simulation and Central Limit Theorem: From Uniform RNG to Gaussian PDF

This project demonstrates the **Central Limit Theorem (CLT)** by simulating dice throws, grouping them into subsets, and showing how the distribution of their means approaches a Gaussian PDF.

---

## 📂 Code Structure
- **main.py** → dice RNG, grouping of outcomes, PDF estimation, and autocorrelation calculation.

---

## 🔑 Important Variables
- `N_rolls` → total number of dice throws  
- `group_size` → number of dice per subset (controls averaging)  
- `faces` → number of sides on each die (default: 6)  

---

## ⚙️ How to Interact
1. Open **main.py**  
2. Change `N_rolls` (e.g., 10^3 → 10^6) to see smoother distributions.  
3. Adjust `group_size` to control the variance of the sample means.  
4. Run:
   ```bash
   python main.py


---

## 🧠 Physical/Statistical Intuition

* Individual dice rolls follow a **uniform distribution**.
* By grouping and averaging rolls, the distribution of means converges to a **Gaussian PDF**, as predicted by the CLT.
* Variance of the mean scales as:

  $$
  \sigma^2 \sim \frac{1}{N}
  $$

---

## 🧮 Numerical Models

* **Monte Carlo dice simulation**
* **Central Limit Theorem (CLT)** demonstration
* **Probability distribution function (PDF) estimation**

