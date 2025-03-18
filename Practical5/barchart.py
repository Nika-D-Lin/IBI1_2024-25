import matplotlib.pyplot as plt
import numpy as np

languages = ["JavaScript", "HTML", "Python", "SQL", "TypeScript"]
users = {
    "JavaScript": 62.3,
    "HTML": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
}
x = np.arange(len(languages)) 
y = list(users.values())     
fig, ax = plt.subplots()
rects = ax.bar(x, y, width=0.5, label="Usage Percentage", color="skyblue")
ax.bar_label(rects, padding=3)
ax.set_ylabel("Percentage (%)")
ax.set_title("Users by Programming Language")
ax.set_xticks(x)
ax.set_xticklabels(languages)

ax.legend()
ax.set_ylim(0, 100)
plt.show()