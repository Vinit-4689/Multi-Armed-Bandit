# 🧠 Multi-Armed Bandit Algorithms — Intuitive + Mathematical Explanation

Imagine you’re in a casino with several slot machines (arms). Each machine gives you a random payout, and you want to win as much money as possible. But you don’t know which machine is the best. Do you keep trying new ones (exploration) or stick with the one that seemed good (exploitation)?

This is the **Multi-Armed Bandit (MAB)** problem.

---

## 🎯 Goal
To **maximize cumulative reward over time** by selecting the best arm as efficiently as possible.

Let:
- `K` = number of arms (options)
- `r_t` = reward at time `t`
- `T` = total number of steps
- `Regret` = difference between reward of best arm and what we got

### 🔻 Regret Formula:
\[
R(T) = T \cdot \mu^* - \sum_{t=1}^T r_t
\]
Where \( \mu^* \) is the best arm's expected reward.

Lower regret = smarter strategy ✅

---

## 📘 1. Epsilon-Greedy

### 💡 Intuition:
- Flip a coin: With small chance `ε`, pick a random arm.
- Otherwise, pick the one that seems best so far.

### 🧮 Formula:
- Pick random arm with probability `ε`
- Pick \( \arg\max_a \hat{\mu}_a \) with probability `1 - ε`

### ✅ Pros:
- Simple and fast
- Good if you want a quick baseline

### ❌ Cons:
- Keeps exploring forever, even if it found a great arm

---

## 📈 2. UCB1 (Upper Confidence Bound)

### 💡 Intuition:
“I’ll pick the option that has the best *potential* — current average plus some bonus for uncertainty.”

### 🧮 Formula:
For each arm \( a \):
\[
UCB_a = \hat{\mu}_a + \sqrt{\frac{2 \log t}{N_a}}
\]
- \( \hat{\mu}_a \) = current average reward
- \( N_a \) = times arm `a` was chosen
- \( t \) = total rounds

### ✅ Pros:
- Automatically balances exploration and exploitation
- Strong theoretical guarantees

### ❌ Cons:
- Needs a bit more computation

---

## 🎲 3. Thompson Sampling

### 💡 Intuition:
“Let’s *imagine* how good each arm could be, and pick the one that looks most promising in that imaginary world.”

It keeps track of how often each arm wins and fails, then samples from that distribution.

### 🧮 For Bernoulli rewards:
Each arm’s success modeled as:
\[
\text{Beta}(\alpha_a, \beta_a)
\]
- Start with \( \alpha = 1, \beta = 1 \)
- Update \( \alpha \) when we get a reward, \( \beta \) when we don’t
- Sample from this distribution, pick the highest

### ✅ Pros:
- Very efficient and adaptive
- Works great in practice

### ❌ Cons:
- Harder to implement for non-Bernoulli rewards

---

## 📊 Final Comparison
| Algorithm         | Easy to Code | Fast Learning | Low Regret | Real-World Use |
|------------------|--------------|---------------|------------|----------------|
| Epsilon-Greedy   | ✅✅✅         | ❌             | ❌❌         | ✅              |
| UCB1             | ✅✅           | ✅✅            | ✅✅✅        | ✅✅             |
| Thompson Sampling| ✅✅           | ✅✅✅          | ✅✅✅✅      | ✅✅✅✅          |

---

## 🔚 Conclusion
These algorithms solve the classic trade-off between *exploring* unknowns vs *exploiting* known good options.

- Epsilon-Greedy: Great intro, but wasteful
- UCB1: Smart confidence-based strategy
- Thompson Sampling: Bayesian brilliance

Choose based on your needs and complexity tolerance — now you're ready to bandit like a pro 💥

