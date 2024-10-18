import matplotlib.pyplot as plt
import readDataFromDat as data
import numpy as np


def dynamicThrust(RPM, d, pitch, V0):
    ans = 4.392399e-8 * RPM * (d ** 3.5) / (pitch ** 0.5) * (4.23333e-4 * RPM * pitch - V0)
    return ans


def C_T(j, d, p):
    # correlation for 4<D<6 , 2<P<5.5 and 0.86<D/P<1.5
    x = j * d / p
    y = -0.123468 * x ** 2 + 0.031706 * x + 0.124147
    return y * p / d


file_path = "Prop DB/PERFILES_WEB/PERFILES2/PER3_21x13WE.dat"

motorDataList, RPM_list = data.readData(file_path)

print(f"maximum data number is {len(RPM_list)}, which is the difference of data in RPM")
data_num = 5
RPM = float(RPM_list[data_num])
d = 21
pitch = 13
j = 0
n = RPM / 60

CTArray = []
motor_data = motorDataList[data_num]
jArray = motor_data['J']

# Remove nan Value
# jArray = jArray.dropna()

# define a counter
i = 0

while True:
    j = jArray[i]
    if (j != np.NaN):
        V0 = n * (d * 0.0254) * j
        # To use the gabriel stapless formula
        T = dynamicThrust(RPM, d, pitch, V0)
        CT = T / (1.225 * n ** 2 * (d * 0.0254) ** 4)
        # To use the correlation
        # CT = C_T(j, d, pitch)

        CTArray.append(CT)
    i += 1
    if i == len(jArray):
        break

plt.plot(jArray, CTArray, label='Theoretical')
plt.plot(jArray, motor_data["Ct"], label='Company data')

# Add labels and legend
plt.xlabel('J')
plt.ylabel('CT')
plt.title('RPM : ' + str(round(RPM)))
plt.legend()
plt.grid()

# Show plot
plt.show()

# error = -(CTArray - motor_data["Ct"])
#
# plt.bar(jArray, error)
#
# # Add labels and legend
# plt.xlabel('J')
# plt.ylabel('delta CT')
# plt.title('RPM : '+str(RPM))
# plt.grid()
#
# # Show plot
# plt.show()
