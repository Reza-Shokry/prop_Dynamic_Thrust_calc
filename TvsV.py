import matplotlib.pyplot as plt
import pandas as pd

static_test_file_path ="V605data.csv"


motor_data = pd.read_csv(static_test_file_path, delimiter=",", header=0)

d = 22
pitch = 7.4
Vmax = 30


def dynamicThrust(RPM, d, pitch, V0):
    ans = 4.392399e-8 * RPM * (d ** 3.5) / (pitch ** 0.5) * (4.23333e-4 * RPM * pitch - V0)
    return ans

def T(RPM):

    j = 0
    n = RPM / 60
    TArray = []
    V0Array = []
    while True:
        V0 = n * (d * 0.0254) * j
        T = dynamicThrust(RPM, d, pitch, V0)
        TArray.append(T)
        V0Array.append(V0)
        j += 0.03
        if V0 >= Vmax:
            break
    return TArray ,V0Array

colors = ['red', 'green', 'blue','orange','purple','pink','gray','brown','lime','navy','gold']
for i in range(0,9):
    TArray, V0Array = T(motor_data["RPM"][2*i+2])
    plt.plot(V0Array, TArray,color=colors[i],label="RPM :"+str(motor_data["RPM"][2*i+2]))
    plt.scatter(0, motor_data["Thrust"][2*i+2]/1000*9.81, color=colors[i], s=10) #To convert grams to newtons ==> /1000*9.81


# Add labels and legend
plt.xlabel('V')
plt.ylabel('T')
plt.title('T vs. V')
plt.legend()
plt.grid()

# Show plot
plt.show()

# #Error
# for i in range(0,len(motor_data)):
#     TArray, V0Array = T(motor_data["RPM"][i])
#     Thrust_motor_data = motor_data["Thrust"][i]/1000*9.81
#     Error = (TArray[0]-Thrust_motor_data)/Thrust_motor_data*100
#     print(Error)
#     plt.bar(motor_data["Throttle"][i],Error,color="mediumvioletred", edgecolor='black',width=1.5)
#
# plt.xlabel('Throttle')
# plt.ylabel('Error %')
# plt.grid()
#
# # Show plot
# plt.show()