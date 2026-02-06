import numpy as np
import pandas as pd 
import os
from datetime import datetime

def load_csv_safely():
    while True:
        path = input("Enter CSV file path: ").strip()

        if not os.path.exists(path):
            print("File not found. Please try again.")
            continue

        delimiters = [",", ";", "\t", "|"]

        for sep in delimiters:
            try:
                df = pd.read_csv(path, sep=sep)

                if df.shape[1] > 1:
                    return df, path
            except Exception:
                continue

        print("Could not detect delimiter automatically.")
        user_sep = input("Enter delimiter manually (e.g., , ; \\t | ): ")

        try:
            df = pd.read_csv(path, sep=user_sep)
            return df, path
        except Exception:
            print("Failed to read file with that delimiter. Try again.")


def dataset_overview(df):
    intcount = 0
    floatcount = 0
    objectcount = 0

    for col in df.columns:
        dtype = df[col].dtype

        if dtype == "int64":
            intcount += 1
        elif dtype == "float64":
            floatcount += 1
        else:
            objectcount += 1

    memory_bytes = df.memory_usage(deep=True).sum()
    memory_kb = memory_bytes / 1024
    memory = round(memory_kb, 2)

    rows, columns = df.shape

    return rows, columns, intcount, floatcount, objectcount, memory


def display(df):
    row, column, intcount, floatcount, objectcount, memory =dataset_overview(df)
    print("======= File Analysis ======")
    print("Rows: ",row)
    print("Columns: ",column)
    print("Integer type Columns: ",intcount)
    print("Float type Columns: ",floatcount)
    print("Object type Columns: ",objectcount)
    print("Memory Usage(KBs): ",memory) 

def missing_value_analysis(df):
    missing_info = {}

    for col in df.columns:
        missing_count = df[col].isna().sum()

        if missing_count > 0:
            missing_info[col] = missing_count

    return missing_info

def numeric_statistics(df):
    stats = {}

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in numeric_cols:
        column_data = df[col]

        if column_data.dropna().empty:
            continue

        stats[col] = {
            "mean": column_data.mean(),
            "median": column_data.median(),
            "min": column_data.min(),
            "max": column_data.max(),
            "std": column_data.std()
        }

    return stats


def display_numeric_table(stats):
    if not stats:
        print("No numeric columns with valid data.")
        return

    table = pd.DataFrame(stats)

    table = table.round(2)

    print("\nNumeric Statistics Table: \n")
    print(table)

def categorical_insights(df):
    insights = {}

    cat_cols = df.select_dtypes(include=["object", "string"]).columns

    for col in cat_cols:
        column_data = df[col].dropna()

        if column_data.empty:
            continue

        unique_count = column_data.nunique()
        top_value = column_data.mode()[0]
        top_count = column_data.value_counts().iloc[0]

        insights[col] = {
            "unique": unique_count,
            "top": top_value,
            "count": top_count
        }

    return insights

def display_categorical_table(insights):
    if not insights:
        print("\nNo categorical columns with valid data.")
        return

    table = pd.DataFrame(insights)
    print("\nCategorical Insights: \n")
    print(table)

import pandas as pd

def generate_report(df):
    report = ""

    # ===== DATASET OVERVIEW =====
    rows, columns, intcount, floatcount, objectcount, memory = dataset_overview(df)

    report += "===== DATASET OVERVIEW =====\n"
    report += f"Rows: {rows}\n"
    report += f"Columns: {columns}\n"
    report += f"Integer columns: {intcount}\n"
    report += f"Float columns: {floatcount}\n"
    report += f"Object/String columns: {objectcount}\n"
    report += f"Memory usage: {memory} KB\n\n"

    # ===== MISSING VALUES =====
    missing = missing_value_analysis(df)

    report += "\n===== MISSING VALUES =====\n"
    if not missing:
        report += "No missing values found.\n\n"
    else:
        for col, count in missing.items():
            report += f"{col}: {count} missing values\n"
        report += "\n"

    # ===== NUMERIC STATISTICS =====
    numeric = numeric_statistics(df)

    report += "\n===== NUMERIC STATISTICS =====\n"
    if not numeric:
        report += "No numeric columns with valid data.\n\n"
    else:
        num_table = pd.DataFrame(numeric).round(2)
        report += num_table.to_string() + "\n\n"

    # ===== CATEGORICAL INSIGHTS =====
    categorical = categorical_insights(df)

    report += "\n===== CATEGORICAL INSIGHTS =====\n"
    if not categorical:
        report += "No categorical columns with valid data.\n"
    else:
        cat_table = pd.DataFrame(categorical)
        report += cat_table.to_string() + "\n"

    return report

def save_report(report_text, dataset_path):

    dataset_name = os.path.splitext(os.path.basename(dataset_path))[0]


    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    filename = f"{dataset_name}_report_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_text)

    print(f"Report saved as: {filename}")


def main():
    df, path = load_csv_safely()
    report = generate_report(df)
    print(report)
    save_report(report, path)

   
if __name__ == "__main__":
    main()
