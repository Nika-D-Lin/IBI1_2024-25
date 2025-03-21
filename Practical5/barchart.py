import matplotlib.pyplot as plt #import the function to create the graph
language_data = {"JavaScript": 62.3, "HTML": 52.9, "Python": 51, "SQL": 51, "TypeScript": 38.5}
print("Programming Language Usage Data:", language_data)
plt.figure(figsize=(8, 5)) #create a graph that is 8 in width and 5 in height
plt.bar(language_data.keys(), language_data.values(), color=['blue', 'green', 'red', 'purple', 'orange']) #bar(x,y,color)
plt.xlabel("Programming Languages") #the lable of x axis
plt.ylabel("Users (%)") #the lable of y axis
plt.title("Programming Language Usage Percentage") #the title of the whole
plt.ylim(0, 70) #the range of y axis
plt.grid(axis="y", linestyle="--", alpha=1) #add dotted line in y axis
plt.show()

selected_language = "Python"
if selected_language in language_data:
    print(f"The percentage of developers using {selected_language} is {language_data[selected_language]}%.") #use the key to find the value
else:
    print("Selected language not found in the dataset.")