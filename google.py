import matplotlib.pyplot as plt

data = """5.0 (5):	Murray Hotel Fudge Company at the Murray Hotel
4.8 (276):	Joann's Fudge
4.8 (14):	Ryba's Fudge Shop - Mall Store
4.7 (53):	May's Candy Shop
4.6 (519):	Doud's Market
4.6 (5):	Ryba's Fudge Shops: Corby Store
4.5 (255):	Sanders Chocolate & Ice Cream Shoppe - Mackinac
4.4 (775):	Murray Hotel
4.4 (163):	Original Murdick's Fudge
4.3 (189):	Ryba's Fudge Shop - Cornerstore
4.1 (36):	Murdick's Fudge Kitchen"""

ratings = []
counts = []
names = []

for line in data.split("\n"):
    rating, rest = line.split(" ", 1)
    count_name = rest.split(":")
    count = int(count_name[0].split("(")[1].strip(")"))

    ratings.append(float(rating))
    counts.append(count)
    names.append(count_name[1].strip())

plt.scatter(ratings, counts)
for i, name in enumerate(names):
    plt.text(ratings[i], counts[i], name, fontsize=8)
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")
plt.title("Scatter Plot of Fudge Shops")
plt.xticks(rotation=45)
plt.show()
