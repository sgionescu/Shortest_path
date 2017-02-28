
#while inotifywait -e close_write myFile.txt; 
#do
./geodesic
#mv nodes_start_end.txt kshortestpaths/.
#cd kshortestpaths
#./kshortestpaths_2.1
#mv output.txt ../nodes_for_xml.txt
#cd ..
./project_algo # this is for dijkstra
python createXML.py
python createXML2.py
python createXML3.py
rm myFile.txt nodes_for_xml.txt nodes_start_end.txt
cp latlong.xml /var/www/html/.
cp latlong2.xml /var/www/html/.
cp latlong3.xml /var/www/html/.
#cp spath.html /var/www/html/.

rm latlong.xml latlong2.xml latlong3.xml
#rm spath.html

sudo chmod 777 /var/www/html/spath.html
sudo chmod 777 /var/www/html/latlong.xml
sudo chmod 777 /var/www/html/latlong2.xml
sudo chmod 777 /var/www/html/latlong3.xml

chromium-browser http://localhost/spath.html
chromium-browser http://localhost/spath2.html
chromium-browser http://localhost/spath3.html

#done;