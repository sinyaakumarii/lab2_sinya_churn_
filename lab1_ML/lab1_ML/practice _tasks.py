farh_str = input("Enter temperature in Fahrenheit: ")
fahr = float(farh_str)
celsius = ((fahr - 32)*5/9)
print(f"{fahr}°F is equal to {celsius:.2f}°C")




for num in range(2,101):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num)

n = int(input("Enter an integer: "))

if n & 1 == 0:
    print(f"{n} is Even")
else:
    print(f"{n} is Odd")

def stats(*nums):
    minimum = min(nums)
    maximum = max(nums)
    average = sum(nums) / len(nums)

    return (minimum, maximum, average)


print(stats(10, 20, 30, 40, 50))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares_of_evens = [n**2 for n in numbers if n % 2 == 0]

print(squares_of_evens)

course1 = {"Ali", "Ahmed", "Sara", "John"}
course2 = {"Sara", "John", "Zain", "Fatima"}
both = course1 & course2
only_one = course1 ^ course2

print("Both courses:", both)
print("Only one course:", only_one)


def remove_duplicates(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)
    return result
numbers = [1, 2, 2, 3, 1, 4, 3]
print(remove_duplicates(numbers))

cubes = {num: num**3 for num in range(1, 11)}

print(cubes)

import numpy as np

arr = np.arange(1, 16)

print("Array:", arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Dtype:", arr.dtype)


import numpy as np

arr = np.random.randint(10, 51, size=(5, 5))

print("Array:")
print(arr)
print("Max:", arr.max())
print("Min:", arr.min())
print("Mean:", arr.mean())

import numpy as np
arr = np.arange(1, 21)
matrix = arr.reshape(4, 5)
print("Original array:")
print(arr)
print("Reshaped 4x5 matrix:")
print(matrix)
cols = matrix[:, 1:3]
print("2nd and 3rd columns:")
print(cols)


import numpy as np

scores = np.array([56, 78, 90, 45, 67, 88, 92, 34, 71, 60, 85, 95, 40, 77, 65])
mean_score = scores.mean()
above_mean = scores[scores > mean_score]
print("Scores:", scores)
print("Mean:", mean_score)
print("Scores above mean:", above_mean)


import numpy as np

arr = np.array([-5, 3, -2, 8, 0, -7, 4, -1, 9])

result = np.where(arr < 0, 0, 1)

print("Original array:", arr)
print("Result:", result)

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "subject": ["Math", "Science", "Math", "English", "Science", "Math"],
    "marks": [85, 72, 90, 65, 78, 88]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("Info:")
df.info()

print("Describe:")
print(df.describe())
import pandas as pd

df = pd.read_csv("Iris.csv")

print("Shape:", df.shape)
print("Column names:", df.columns.tolist())
print("First 5 rows:")
print(df.head())


import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "subject": ["Math", "Science", "Math", "English", "Science", "Math"],
    "marks": [85, 72, 90, 65, 78, 88]
}
df = pd.DataFrame(data)
above_80 = df[df["marks"] > 80]
print("Students who scored above 80:")
print(above_80)

import pandas as pd
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "subject": ["Math", "Science", "Math", "English", "Science", "Math"],
    "marks": [85, 72, 90, 65, 78, 88]
}

df = pd.DataFrame(data)
row_loc = df.loc[2]
row_iloc = df.iloc[2]
print("Using .loc:")
print(row_loc)
print("Using .iloc:")
print(row_iloc)

print("Do they match?", row_loc.equals(row_iloc))

import pandas as pd
import numpy as np

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "subject": ["Math", "Science", "Math", "English", "Science", "Math"],
    "marks": [85, np.nan, 90, 65, np.nan, 88]
}

df = pd.DataFrame(data)

print("Missing values per column:")
print(df.isnull().sum())

df["marks"] = df["marks"].fillna(df["marks"].mean())

print("DataFrame after filling missing values:")
print(df)


import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "subject": ["Math", "Science", "Math", "English", "Science", "Math"],
    "marks": [85, 72, 90, 65, 38, 88]
}

df = pd.DataFrame(data)

df["pass_fail"] = df["marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print(df)

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "subject": ["Math", "Science", "Math", "English", "Science", "Math"],
    "marks": [85, 72, 90, 65, 78, 88]
}

df = pd.DataFrame(data)

grouped = df.groupby("subject")["marks"].agg(["mean", "min", "max"])

print(grouped)


import pandas as pd

students = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "marks": [85, 72, 90, 65, 78]
})

attendance = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 6],
    "attendance_pct": [95, 88, 76, 92, 80]
})

merged = pd.merge(students, attendance, on="student_id")

print("Students:")
print(students)
print("Attendance:")
print(attendance)
print("Merged (inner join by default):")
print(merged)

import matplotlib.pyplot as plt
days = list(range(1, 11))
temperatures = [22, 24, 23, 25, 27, 26, 28, 30, 29, 31]
plt.plot(days, temperatures, marker='o', color='blue')
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("10-Day Temperature Readings")
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    "subject": ["Math", "Science", "Math", "English", "Science", "Math"],
    "marks": [85, 72, 90, 65, 78, 88]
}

df = pd.DataFrame(data)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

category_counts = df["subject"].value_counts()
axes[0].bar(category_counts.index, category_counts.values, color='skyblue')
axes[0].set_xlabel("Subject")
axes[0].set_ylabel("Count")
axes[0].set_title("Category Counts")

axes[1].hist(df["marks"], bins=5, color='salmon', edgecolor='black')
axes[1].set_xlabel("Marks")
axes[1].set_ylabel("Frequency")
axes[1].set_title("Marks Distribution")

plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "marks": [85, 72, 90, 65, 78, 88, 45, 92, 76, 60]
}

df = pd.DataFrame(data)

df["marks"].plot(kind="box")

plt.ylabel("Marks")
plt.title("Boxplot of Marks")

plt.show()


