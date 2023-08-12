# Import the matplotlib.pyplot library to create plots and visualize data
import matplotlib.pyplot as plt

# Define a multi-line string that contains the rating, review count, and name of each fudge shop
data = """5.0 (5):	Murray Hotel Fudge Company at the Murray Hotel
4.8 (276):	Joann's Fudge
...
4.1 (36):	Murdick's Fudge Kitchen"""

# Initialize empty lists to store ratings, counts, and names for each fudge shop
ratings = []
counts = []
names = []

# Loop through each line in the data string
for line in data.split("\n"):
    # Split the line into rating and the rest of the string (reviews and name)
    rating, rest = line.split(" ", 1)
    # Split the rest of the string into count and name using the colon as a separator
    count_name = rest.split(":")
    # Extract the count by splitting the string, getting the number inside the parentheses, and converting it to an integer
    count = int(count_name[0].split("(")[1].strip(")"))

    # Append the rating (converted to float), count, and name to the respective lists
    ratings.append(float(rating))
    counts.append(count)
    names.append(count_name[1].strip())

# Create a scatter plot using the ratings (x-axis) and counts (y-axis)
plt.scatter(ratings, counts)
# Loop through the names, ratings, and counts, adding a text label to each point in the plot
for i, name in enumerate(names):
    plt.text(ratings[i], counts[i], name, fontsize=8)
# Add labels to the x and y axes
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")
# Add a title to the plot
plt.title("Scatter Plot of Fudge Shops")
# Rotate the x-axis labels by 45 degrees for better visibility
plt.xticks(rotation=45)
# Display the plot
plt.show()
