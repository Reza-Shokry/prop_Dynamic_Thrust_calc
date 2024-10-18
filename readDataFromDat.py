import pandas as pd
import re
import matplotlib.pyplot as plt

file_folder = "Prop DB/PERFILES_WEB/PERFILES2/"
file_name ="PER3_5x3.dat"
file_path = file_folder+file_name

def readData(file_path):
    header = None

    with open(file_path, 'r') as file:
        content = file.read()
        # جدا کردن دیتافریم‌ها بر اساس یک علامت خاص (در اینجا ما از '#' استفاده می‌کنیم)
        dataframes = content.split('RPM')[1:]

        # لیستی برای نگهداری دیتافریم‌ها
        df_list = []
        RPM_list = []

        # تبدیل هر بخش به یک دیتافریم
        for data in dataframes:
            # حذف فضای اضافی و تقسیم به خطوط
            lines = data.strip().splitlines()

            RPM = re.findall(r'\d+', lines[0])  # to integer
            RPM_list.append(RPM[0])

            # جدا کردن نام ستون‌ها
            header = lines[2].split()

            # جدا کردن داده‌ها
            values = [line.split() for line in lines[4:-1]]

            # ایجاد دیتافریم
            df = pd.DataFrame(values, columns=header)

            float_df = df.astype(float)

            # اضافه کردن دیتافریم به لیست
            df_list.append(float_df)
    return df_list,RPM_list


def plotData(motorDataList,RPM_list,xAxis,yAxis,n):

    motor_data = motorDataList[n]

    plt.plot(motor_data[xAxis],motor_data[yAxis])

    plt.title('RPM = '+RPM_list[n])
    plt.xlabel(xAxis)
    plt.ylabel(yAxis)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    motorDataList,RPM_list = readData(file_path)
    plotData(motorDataList,RPM_list,"V","Ct",22)