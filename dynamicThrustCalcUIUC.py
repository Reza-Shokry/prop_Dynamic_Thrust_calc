import matplotlib.pyplot as plt
import readDataFromTXT as data
import numpy as np


def dynamicThrust(RPM, d, pitch, V0):
    ans = 4.392399e-8 * RPM * (d ** 3.5) / (pitch ** 0.5) * (4.23333e-4 * RPM * pitch - V0)
    return ans

file_folder = "UIUC-propDB/volume-2/data/"
file_name ="mit_5x4_0363rd_3032.txt"
file_path = file_folder+file_name


motor_data,RPM,d,pitch = data.readData(file_path,file_name)

RPM = float(RPM)
j = 0
n = RPM / 60

CTArray = []
jArray = motor_data['J']


#define a counter
i =0

while True:
    j = jArray[i]
    if (j != np.NaN):
        V0 = n * (d * 0.0254) * j
        T = dynamicThrust(RPM, d, pitch, V0)
        CT = T / (1.225 * n ** 2 * (d * 0.0254) ** 4)
        CTArray.append(CT)
    i += 1
    if i == len(jArray):
        break


plt.plot(jArray, CTArray, label='Theoretical')
plt.plot(jArray, motor_data["CT"], label='test data')

# Add labels and legend
plt.xlabel('J')
plt.ylabel('CT')
plt.title('RPM : '+str(RPM))
plt.legend()
plt.grid()

# Show plot
plt.show()
