# Week 1 Lab: Python Refresher, NumPy, Pandas & Matplotlib
# Name : Sinya 
# CMS-ID 023-24-0227

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io

# Q1: Swap values without a third variable
x, y = 15, 25
x, y = y, x  # standard python tuple unpacking
print(f"Q1: Swapped values -> x={x}, y={y}")

# Q2: Check if prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(f"Q2: is 17 prime? {is_prime(17)}")

# Q3: Fibonacci using loop
def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list
print(f"Q3: Fibonacci up to 5 terms: {fibonacci(5)}")

# Q4: Remove duplicates but keep order
def remove_dups(lst):
    result = []
    seen = set()
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result
print(f"Q4: Unique list: {remove_dups([1, 2, 2, 3, 1, 4])}")

# Q5: Multiply any number of args
def multiply(*args):
    ans = 1
    for num in args:
        ans *= num
    return ans
print(f"Q5: Multiply(2,3,4) = {multiply(2, 3, 4)}")

# Q6: Dictionary comprehension for char frequency
string = "data science"
freq = {char: string.count(char) for char in set(string)}
print(f"Q6: Char frequencies: {freq}")

# Q7: Highest salary from list of dicts
employees = [
    {"name": "John", "department": "HR", "salary": 45000},
    {"name": "Alice", "department": "IT", "salary": 95000},
    {"name": "Bob", "department": "Sales", "salary": 60000}
]
best_paid = max(employees, key=lambda x: x['salary'])
print(f"Q7: Highest salary belongs to: {best_paid['name']}")

# Q8: Lambda and filter for odd numbers
nums = [10, 15, 20, 25, 30, 33]
odds = list(filter(lambda x: x % 2 != 0, nums))
print(f"Q8: Odd numbers: {odds}")

# Q9: 1D array 1 to 30 reshaped to 5x6
arr1 = np.arange(1, 31).reshape(5, 6)
print("Q9: 5x6 Matrix:\n", arr1)

# Q10: 6x6 identity matrix with custom diagonal
eye_mat = np.eye(6)
np.fill_diagonal(eye_mat, [1, 2, 3, 4, 5, 6])
print("Q10: Modified Identity:\n", eye_mat)

# Q11: 25 random ints, sum, mean, std
rand_arr = np.random.randint(1, 100, 25)
print(f"Q11: Sum: {rand_arr.sum()}, Mean: {rand_arr.mean()}, Std: {rand_arr.std():.2f}")

# Q12: Diagonal of 4x4 and sum
arr4x4 = np.random.randint(1, 10, (4, 4))
diag = np.diag(arr4x4)
print(f"Q12: Diagonal sum of 4x4 matrix is {diag.sum()}")

# Q13: Element-wise (*) vs Matrix multiplication (@)
a = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
b = np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
print("Q13: Element-wise:\n", a * b)
print("Matrix Multi:\n", a @ b)

# Q14: Boolean masking for temps > 35
temps = np.random.randint(28, 42, 30)
hot_days = temps[temps > 35]
print(f"Q14: Count of days > 35C: {len(hot_days)}")

# Q15: Normalize array to 0-1
raw = np.array([10, 20, 30, 40, 50])
norm = (raw - raw.min()) / (raw.max() - raw.min())
print(f"Q15: Normalized array: {norm}")

# Q16: Aggregate student marks (axis based)
marks_matrix = np.random.randint(30, 100, (5, 3)) # 5 students, 3 subjects
print(f"Q16: Total marks per student: {marks_matrix.sum(axis=1)}")
print(f"Average marks per student: {marks_matrix.mean(axis=1)}")

# Q17: np.where to replace evens with -1
arr_mixed = np.array([1, 2, 3, 4, 5, 6])
res = np.where(arr_mixed % 2 == 0, -1, arr_mixed)
print(f"Q17: Evens replaced: {res}")



# Q18: DataFrame of 8 students and describe
data = {
    "student_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "section": ["X", "Y", "X", "Z", "Y", "X", "Z", "Y"],
    "marks": [88, 42, 95, 33, 76, 50, 91, 65]
}
df = pd.DataFrame(data)
print("Q18: df.describe():\n", df.describe())

# Q19: Load a provided CSV, report missing values, fill numeric missing with column mean.

df_csv = pd.read_csv("Iris.csv")

# Missing values check karna
print("\nQ19: Missing values count per column in Iris.csv:\n", df_csv.isna().sum())

df_csv = df_csv.fillna(df_csv.mean(numeric_only=True))

print("DataFrame after fillna (first 5 rows):\n", df_csv.head())

# Q20: .loc for marks < 50
fail_students = df.loc[df["marks"] < 50, ["name", "marks"]]
print("\nQ20: Students scoring < 50:\n", fail_students)

# Q21: Groupby section for mean and max
grouped = df.groupby("section")["marks"].agg(["mean", "max"])
print("\nQ21: Groupby Section Stats:\n", grouped)

# Q22: Merge DataFrames
attendance_df = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "attendance": [95, 80, 60, 99, 70, 85, 40, 100]
})
merged = pd.merge(df, attendance_df, on="student_id")
low_att = merged[merged["attendance"] < 75]
print("\nQ22: Attendance < 75%:\n", low_att)


# Q23: Bar chart of average marks per section
plt.figure(figsize=(5, 3))
plt.bar(grouped.index, grouped["mean"], color='cadetblue')
plt.xlabel("Section")
plt.ylabel("Average Marks")
plt.title("Avg Marks by Section")
plt.show()

# Q24: Histogram of marks
plt.figure(figsize=(5, 3))
plt.hist(df["marks"], bins=5, color='orange', edgecolor='black')
plt.xlabel("Marks")
plt.title("Distribution of Student Marks")
plt.show()

# Q25: 1x2 Subplot (line and scatter)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# Left plot: Line chart for marks trend
ax[0].plot(df["student_id"], df["marks"], marker='x', color='blue')
ax[0].set_title("Marks per Student ID")
ax[0].set_xlabel("Student ID")
ax[0].set_ylabel("Marks")

# Right plot: Scatter chart for marks vs attendance
ax[1].scatter(merged["marks"], merged["attendance"], color='green')
ax[1].set_title("Marks vs Attendance")
ax[1].set_xlabel("Marks")
ax[1].set_ylabel("Attendance (%)")

plt.tight_layout()
plt.show()