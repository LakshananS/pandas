import pandas as pd
import numpy as np

a_dic = {'1st':1, '2nd':2, '3rd':3, '4th':4, '5th':5}
ser= pd.Series(a_dic)

print(ser)
print(ser[0:3])
print(ser['2nd'])
print(ser[1])

#2D


# Your data dictionary
data = {
    "fruitsRegNo": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "prices": [10, 20, 30, 40, 50, 60, 64, 70, 80, 90, 100]
}

# Load data into a DataFrame object
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Accessing a specific column
col = "prices"
print(f"\nAccessing column '{col}':")
print(df[col])

# Accessing a specific label (row)
label = 2
print(f"\nAccessing row with label '{label}':")
print(df.loc[label])

# Accessing a specific location (row by index)
loc = 3
print(f"\nAccessing row at index '{loc}':")
print(df.iloc[loc])

# Slicing rows// data frame
print("\nSlicing rows from index 5 to 10:")
print(df[5:11])

# Using a boolean vector to filter rows. Dataframe
bool_vec = df["prices"] > 50
print("\nRows where 'prices' is greater than 50:")
print(df[bool_vec])

# Print the first 5 rows using head
print("\nFirst 5 rows:")
print(df.head(5))

#Fixing data
print("\nFixing data:")
for x in df.index:
    if df.loc[x,"prices"] >60:
        df.loc[x,"prices"] = 100
        print(df)


#print duplicate methods
print("\nDuplicated values:")
print(df.duplicated())
