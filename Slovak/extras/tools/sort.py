#!/usr/bin/env python
# Script originally by MarkHUK
# Multiple line changes by iBotPeaches
import os, sys, os.path
import string
 
try:
    from xml.etree import ElementTree as ET
except ImportError:
    try:
        from elementtree import ElementTree as ET
    except ImportError:
        try:
            from lxml import etree as ET
        except ImportError:
            print "No usable element tree api found, install lxml or elementtree plz"
            sys.exit(1)
 
def indent(elem, level=0):
    """Insert whitespaces so elements are pretty printed"""
   
    i = "\n" + level*"    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
 
def sort_strings_file(xmlfile,typee):
    """sort all strings within given strings.xml file"""
   
    all_strings = {}
    all_format  = {}
   
    orig_type=typee
   
    # read original file
    tree = ET.ElementTree()
    tree.parse(xmlfile)
 
    # iter over all strings, stick them into dictionary
    for element in list(tree.getroot()):
        all_strings[element.attrib['name']] = element.text
        all_format[element.attrib['name']] = element.get("formatted")
 
    # create new root element and add all strings sorted below
    newroot = ET.Element("resources")
    for key in sorted(all_strings.keys()):
        # Check for IDs
        if typee == "id":
         typee="item"
      
    # set main node type
        newstring = ET.SubElement(newroot, typee)
       
        #add id attrib
        if orig_type == "id":
          newstring.attrib['type']="id"
     
    # continue on
        newstring.attrib['name'] = key
       
        # ibotpeaches - check for % then add formatted=false
        # fix for chinese chars - May 7, 2012
        if all_format[key] == "false":
          newstring.attrib['formatted'] = "false"
     
        newstring.text = all_strings[key]
 
    # Re-indent new root element, aka pretty-format it
    indent(newroot)
 
    # write new root element back to xml file
    newtree = ET.ElementTree(newroot)
    newtree.write(xmlfile, encoding="UTF-8")
   
if __name__ == '__main__':
  # Pass path, or take it from current location, ibot fix
    if (len(sys.argv) > 1):
      path=sys.argv[1]
    else:
      path=os.path.realpath(os.path.dirname(sys.argv[0]))
   
    for root, dirs, files in os.walk((path)):
        for filename in files:
            if filename == "strings.xml":
                realfile = os.path.join(root, filename)
                print "Sorting strings in %s" % realfile
                sort_strings_file(realfile,"string")
            #if filename == "ids.xml":
            #  realfile = os.path.join(root,filename)
            #print "Sorting strings in %s" % realfile
            #sort_strings_file(realfile,"id")
