import matplotlib.pyplot as plt
import numpy as np

# Yelp and Google ratings
# OLD
#yelp_ratings = [4.53, 3.7, 4.2, 4.0, 4.5, 3.9]
#google_ratings = [4.8, 4.7, 4.33, 4.4, 4.35, 4.5]
# NEW
yelp_ratings = [4.53, 4.2, 4.33, 4.5, 3.9, 3.9]
google_ratings = [4.8, 4.7, 4.33, 4.4, 4.35, 4.5]
# DATA:
# Name       Yelp   Google
# Joanns     4.53   4.8
# Mays       4.2    4.7
# Murdicks   4.33   4.33
# Murray     4.5    4.4
# Rybas      3.9    4.35
# Sanders    3.9    4.5

# Names for labeling
names = ["Joanns", "Mays", "Murdicks", "Murray", "Rybas", "Sanders"]

# Scatter plot
plt.scatter(google_ratings, yelp_ratings, label="Shops")

# Adding labels for each point
for i, name in enumerate(names):
    plt.text(google_ratings[i], yelp_ratings[i], name, fontsize=8)

# Red line y=x
min_val = min(min(google_ratings), min(yelp_ratings)) - 0.1  # Padding
max_val = max(max(google_ratings), max(yelp_ratings)) + 0.1  # Padding
x = np.linspace(min_val, max_val, 100)
plt.plot(x, x, color='red')

plt.xlim(min_val, max_val)
plt.ylim(min_val, max_val)
plt.xlabel('Google Ratings')
plt.ylabel('Yelp Ratings')
plt.title('Scatter Plot of Yelp vs Google Ratings')
plt.legend()
plt.show()
