import matplotlib.pyplot as plt
import pandas as pd

datasheet_file_path = "motocalc data/U7-16-5.4-dsh.csv"
motocalc_file_path = "motocalc data/U7-16-5.4-ESC2.2-6s.csv"

ds_data = pd.read_csv(datasheet_file_path, delimiter=",", header=0)
mc_data = pd.read_csv(motocalc_file_path, delimiter=",", header=0)

x_axis = "Throttle"
y_axis = "Power"
name = datasheet_file_path.split("/")[1].split('-')[0]
d = datasheet_file_path.split("/")[1].split('-')[1]
p = datasheet_file_path.split("/")[1].split('-')[2]


plt.plot(ds_data[x_axis], ds_data[y_axis], label="Company data")
plt.plot(mc_data[x_axis], mc_data[y_axis], label="MotoCalc data")


# Add labels and legend
plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.title(name + " " + d + "*" + p)
plt.legend()
plt.grid()

# Show plot
plt.show()