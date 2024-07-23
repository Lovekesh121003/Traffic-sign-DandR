import pandas as pd

# Replace 'path_to_labels.csv' with the absolute path to your labels.csv file
labelFile = r'C:\Users\Sameer\Desktop\dip\traffic_sign_recognition-main\labels.csv'

# Read the CSV file
data = pd.read_csv(labelFile)

# Print the first few rows of the dataframe
print(data.head())
