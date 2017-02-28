import xml.etree.cElementTree as ET

with open('cal_cnode.txt') as f_nodes_to_latlong:
    content = f_nodes_to_latlong.readlines()

#print(content[20]);
f = open('nodes_for_xml.txt', 'r')
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(line3)
mylist3 = line3.split(",")


root = ET.Element("root")
#3rd shortest path

for nodes3 in mylist3[:-1]:
	doc = ET.SubElement(root, "row")
	latlong = content[int(nodes3)].split(' ')
	ET.SubElement(doc, "lat").text = latlong[2]
	ET.SubElement(doc, "long").text = latlong[1] # may have to switch

tree = ET.ElementTree(root)
tree.write("latlong3.xml")

#print(mylist1[:-1])
#print('\n')
#print(mylist2[:-1])
#print('\n')
#print(mylist3[:-1])

f.close()