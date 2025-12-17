import pandas as pd
import matplotlib.pyplot as plt

print("Attempting to load data...")

try:
    # We change encoding to 'ISO-8859-1' which handles special characters better
    df = pd.read_csv('train.csv', encoding='ISO-8859-1')
    
    print("SUCCESS: Data loaded!")
    print(df.head()) # Show first 5 rows

    # AUTOMATICALLY FIND THE DATE COLUMN
    # This looks for any column name that contains the word "Date"
    date_col = [col for col in df.columns if 'Date' in col]
    
    if date_col:
        date_column_name = date_col[0]
        print(f"Plotting data using column: {date_column_name}")
        
        # Convert text to dates
        df[date_column_name] = pd.to_datetime(df[date_column_name], dayfirst=True, errors='coerce')
        df = df.sort_values(date_column_name)
        
        # Plot Sales vs Date
        plt.figure(figsize=(10, 6))
        
        # Check for Sales column
        if 'Sales' in df.columns:
            plt.plot(df[date_column_name], df['Sales'], label='Sales', color='blue')
            plt.ylabel("Sales Amount")
        else:
            # If no 'Sales' column, just count the number of orders per day
            print("No 'Sales' column found. Plotting order counts instead.")
            df[date_column_name].value_counts().sort_index().plot()
            plt.ylabel("Number of Orders")

        plt.title("Sales Forecast / Trends")
        plt.xlabel("Date")
        plt.legend()
        plt.grid(True)
        plt.show()
        
    else:
        print("ERROR: Could not find a 'Date' column in your CSV file.")
        print("Your columns are:", df.columns)

except Exception as e:
    print("Still having trouble? Here is the error:")
    print(e)