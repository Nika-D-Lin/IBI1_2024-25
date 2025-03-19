import matplotlib.pyplot as plt
uk_countries = {"England": 57.11, "Wales": 3.13, "Northern Ireland": 1.91, "Scotland": 5.45}
china_provinces = {"Zhejiang": 65.77, "Fujian": 41.88, "Jiangxi": 45.28, "Anhui": 61.27, "Jiangsu": 85.15}
sorted_uk = sorted(uk_countries.items(), key=lambda x: x[1], reverse=True)
sorted_china = sorted(china_provinces.items(), key=lambda x: x[1], reverse=True)
print(sorted_uk)
print(sorted_china)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].pie(uk_countries.values(), labels=uk_countries.keys(), autopct='%1.1f%%', startangle=140, colors=["blue", "orange", "green", "red"])
axes[0].set_title("Population Distribution in UK Countries")
axes[1].pie(china_provinces.values(), labels=china_provinces.keys(), autopct='%1.1f%%', startangle=140, colors=["purple", "cyan", "yellow", "pink", "gray"])
axes[1].set_title("Population Distribution in Zhejiang-Neighbouring Provinces")

plt.tight_layout()
plt.show()