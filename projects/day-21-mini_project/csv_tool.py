import pandas as pd
import argparse
from pathlib import Path
from datetime import datetime

def analyze_data(file_path):
    """
    Reads a CSV file, performs a health check, and saves a 
    professional report to a dedicated folder.
    """
    try:
        # 1. LOAD DATA
        df = pd.read_csv(file_path)
        
        # 2. CREATE REPORTS DIRECTORY
        # Using pathlib to ensure we stay organized
        report_dir = Path("reports")
        report_dir.mkdir(exist_ok=True)
        
        # 3. PREPARE THE REPORT CONTENT
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_name = f"{file_path.stem}_summary.txt"
        report_path = report_dir / report_name
        
        # We use a multi-line f-string for a clean layout
        report_text = f"""
================================================
          SPOTTER: DATA HEALTH AUDIT
================================================
Generated on: {timestamp}
Source File:  {file_path.name}
------------------------------------------------

📊 DIMENSIONS:
- Total Rows:    {df.shape[0]}
- Total Columns: {df.shape[1]}

📋 COLUMN LIST:
{", ".join(df.columns)}

🔍 NULL VALUE SUMMARY:
{df.isnull().sum().to_string()}

------------------------------------------------
💡 QUICK INSIGHT:
- Memory Usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB
================================================
"""

        # 4. SAVE THE REPORT
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report_text)
            
        # 5. USER FEEDBACK (Console)
        print("\n" + "="*30)
        print(f"✅ ANALYSIS COMPLETE")
        print(f"📁 Report Saved: {report_path}")
        print("="*30 + "\n")
        
        # Preview top 5 rows for the developer (not saved in report)
        print("👀 Data Preview (Top 5 Rows):")
        print(df.head())

    except Exception as e:
        print(f"❌ ERROR: Could not process {file_path.name}")
        print(f"Details: {e}")

def main():
    # SETUP ARGPARSE
    parser = argparse.ArgumentParser(
        description="SPOTTER CSV Tool: Analyze your gym data logs instantly."
    )
    
    # REQUIRED ARGUMENT: The path to the CSV
    parser.add_argument("path", type=str, help="Path to the input CSV file")
    
    args = parser.parse_args()
    csv_path = Path(args.path)

    # VALIDATION
    if csv_path.exists() and csv_path.suffix.lower() == ".csv":
        analyze_data(csv_path)
    else:
        print(f"❌ INVALID FILE: Please provide a valid .csv file. (Checked: {csv_path})")

if __name__ == "__main__":
    main()