import random
import pandas as pd

max_data=[0,0,0,0,0,0]

sensor_data1=[0,0,0,0,0]
sensor_data2=[0,0,0,0,0]
sensor_data3=[0,0,0,0,0]
sensor_data4=[0,0,0,0,0]
sensor_data5=[0,0,0,0,0]
sensor_data6=[0,0,0,0,0]
def noise_sensor_1():
    data = random.randint(40, 100)
    if(data > max_data[0]):
        max_data[0]=data
    sensor_data1.pop(0)
    sensor_data1.append(data)
    df = pd.DataFrame([sensor_data1], columns=['READING_1', 'READING_2', 'READING_3', 'READING_4', 'READING_5'])
    return df

def noise_sensor_2():
    data = random.randint(40, 120)
    if(data > max_data[1]):
        max_data[1]=data
    sensor_data2.pop(0)
    sensor_data2.append(data)
    df = pd.DataFrame([sensor_data2], columns=['READING_1', 'READING_2', 'READING_3', 'READING_4', 'READING_5'])
    return df

def noise_sensor_3():
    data = random.randint(40, 157)
    if(data > max_data[2]):
        max_data[2]=data
    sensor_data3.pop(0)
    sensor_data3.append(data)
    df = pd.DataFrame([sensor_data3], columns=['READING_1', 'READING_2', 'READING_3', 'READING_4', 'READING_5'])
    return df

def noise_sensor_4():
    data = random.randint(40, 210)
    if(data > max_data[3]):
        max_data[3]=data
    sensor_data4.pop(0)
    sensor_data4.append(data)
    df = pd.DataFrame([sensor_data4], columns=['READING_1', 'READING_2', 'READING_3', 'READING_4', 'READING_5'])
    return df

def noise_sensor_5():
    data = random.randint(40, 337)
    if(data > max_data[4]):
        max_data[4]=data
    sensor_data5.pop(0)
    sensor_data5.append(data)
    df = pd.DataFrame([sensor_data5], columns=['READING_1', 'READING_2', 'READING_3', 'READING_4', 'READING_5'])
    return df

def noise_sensor_6():
    data = random.randint(40, 197)
    if(data > max_data[5]):
        max_data[5]=data
    sensor_data6.pop(0)
    sensor_data6.append(data)
    df = pd.DataFrame([sensor_data6], columns=['READING_1', 'READING_2', 'READING_3', 'READING_4', 'READING_5'])
    return df


def noise_data_insights():
    max_value= max(max_data)


    mean_value= sum(max_data) / len(max_data)


    max_index=max_data.index(max_value)

    sensor_info=""
    if(max_index==0):
        sensor_info="SENSOR_1"
    elif(max_index==1):
        sensor_info="SENSOR_2"
    elif(max_index==2):
        sensor_info="SENSOR_3"
    elif(max_index==4):
        sensor_info="SENSOR_4"
    elif(max_index==5):
        sensor_info="SENSOR_5"
    elif(max_index==6):
        sensor_info="SENSOR_6"
    print(f"[{max_data},{mean_value}]")
    return  max_value , mean_value ,sensor_info