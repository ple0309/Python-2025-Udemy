#********************  Practicing with CSV data *******************
#******************************************************************
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

#******************************************************************
# # Understanding about csv library
# # Using to hold a single column of data from this table
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
# print(temperatures)

#******************************************************************
# #Understanding about pandas library
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# print(data["temp"]) #Reading first row to hold name of columns.

#******************************************************************
# #Using pandas documentation
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))         #DataFrame(2-dimension)
# print(type(data["temp"])) #Series(1-dimension)

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get Data in Columns *****************************
# print(data["condition"])
# print(data.condition) #OR print(data.temp) or print(data.day)
# # Be careful when in weather_data file having Condition with Upper C
# # print(data["Condition"]) #And print(data.Condition) as well
#
# #Get Data in Row *********************************
# print(data[data.day == "Monday"])
# print(data[data["day"] == "Monday"])
# print(data[data.temp == data.temp.max()])

# #Getting monday row then print condition of that row.
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# #Create a dataframe from scratch ******************
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores":[76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")



#********************  Squirrel Count Practice ********************
#******************************************************************
#Fur Color, Count
#Grey, red, black
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey = data[data["Primary Fur Color"] == "Gray"]
red = data[data["Primary Fur Color"] == "Cinnamon"]
black = data[data["Primary Fur Color"] == "Black"]
data_list = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [len(grey), len(red), len(black)]
}
df = pandas.DataFrame(data_list)
df.to_csv("squirrel_count.csv")