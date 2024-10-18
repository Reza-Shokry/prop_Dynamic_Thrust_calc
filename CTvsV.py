import matplotlib.pyplot as plt
import pandas as pd

static_test_file_path ="V605data.csv"


motor_data = pd.read_csv(static_test_file_path, delimiter=",", header=0)

# RPM = 12000
d = 22
pitch = 7.4
Vmax = 25
# n = RPM / 60


def dynamicThrust(RPM, d, pitch, V0):
    ans = 4.392399e-8 * RPM * (d ** 3.5) / (pitch ** 0.5) * (4.23333e-4 * RPM * pitch - V0)
    return ans

def CT(RPM):
    j = 0
    CTArray = []
    V0Array = []
    n = RPM / 60
    while True:
        V0 = n * (d * 0.0254) * j
        T = dynamicThrust(RPM, d, pitch, V0)
        CT = T / (1.225 * n ** 2 * (d * 0.0254) ** 4)
        CTArray.append(CT)
        V0Array.append(V0)
        j += 0.01
        if V0 >= Vmax:
            break
    return CTArray ,V0Array

colors = ['red', 'green', 'blue','orange','purple','pink','gray','brown','lime','navy','gold']
for i in range(0,10):
    CTArray, V0Array = CT(motor_data["RPM"][2*i])
    plt.plot(V0Array, CTArray,color=colors[i],label=str(motor_data["RPM"][2*i]))
    plt.scatter(0, motor_data["CT"][2*i], color=colors[i], s=10)

print(motor_data["RPM"])

# Add labels and legend
plt.xlabel('V')
plt.ylabel('CT')
plt.title('CT vs. V')
plt.legend()
plt.grid()

# Show plot
plt.show()