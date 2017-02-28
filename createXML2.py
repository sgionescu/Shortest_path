import xml.etree.cElementTree as ET

with open('cal_cnode.txt') as f_nodes_to_latlong:
    content = f_nodes_to_latlong.readlines()

#print(content[20]);
f = open('nodes_for_xml.txt', 'r')

line1 = f.readline()
line2 = f.readline()
mylist2 = line2.split(",")

root = ET.Element("root")
#2nd shortest path


for nodes2 in mylist2[:-1]:
	doc = ET.SubElement(root, "row")
	latlong = content[int(nodes2)].split(' ')
	ET.SubElement(doc, "lat").text = latlong[2]
	ET.SubElement(doc, "long").text = latlong[1] # may have to switch

tree = ET.ElementTree(root)
tree.write("latlong2.xml")

f.close()