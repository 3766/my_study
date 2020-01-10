import json
import math
import csv

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 扁率

def wgs84togcj02(lng, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    if out_of_china(lng, lat):  # 判断是否在国内
        return lng, lat
    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [mglng, mglat]


def gcj02towgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    if out_of_china(lng, lat):
        return lng, lat
    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]


def transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
        0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
        0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret


def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    if lng < 72.004 or lng > 137.8347:
        return True
    if lat < 0.8293 or lat > 55.8271:
        return True
    return False


if __name__ == '__main__':

    with open('handled_total+1.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        column_x = [row[2]for row in reader]
    with open('handled_total+1.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        column_y = [row[3]for row in reader]
    with open('handled_total+1.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        column_x1 = [row[5]for row in reader]
    with open('handled_total+1.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        column_y1 = [row[6]for row in reader]
    my_transformlat=[]
    my_transformlng=[]
    my_transformlat1=[]
    my_transformlng1=[]
    
    with open("out.csv", "w", newline="") as f:
        writers = csv.writer(f)
        for i in range(1,5):
            [a1,b1]=gcj02towgs84(float(column_x[i]), float(column_y[i]))
            [c1,d1]=gcj02towgs84(float(column_x1[i]), float(column_y1[i]))
            writers.writerow([a1,b1,c1,d1])
            # my_transformlat.append(a1)
            # my_transformlng.append(b1)
            # my_transformlat1.append(c1)
            # my_transformlng1.append(d1)
            print(i)
    # #字典中的key值即为csv中列名
    # dataframe = pd.DataFrame({'wgs84lng':my_transformlng,'wgs84lat':my_transformlat,'transformlng1':my_transformlng1,'transformlat1':my_transformlat1})
    # #将DataFrame存储为csv,index表示是否显示行名，default=True
    # dataframe.to_csv("test.csv",sep=',')


    # with open("out.csv", "w", newline="") as f:
    #     writers = csv.writer(f)
    #     writers.writerow(my_transformlat)
    #     writers.writerow(my_transformlng)
    #     writers.writerow(my_transformlat1)
    #     writers.writerow(my_transformlng1)
