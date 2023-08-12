import matplotlib.pyplot as plt

data = """1. Joann’s Fudge: 4.5 (104 reviews)
2. Original Murdick’s Fudge of Mackinac Island: 4.0 (63 reviews)
3. Ryba’s Fudge Shops: 3.9 (92 reviews)
4. Joann’s Fudge Shop: 4.8 (11 reviews)
5. Murray Hotel Fudge: 4.5 (11 reviews)
6. May’s Candy Shop: 4.2 (21 reviews)
7. Sanders Chocolate & Ice Cream Shops: 3.8 (33 reviews)
8. Kilwin’s of Mackinac: 3.7 (11 reviews)
9. Sadie’s Ice Cream Parlor: 4.6 (45 reviews)
10. Sanders: 5.0 (3 reviews)"""

ratings = []
counts = []
names = []

for line in data.split("\n"):
    rank, rest = line.split(".", 1)
    name, rest_details = rest.split(":", 1)
    rating, reviews = rest_details.strip().split(" ", 1)
    count = int(reviews.split("(")[1].strip(" reviews)"))

    ratings.append(float(rating))
    counts.append(count)
    names.append(name.strip())

plt.scatter(ratings, counts)
for i, name in enumerate(names):
    plt.text(ratings[i], counts[i], name, fontsize=8)
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")
plt.title("Scatter Plot of Fudge Shops")
plt.xticks(rotation=45)
plt.show()
