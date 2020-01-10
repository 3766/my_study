import osmnx as ox
import csv
import networkx as nx
import json

with open('Wgs84_and_Mars.csv','r') as csvfile:
    reader = csv.reader(csvfile)
#     column_x = [row[1]for row in reader]
#     column_y = [row[2]for row in reader]
#     column_x1 = [row[3]for row in reader]
#     column_y1 = [row[4]for row in reader]
#     column_x_mars = [row[5]for row in reader]
    column_y_mars = [row[6]for row in reader]
#     column_x1_mars = [row[7]for row in reader]
#     column_y1_mars = [row[8]for row in reader]


with open('Id_wgs84_mars.csv','r') as csvfile:
    reader = csv.reader(csvfile)
#     column_id_y = [row[2]for row in reader]
#     column_id_x = [row[3]for row in reader]
#     column_id = [row[1]for row in reader]
#     column_id_y_mars = [row[4]for row in reader]
    column_id_x_mars = [row[5]for row in reader]

id_dict={}
for i in range(1,len(column_id)):
    id_dict.setdefault(float(column_id[i]),[]).append(float(column_id_y_mars[i]))
    id_dict.setdefault(float(column_id[i]),[]).append(float(column_id_x_mars[i]))


to_mars=[]
column_x_row=[]
column_y_row=[]
column_x_row=[]
column_x_row=[]
with open("Wgs84_path.json","w") as f:
    f.write("[\n")
    for i in range(1,len(column_x)):
        my_dict={"level":1,"number":"001","path":[[None,None,None]]}
        origin_point = (float(column_y[i]), float(column_x[i]))
        destination_point = (float(column_y1[i]), float(column_x1[i]))
        origin_node = ox.get_nearest_node(G, origin_point)
        destination_node = ox.get_nearest_node(G, destination_point)
        origin_node, destination_node
        # find the shortest path between origin and destination nodes
        route = nx.shortest_path(G, origin_node, destination_node, weight='length')
        if i%5000==0:
            print(route)
#         now_point=(float(column_x[i]),float(column_y[i]), 0)
        now_point=(float(column_x_mars[i]),float(column_y_mars[i]), 0)
        
        my_dict["path"][0]=now_point
        for j in range(0,len(route)):
#             将id对应坐标
            now_point=(id_dict[route[j]][0],id_dict[route[j]][1],0)
            my_dict["path"].append(now_point)
        now_point=(float(column_x1_mars[i]),float(column_y1_mars[i]), 0)
        my_dict["path"].append(now_point)
        json.dump(my_dict,f)
        if i !=len(column_x)-1:
            f.write(",\n")
#     按照格式输出
    f.write("\n]")