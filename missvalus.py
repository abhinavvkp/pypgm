import pandas as pd
import matplotlib.pyplot as plt
data = {
    "name" : ["aman", "diya" , "rahul","sneha","arjun"],
    "marks": [78,92,85,67,74],
    "grade": [ "B","A","A","C","B"]
}
df = pd.DataFrame(data)
print("complete dataset:")
print(df)
print("\nfirst 3 rows:")
print(df.head(3))
print("\nmissing values:")
print(df.isnull().sum())
plt.hist(df["marks"],bins = 5,edgecolor="black")
plt.xlabel("marks")
plt.ylabel("number of students")
plt.title("mark distribution")
plt.show()
print("\nmedian of marks : " , df["marks"].median())
print("standard deviation of marks :" , df["marks"].std())