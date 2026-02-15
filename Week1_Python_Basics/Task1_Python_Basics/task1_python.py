# TASK 1: Python Data Handling Practical
# Internship Month 1

# -----------------------------
# PART 1: List of Numbers
# -----------------------------

numbers = [
    12, 45, 67, 23, 89, 90, 34, 56, 78, 11,
    22, 44, 55, 66, 77, 88, 99, 100, 10, 5,
    15, 25, 35, 65, 75, 85, 95, 40, 50, 60
]

# Mean
mean = sum(numbers) / len(numbers)

# Median
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)
median = (sorted_numbers[n//2] + sorted_numbers[n//2 - 1]) / 2

# Min & Max
minimum = min(numbers)
maximum = max(numbers)

print("Mean:", mean)
print("Median:", median)
print("Minimum:", minimum)
print("Maximum:", maximum)

# -----------------------------
# PART 2: Student Dictionary
# -----------------------------

students = {
    "Ayaan": 88,
    "Sara": 92,
    "Rahul": 76,
    "Nida": 95,
    "Zoya": 90,
    "Arjun": 85,
    "Ibrahim": 80,
    "Meera": 89,
    "Kabir": 78,
    "Ananya": 91
}

# Sort students by marks
top_students = sorted(students.items(), key=lambda x: x[1], reverse=True)

print("\nTop 3 Scorers:")
for student in top_students[:3]:
    print(student[0], "-", student[1])

# -----------------------------
# PART 3: Read Text File
# -----------------------------

file_sum = 0

with open("numbers.txt", "r") as file:
    for line in file:
        file_sum += int(line.strip())

print("\nSum of numbers from file:", file_sum)
