import json
import matplotlib.pyplot as plt

# Load existing coordinates from the JSON file, if it exists
try:
    with open("train_xy.json", "r") as file:
        data = json.load(file)
        x_coordinates = data["x"]
        y_coordinates = data["y"]
except FileNotFoundError:
    x_coordinates = []
    y_coordinates = []

# Create a figure and axes
fig, ax = plt.subplots()

# Define a callback function for mouse click events
def onclick(event):
    if event.button == 1:  # Left mouse button
        x_coordinates.append(event.xdata)
        y_coordinates.append(event.ydata)

        # Update the JSON data
        data = {"x": x_coordinates, "y": y_coordinates}
        with open("train_xy.json", "w") as file:
            json.dump(data, file, indent=4)

        # Update the plot with the new point and arrows
        ax.plot(x_coordinates, y_coordinates, 'ro')
        for i in range(len(x_coordinates)-1):
            ax.annotate('', xy=(x_coordinates[i+1], y_coordinates[i+1]), xytext=(x_coordinates[i], y_coordinates[i]),
                        arrowprops={'arrowstyle': '->', 'color': 'black'})
        plt.draw()

# Connect the callback function to the figure's button_press_event
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Display the box or plot your data
# Customize the box dimensions and appearance as needed
box_size = 1
box_coords = [0, box_size, 0, box_size]

# Set the x and y limits of the plot
ax.set_xlim(box_coords[0], box_coords[1])
ax.set_ylim(box_coords[2], box_coords[3])

# Show the plot
plt.show()

print("train_xy saved to coordinates.json")
