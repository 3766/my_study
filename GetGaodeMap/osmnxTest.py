import osmnx as ox 
city=ox.gdf_from_place("南山区,深圳市,中国")
print (city)
ox.plot_shape(ox.project_gdf(city))



import osmnx as ox
import networkx as nx
import os

G = ox.graph_from_place('Shanghai, China', which_result=2, network_type='drive')
fig, ax = ox.plot_graph(ox.project_graph(G))
ox.save_graphml(G, filename='STREETGRAPH_FILENAME')


origin_point = (31.2827320285,121.2106132507)
destination_point = (31.2819500000,121.1651300000)
origin_node = ox.get_nearest_node(G, origin_point)
destination_node = ox.get_nearest_node(G, destination_point)
route = nx.shortest_path(G, origin_node, destination_node, weight='length')
str(route)
distance = nx.shortest_path_length(G, origin_node, destination_node, weight='length')
fig, ax = ox.plot_graph_route(G, route, origin_point=origin_point, destination_point=destination_point)