#!/bin/bash

for file in $(find -type f -name *.xml); do

java -jar /home/ingbrzy/miui/roms/sort_res_xml.jar $file

done


