import matplotlib.pyplot as plt
language_data = {"JavaScript": 62.3, "HTML": 52.9, "Python": 51, "SQL": 51, "TypeScript": 38.5}
print("Programming Language Usage Data:", language_data)
plt.figure(figsize=(8, 5))
plt.bar(language_data.keys(), language_data.values(), color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel("Programming Languages")
plt.ylabel("Users (%)")
plt.title("Programming Language Usage Percentage")
plt.ylim(0, 70)
plt.grid(axis="y", linestyle="--", alpha=1)
plt.show()