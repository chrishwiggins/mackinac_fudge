import matplotlib.pyplot as plt

# Yelp and Google ratings
yelp_ratings = [4.53, 3.7, 4.2, 4.0, 4.5, 3.9]
google_ratings = [4.8, 4.7, 4.33, 4.4, 4.35, 4.5]

# Names for labeling
names = ["Joanns", "Mays", "Murdicks", "Murray", "Rybas", "Sanders"]

# Scatter plot
plt.scatter(google_ratings, yelp_ratings, label="Shops")

# Adding labels for each point
for i, name in enumerate(names):
    plt.text(google_ratings[i], yelp_ratings[i], name, fontsize=8)

plt.xlabel("Google Ratings")
plt.ylabel("Yelp Ratings")
plt.title("Scatter Plot of Yelp vs Google Ratings")
plt.legend()
plt.show()
