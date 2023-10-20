import random
import pandas as pd



sensor_data1=[0,0,0,0,0]
sensor_data2=[0,0,0,0,0]
sensor_data3=[0,0,0,0,0]
sensor_data4=[0,0,0,0,0]
sensor_data5=[0,0,0,0,0]
sensor_data6=[0,0,0,0,0]
def noise_sensor_1():
    data = random.randint(40, 97)
    # sensor_data = [0, 0, 0, 0, 0]
    sensor_data1.pop(0)
    sensor_data1.append(data)
    df = pd.DataFrame([sensor_data1], columns=['READING_1', 'READING_2', 'READING_3', 'READING_4', 'READING_5'])
    return df

def noise_sensor_2():
    data = random.randint(40, 97)
    # sensor_data = [0, 0, 0, 0, 0]
    sensor_data2.pop(0)
    sensor_data2.append(data)
    df = pd.DataFrame([sensor_data2], columns=['READING_1', 'READING_2', 'READING_3', 'READING_4', 'READING_5'])
    return df

def noise_sensor_3():
    data = random.randint(40, 97)
    # sensor_data = [0, 0, 0, 0, 0]
    sensor_data3.pop(0)
    sensor_data3.append(data)
    df = pd.DataFrame([sensor_data3], columns=['READING_1', 'READING_2', 'READING_3', 'READING_4', 'READING_5'])
    return df

def noise_sensor_4():
    data = random.randint(40, 97)
    # sensor_data = [0, 0, 0, 0, 0]
    sensor_data4.pop(0)
    sensor_data4.append(data)
    df = pd.DataFrame([sensor_data4], columns=['READING_1', 'READING_2', 'READING_3', 'READING_4', 'READING_5'])
    return df

def noise_sensor_5():
    data = random.randint(40, 97)
    # sensor_data = [0, 0, 0, 0, 0]
    sensor_data5.pop(0)
    sensor_data5.append(data)
    df = pd.DataFrame([sensor_data5], columns=['READING_1', 'READING_2', 'READING_3', 'READING_4', 'READING_5'])
    return df

def noise_sensor_6():
    data = random.randint(40, 97)
    # sensor_data = [0, 0, 0, 0, 0]
    sensor_data6.pop(0)
    sensor_data6.append(data)
    df = pd.DataFrame([sensor_data6], columns=['READING_1', 'READING_2', 'READING_3', 'READING_4', 'READING_5'])
    return df

# Example of how to use these functions to generate data for each sensor
# sensor_1_data = noise_sensor_1()
# sensor_2_data = noise_sensor_2()
# sensor_3_data = noise_sensor_3()
# sensor_4_data = noise_sensor_4()
# sensor_5_data = noise_sensor_5()
# sensor_6_data = noise_sensor_6()

