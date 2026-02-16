# First Security Simulation: Intrusion Path Analysis

### 🔑 Legend (Definition of Terms)
To help understand the experimental data and images:
* **A (Path 1)**: Basic intrusion path (Control group).
* **B (Path 2 - Before)**: Vulnerable path with high hint frequency (31% success rate).
* **C (Path 3)**: Alternative intrusion path.
* **D (Path 2 - Modified)**: Hardened path after reducing hint frequency (4% success rate).

## 📌 Project Overview
This project was conducted during my 1st year of high school to explore **Information Security** and **Digital Forensics**. I designed a simulation game to analyze security vulnerabilities based on intrusion path probabilities.

## 🔍 Key Findings
* **Objective:** Identifying the most vulnerable intrusion path through 50 trials per path.
* **Result:** Path 2 was identified as the most vulnerable (Success rate: 31%) due to the "Up-Down" hint structure.
* **Improvement:** After reducing the hint frequency, the success rate dropped to 4%, successfully mitigating the vulnerability.

## 🛠 Tech Stack
* **Python**: Game logic implementation (Assisted by AI, logic modified by developer).
* **R / Excel**: Data processing and visualization of success rates.

## ⚖️ Disclaimer
The core Python code was generated with the assistance of AI (GPT). However, the **experimental design, data analysis, and vulnerability mitigation logic** were entirely developed by me.

## 📊 Experiment Results (Vulnerability Analysis)

I analyzed the success rate of three different intrusion paths through 50 trials each.

| Intrusion Path | Initial Success Rate | Mitigation Applied | Final Success Rate |
| :--- | :---: | :--- | :---: |
| Path 1 | 12% | - | - |
| **Path 2** | **31% (High)** | Reduced "Up-Down" hints | **4%** |
| Path 3 | 8% | - | - |

### 💡 Conclusion
Path 2 was the most vulnerable due to the logical flaw in the hint system. By limiting information disclosure (hints), the security was significantly improved, reducing the success rate by 27 percentage points.
