# import csv 
import pandas

# # with open('weather_data.csv','r') as weather_data:
# #     data = csv.reader(weather_data)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# print(data)
# # tempratures = data["temp"]
# # average_temp = round(sum(tempratures)/ len(tempratures), 2)
# # print(f"Average temperature is {average_temp}")

# average = round(data["temp"].mean(), 2)
# print(f"Average temperature is {average}")

# max = data["temp"].max()
# print(f"The maximum temperature is {max}")

# print(data[data.day == "Wednesday"])

# max_temp_day = data[data.temp == data.temp.max()]
# print(max_temp_day)


# monday = data[data.day == "Monday"]
# temp_f = round((monday.temp.iloc[0] * 9/5) + 32) 
# print(f"{monday.temp.iloc[0]}C is equal to {temp_f}F") 

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Count occurrences of each fur color
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

# Store in a dictionary
squirrel_count = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [grey_count, black_count, cinnamon_count]
}

# Convert to DataFrame
data_frame = pandas.DataFrame(squirrel_count)

# Save to CSV
data_frame.to_csv("squirrel_count.csv", index=False)

print("CSV file saved successfully!")