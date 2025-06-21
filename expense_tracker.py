import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

# File path for expenses CSV
EXPENSES_CSV = 'expenses.csv'
SUMMARY_CSV = 'summary_report.csv'


def load_expenses(file_path):
    """Load expenses from a CSV file into a pandas DataFrame"""
    try:
        df = pd.read_csv(file_path, parse_dates=['Date'])
        # Ensure columns exist
        expected_cols = {'Date', 'Category', 'Amount', 'Description'}
        if not expected_cols.issubset(df.columns):
            raise ValueError(f"CSV is missing one or more required columns: {expected_cols}")
        # Clean amount column and convert to numeric
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
        df.dropna(subset=['Amount', 'Date'], inplace=True)
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])
    except Exception as e:
        print(f"Error loading expenses: {e}")
        return pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])


def save_expenses(df, file_path):
    """Save expenses DataFrame back to CSV file"""
    df.to_csv(file_path, index=False)
    print(f"Expenses saved to {file_path}.")


def total_spending_overview(df):
    """Display total spending and highest/lowest expense entries"""
    if df.empty:
        print("No expenses to analyze.")
        return
    total_spent = np.sum(df['Amount'])
    highest_expense = df.loc[df['Amount'].idxmax()]
    lowest_expense = df.loc[df['Amount'].idxmin()]

    print("\n=== Total Spending Overview ===")
    print(f"Total Amount Spent: ₹{total_spent:.2f}")
    print("\nHighest Expense:")
    print(highest_expense.to_string())
    print("\nLowest Expense:")
    print(lowest_expense.to_string())


def category_wise_analysis(df):
    """Group expenses by category and display analysis"""
    if df.empty:
        print("No expenses to analyze.")
        return
    grouped = df.groupby('Category')['Amount']
    total_per_category = grouped.sum()
    count_per_category = grouped.count()
    total_spent = total_per_category.sum()
    percent_per_category = (total_per_category / total_spent) * 100

    summary_df = pd.DataFrame({
        'Total Spent': total_per_category,
        'Transaction Count': count_per_category,
        'Percentage of Total (%)': percent_per_category.round(2)
    }).sort_values(by='Total Spent', ascending=False)

    print("\n=== Category-wise Analysis ===")
    print(summary_df.to_string())


def plot_pie_chart(df):
    """Generate a pie chart for expenses by category"""
    if df.empty:
        print("No expenses to visualize.")
        return
    total_per_category = df.groupby('Category')['Amount'].sum()
    plt.figure(figsize=(8, 8))
    plt.pie(total_per_category, labels=total_per_category.index, autopct='%1.1f%%', startangle=140)
    plt.title('Expense Breakdown by Category')
    plt.show()


def filter_by_date_range(df):
    """Filter expenses by date range entered by the user"""
    if df.empty:
        print("No expenses to filter.")
        return df
    print("\nEnter start date (DD-MM-YYYY) or leave blank to skip:")
    start_date_str = input().strip()
    print("Enter end date (DD-MM-YYYY) or leave blank to skip:")
    end_date_str = input().strip()

    try:
        if start_date_str:
            start_date = pd.to_datetime(start_date_str)
            df = df[df['Date'] >= start_date]
        if end_date_str:
            end_date = pd.to_datetime(end_date_str)
            df = df[df['Date'] <= end_date]
    except Exception as e:
        print(f"Invalid date format: {e}")
    return df


def add_new_expense(df):
    """Add a new expense record from user input"""
    print("\nEnter new expense details:")

    # Input date with validation
    while True:
        date_str = input("Date (DD-MM-YYYY): ").strip()
        try:
            date = pd.to_datetime(date_str)
            break
        except Exception:
            print("Invalid date format. Please enter a valid date in DD-MM-YYYY format.")

    category = input("Category: ").strip()
    while True:
        amount_str = input("Amount (numeric): ").strip()
        try:
            amount = float(amount_str)
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
            break
        except Exception:
            print("Invalid amount. Please enter a positive number.")

    description = input("Description: ").strip()

    # Append new expense row
    new_expense = pd.DataFrame({
        'Date': [date],
        'Category': [category],
        'Amount': [amount],
        'Description': [description]
    })
    df = pd.concat([df, new_expense], ignore_index=True)
    print("New expense added successfully.")
    return df


def export_summary_report(df):
    """Export summary report to a CSV file"""
    if df.empty:
        print("No data available to export.")
        return
    grouped = df.groupby('Category')['Amount']
    total_per_category = grouped.sum()
    count_per_category = grouped.count()
    total_spent = total_per_category.sum()
    percent_per_category = (total_per_category / total_spent) * 100

    summary_df = pd.DataFrame({
        'Total Spent': total_per_category,
        'Transaction Count': count_per_category,
        'Percentage of Total (%)': percent_per_category.round(2)
    }).sort_values(by='Total Spent', ascending=False)

    summary_df.to_csv(SUMMARY_CSV)
    print(f"Summary report exported to {SUMMARY_CSV}.")


def main():
    print("===== Expense Tracker =====")

    # Load existing data
    df = load_expenses(EXPENSES_CSV)

    # Main menu loop
    while True:
        print("\nSelect an option:")
        print("1. View total spending overview")
        print("2. View category-wise analysis")
        print("3. Filter expenses by date range")
        print("4. Add new expense")
        print("5. Generate pie chart (visualization)")
        print("6. Export summary report to CSV")
        print("7. Exit")
        choice = input("Enter choice (1-7): ").strip()

        if choice == '1':
            total_spending_overview(df)
        elif choice == '2':
            category_wise_analysis(df)
        elif choice == '3':
            df_filtered = filter_by_date_range(df)
            if not df_filtered.empty:
                print("\nFiltered data summary:")
                total_spending_overview(df_filtered)
                category_wise_analysis(df_filtered)
            else:
                print("No data after filtering.")
        elif choice == '4':
            df = add_new_expense(df)
            save_expenses(df, EXPENSES_CSV)
        elif choice == '5':
            plot_pie_chart(df)
        elif choice == '6':
            export_summary_report(df)
        elif choice == '7':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-7).")


if __name__ == "__main__":
    main()