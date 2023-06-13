import json
import matplotlib.pyplot as plt

# load existing data from the JSON file if it exists
try:
    with open("train_xy.json", "r") as file:
        data = json.load(file)
        x_coordinates = data["x"]
        y_coordinates = data["y"]
except FileNotFoundError:
    x_coordinates = []
    y_coordinates = []

fig, ax = plt.subplots()

# callback function for mouse click events
def onclick(event):
    if event.button == 1:  
        x_coordinates.append(event.xdata)
        y_coordinates.append(event.ydata)

        # update the JSON data
        data = {"x": x_coordinates, "y": y_coordinates}
        with open("train_xy.json", "w") as file:
            json.dump(data, file, indent=4)

        # update the plot 
        ax.plot(x_coordinates, y_coordinates, 'ro')
        for i in range(len(x_coordinates)-1):
            ax.annotate('', xy=(x_coordinates[i+1], y_coordinates[i+1]), xytext=(x_coordinates[i], y_coordinates[i]),
                        arrowprops={'arrowstyle': '->', 'color': 'black'})
        plt.draw()

# connect the callback function to the button_press_event
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# display the box or plot your data
# customize the box dimensions and appearance as needed
box_size = 1
box_coords = [0, box_size, 0, box_size]

ax.set_xlim(box_coords[0], box_coords[1])
ax.set_ylim(box_coords[2], box_coords[3])

plt.show()

print("train_xy saved to coordinates.json")
