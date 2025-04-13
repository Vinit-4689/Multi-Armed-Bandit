# Multi-Armed Bandit Algorithms

This project implements and compares popular Multi-Armed Bandit algorithms:

- 🎯 **Epsilon-Greedy**
- 📈 **UCB1 (Upper Confidence Bound)**
- 🎲 **Thompson Sampling**

The goal is to simulate a scenario where we repeatedly choose between different options ("arms") to maximize the total reward, just like picking ads, treatments, or online recommendations.

---

## 🔍 Purpose

This project serves as a practical and intuitive demonstration of key strategies for solving the **exploration vs exploitation** dilemma using Bandit algorithms. It's meant for:

- 📘 Learning and experimenting with Bandit strategies
- 📊 Comparing different algorithms' performance
- 🧠 Understanding real-world decision making with uncertainty
- 🧑‍💻 Building a solid portfolio project

---

## 🚀 Quick Start

### 🔧 Installation
```bash
pip install numpy matplotlib
```

### ▶️ Run the Project
```bash
python bandit_simulation.py
```
You’ll see a graph comparing the cumulative rewards of each strategy.

---

## 📂 Project Structure

```
.
├── bandit_simulation.py      # Main code implementing all algorithms
├── README.md                 # Overview & instructions
└── explanation.md            # In-depth explanation of algorithms and results
```

---

## 📈 Algorithms Overview

- **Epsilon-Greedy**: Explores randomly with probability ε, otherwise picks best-known option.
- **UCB1**: Picks based on current average + confidence interval (more balanced).
- **Thompson Sampling**: Samples from a probability distribution and picks the most likely winner.

---

## 📊 Result Preview
The script visualizes cumulative rewards from all 3 strategies over 1000 iterations. Helps see which learns fastest.

---

## 📘 License
This project is open-source and free to use under the MIT license.

---

## 🙋‍♂️ Author
**Vinit Singh Pathir**  
[GitHub](https://github.com/Vinit-4689) | [LinkedIn](www.linkedin.com/in/vinit-singh-cse)

---

>**“The more you explore, the better you exploit.”**

