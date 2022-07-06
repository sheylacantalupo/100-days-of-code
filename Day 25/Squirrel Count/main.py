import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

color_list = data["Primary Fur Color"].to_list()
print(color_list)
Gray = 0
Cinnamon = 0
Black = 0
for color in color_list:
    if color == "Gray":
        Gray += 1
    elif color == "Cinnamon":
        Cinnamon += 1
    elif color == "Black":
        Black += 1

fur_Color = ["Gray", "Cinnamon", "Black"]
count = [Gray, Cinnamon, Black]
data_dict = {
    "Fur Color": fur_Color,
    "Count": count
}

df = pandas.DataFrame(data_dict)

df.to_csv('squirrel_count.csv')
