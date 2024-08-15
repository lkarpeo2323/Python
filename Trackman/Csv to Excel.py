import pandas as pd

def csv_to_excel(csv_file_path, excel_file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file_path)
        
        # Save the DataFrame to an Excel file
        df.to_excel(excel_file_path, index=False)
        print(f"Successfully converted {csv_file_path} to {excel_file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
csv_file = 'trackman.csv'  # Replace with your CSV file path
excel_file = 'trackman.xlsx'  # Desired Excel file path

csv_to_excel(csv_file, excel_file)
