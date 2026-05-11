# 📊 SPOTTER: CSV Data Health Analyzer

A lightweight Command Line Interface (CLI) tool built during **Day 21** of my AI/ML Journey. This tool performs instant "health audits" on CSV datasets to ensure they are ready for Machine Learning models.

## 🚀 Features
* **CLI Powered:** Run analysis directly from your terminal using `argparse`.
* **Automated Reporting:** Generates a professional `.txt` report in a dedicated `/reports` folder.
* **Smart Validation:** Uses `pathlib` to verify file existence and extensions.
* **Data Insights:** Provides dimensions, column lists, and a detailed null-value summary using `pandas`.
* **Timestamped Logs:** Tracks exactly when each audit was performed.

## 🛠️ Tech Stack
* **Language:** Python 3.12.10
* **Libraries:** Pandas, Argparse, Pathlib, Datetime

## 📖 How to Use

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/07-nilesh/ai-journey.git>