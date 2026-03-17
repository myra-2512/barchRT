import matplotlib.pyplot as plt

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
july = [12,15,11,9,1,9,21]
aug = [17,5,2,11,1,8,29]

x = range(len(days))
width = 0.35

plt.figure(figsize=(10,6))
plt.bar([p - width/2 for p in x], july, width=width, label='July', color='green', edgecolor='black', alpha=0.7)
plt.bar([p + width/2 for p in x], aug, width=width, label='August', color='orange', edgecolor='black', alpha=0.7)

plt.xticks(x, days)
plt.xlabel('Days of the Week')
plt.ylabel('Birth Rate')
plt.title('Birth Rate in July vs August')
plt.legend()
plt.show()