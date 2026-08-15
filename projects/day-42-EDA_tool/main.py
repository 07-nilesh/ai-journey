import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import os

def generate_eda_report(csv_file, output_file="eda_report.html"):
    # Load dataset
    df = pd.read_csv(csv_file)

    # --- Basic Info ---
    shape_info = f"Dataset Shape: {df.shape}"
    dtypes_info = df.dtypes.to_frame("dtype")
    missing_info = df.isnull().sum().to_frame("missing_values")
    summary_stats = df.describe(include="all").transpose()

    # --- Distribution plots for numerical columns ---
    dist_plots_html = ""
    num_cols = df.select_dtypes(include=np.number).columns
    for col in num_cols:
        fig = px.histogram(df, x=col, nbins=30, title=f"Distribution of {col}")
        dist_plots_html += pio.to_html(fig, include_plotlyjs="cdn", full_html=False)

    # --- Correlation heatmap ---
    corr = df[num_cols].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("heatmap.png")
    plt.close()

    # --- Top 10 correlated pairs ---
    corr_pairs = (
        corr.unstack()
        .sort_values(ascending=False)
        .drop_duplicates()
    )
    top_corr = corr_pairs[(corr_pairs < 1)].head(10)

    # --- Outlier detection using IQR ---
    outlier_info = {}
    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)][col]
        outlier_info[col] = len(outliers)

    # --- Build HTML report ---
    html_content = f"""
    <html>
    <head><title>EDA Report</title></head>
    <body>
        <h1>Exploratory Data Analysis Report</h1>
        <h2>Dataset Overview</h2>
        <p>{shape_info}</p>
        <h3>Dtypes</h3>
        {dtypes_info.to_html()}
        <h3>Missing Values</h3>
        {missing_info.to_html()}
        <h3>Statistical Summary</h3>
        {summary_stats.to_html()}

        <h2>Distribution Plots</h2>
        {dist_plots_html}

        <h2>Correlation Heatmap</h2>
        <img src="heatmap.png" width="600">

        <h2>Top 10 Correlated Feature Pairs</h2>
        {top_corr.to_frame("correlation").to_html()}

        <h2>Outlier Detection (IQR)</h2>
        <table border="1">
            <tr><th>Column</th><th>Outlier Count</th></tr>
            {''.join([f"<tr><td>{col}</td><td>{count}</td></tr>" for col, count in outlier_info.items()])}
        </table>
    </body>
    </html>
    """

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ EDA report saved as {output_file}")

# Example usage:
generate_eda_report("ai_financial_market_daily_realistic_synthetic.csv")
