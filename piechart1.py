import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'GNB(88%)', 'VC(90%)','QDA(95%)','MLPC(97%)'
sizes = [88,90,95, 97]
explode = (0, 0.1,0,0.1)  # only "explode" the 2nd slice and 4th slice

fig1, ax1 = plt.subplots()
#ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.pie(sizes, explode=explode, labels=labels,shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Accuracy of GNBC vs. VC vs.QDA vs. MLPC')
plt.show()