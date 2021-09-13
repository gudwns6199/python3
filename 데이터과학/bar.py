from collections import Counter
import matplotlib.pyplot as plt
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
rate = Counter(min(90, grade // 10 * 10) for grade in grades)

plt.bar([x + 5 for x in rate.keys()], rate.values(), width = 10, edgecolor = 'black')

plt.title("Grade")
plt.xlabel("grades")
plt.ylabel("students")
plt.xticks(range(0,101,10))

plt.show()
