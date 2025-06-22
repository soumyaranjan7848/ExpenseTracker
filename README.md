


                                                         ExpenseTracker
 



The Expense Tracker program is a simple, interactive Python application designed to help users track, manage, and analyze their personal expenses.
It uses CSV files to store and load data and supports various functions like viewing summaries, adding new expenses, filtering data, visualizing expenses, and exporting reports.

For Run 
Make sure you have the required libraries installed:

         • pip install pandas numpy matplotlib

Create an expenses.csv file in the same directory with columns: Date, Category, Amount, Description. Example:

  • Date,Category,Amount,Description
  • 2024-01-05,Food,15.50,Lunch at cafe
  • 2024-01-07,Transport,8.20,Bus ticket
  • 2024-01-09,Entertainment,20.00,Movie ticket

Run the script:
   • python expense_tracker.py
   • Then use the menu to explore features.

    🔧 FEATURE OF THE EXPENSE TRACKERS:

1. Load Expenses from CSV

      • Reads an expenses.csv file.
      • Ensures required columns (Date, Category, Amount, Description) are present.
      • Cleans and prepares the data for analysis.

2. Add New Expense

• Allows users to enter a new expense by specifying:
             • Date
             • Category
             • Amount
             • Description
             
• Appends the new entry to the CSV file.


3. Total Spending Overview

   • Calculates and displays:

      • Total amount spent.
      • The highest single expense.
      • The lowest single expense.

   
 4. Category-wise Analysis

 •Groups expenses by category.

   • Displays:
      • Total spent in each category.
      • Number of transactions per category.
      • Percentage of total expenses per category.


5. Filter Expenses by Date

    • Allows filtering expenses between a user-specified start and end date.

    • Useful for analyzing spending over specific time periods.

6. Pie Chart Visualization (optional)

      • Plots a pie chart of expenses by category using Matplotlib.

7. Export Summary Report

      • Exports a category-wise expense summary to a summary_report.csv file.

8. Menu-driven Interface

    • Easy-to-navigate command-line interface.

    • Users choose actions by entering numbers from a menu.

        🧰 Tools/Libraries Used:

• pandas for data handling

• numpy for numerical operations

• matplotlib for plotting

• Standard Python libraries like datetime, os


     • INPUT / OUTPUT

Select an option:
1. View total spending overview      
2. View category-wise analysis       
3. Filter expenses by date range     
4. Add new expense
5. Generate pie chart (visualization)
6. Export summary report to CSV      
7. Exit
Enter choice (1-7): 
