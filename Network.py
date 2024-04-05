
# Python program to read
# json file
import json
import folium

 
# Opening JSON file
f = open('C:/Users/sampr/Desktop/TU Munich/LKN Hiwi/nobel-germany.json')
 
# returns JSON object as 
# a dictionary
data=json.load(f)
# print(data)
mymap = folium.Map(location=[51.1657, 10.4515], zoom_start=6)


# plot each node on the map

for node in data['networkStructure']['node']:
    long = float(node['coordinates']['lon'])
    lati = float(node['coordinates']['lat'])
    node_id = node['id']
    # print (node1)
    pop_up = folium.Popup(node_id, parse_html=True)
    # folium.CircleMarker([lati, long],color='black',fill=True, fill_color='white', popup=pop_up,tooltip=node_id).add_to(mymap)
    folium.Marker([lati, long], tooltip=node_id).add_to(mymap)

for link in data['networkStructure']['links']:
    source_node = next(node for node in data['networkStructure']['node'] if node['id'] == link['source'])
    # print(source_node)
    target_node = next(node for node in data['networkStructure']['node'] if node['id'] == link['target'])
    # print(target_node)
    
    coordinates = [
        (float(source_node['coordinates']['lat']), float(source_node['coordinates']['lon'])),
        (float(target_node['coordinates']['lat']), float(target_node['coordinates']['lon']))
    ]
    
    # print (coordinates)
    id=link['id']
    folium.PolyLine(locations=coordinates, color='black',popup=id,tooltip=id).add_to(mymap)
    # source = (link['source'])
    # print(source)
    # target = link['target'] 
    # print(target)
#   # folium.PolyLine(locations=[source, target], color="blue", weight=2.5, opacity=1).add_to(mymap)

mymap.save("nobel-germany_map.html")
 
