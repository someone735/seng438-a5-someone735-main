import pandas as pd

# This script demonstrates how to read a Python file and print its contents.
def read_python_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().splitlines()
            newContent = []
            for i,j in enumerate(content):
                newContent.append(j.split('\t'))
            print(newContent)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        return newContent

# Read the data from 'failure_data_set/csr2.dat' and print its contents
readData = read_python_file('SYS2Target.DAT')
readData.pop(-1)
summationOfTime = []
# differenceBetweenPoints = []
for i in range(len(readData)):
    if i == 0:
        summationOfTime.append(int(readData[i][1]))
        # differenceBetweenPoints.append(int(readData[i][1]))
    else:
        summationOfTime.append((int(readData[i][1])+int(summationOfTime[-1])))
        # differenceBetweenPoints.append((int(readData[i][1])-int(readData[i-1][1])))
        
print("Summation of Time: ", summationOfTime)
# print("Difference Between Points: ", differenceBetweenPoints)

# Create DataFrames from summationOfTime and differenceBetweenPoints
df_summation = pd.DataFrame(summationOfTime, columns=["Summation of Time"])
# df_difference = pd.DataFrame(differenceBetweenPoints, columns=["Difference Between Points"])

# Save the DataFrames to separate Excel files
output_file_path_summation = 'summation_of_time.xlsx'
# output_file_path_difference = 'difference_between_points.xlsx'

df_summation.to_excel(output_file_path_summation, index=False)
# df_difference.to_excel(output_file_path_difference, index=False)

print(f"Summation of Time has been saved to {output_file_path_summation}")
# print(f"Difference Between Points has been saved to {output_file_path_difference}")
