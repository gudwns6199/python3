import matplotlib.pyplot as plt
friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

plt.title("Daily vs Number")
plt.xlabel("of friends")
plt.ylabel("daily")

for x, y, label in zip(friends, minutes, labels):
  plt.annotate(label , xy= (x,y), xytext = (5,-5), textcoords="offset points")

plt.show()
