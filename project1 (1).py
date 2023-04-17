"""
Name: Carter Salna
External Resources Used:
1. csv library
2. json library
3. xml library plus ElementTree
...
"""
import csv
import json
import xml
import xml.etree.ElementTree as ET

def read_csv_file(filename):
    """
    Takes a filename denoting a CSV formatted file.
    Returns an object containing the data from the file.
    The specific representation of the object is up to you.
    The data object will be passed to the write_*_files functions.
    """
    # use csv library to open and read file
    file = open(filename, "r")
    data = list(csv.reader(file, delimiter=","))
    file.close()
    # the initial row is the header column
    header = data[0]
    L = []
    # loop through the whole table
    for j in range(1, len(data)):
        D = {}
        for i in range(len(header)):
            D[header[i]] = data[j][i]
            new_dict = {}
        # same algorithm used in other functions to resort the dictionary
        keys = list(D.keys())
        keys.sort()
        # reassign values and append to new list
        for key in keys:
            new_dict[key] = D.get(key)
        L.append(new_dict)

    return L


def write_csv_file(filename, data):
    """
    Takes a filename (to be writen to) and a data object 
    (created by one of the read_*_file functions). 
    Writes the data in the CSV format.
    """
    # Open file and assign it to file
    file = open(filename, "w", newline='')
    writer = csv.writer(file)
    record = data[0]
    L = []
    # append header row to the table
    for key in record.keys():
        L.append(key)
    writer.writerow(L)

    # loop through data to get values and then add rest of rows
    for i in range(0, len(data)):
        L = list(data[i].values())
        writer.writerow(L)
    file.close()


def read_json_file(filename):
    """
    Similar to read_csv_file, except works for JSON files.
    """
    # open file using json library
    file = open(filename, "r")
    data = json.load(file)
    L = []
    # since json is our intermediate, no data deciphering is needed here
    # except for sorting columns by alpha
    for D in data:
        new_dict = {}
        keys = list(D.keys())
        keys.sort()
        for key in keys:
            new_dict[key] = D.get(key)
        L.append(new_dict)
    return L


def write_json_file(filename, data):
    """
    Writes JSON files. Similar to write_csv_file.
    """
    # Because I use JSON as my intermediate, all I need to do here
    # is to use json dump to write to the new file
    with open(filename, "w") as file:
        json.dump(data, file)

def read_xml_file(filename):
    """
    You should know the drill by now...
    """
    # parse to get the root of the xml
    tree = ET.parse(filename)
    root = tree.getroot()

    # creating an empty list to bc my intermediate form
    L = []
    # loop through root to get the records
    for child in root:
        D = {}
        for att in child:
            D[att.tag] = att.text
        # this is used to sort the dictionary in alphabetical order
        new_dict = {}
        keys = list(D.keys())
        keys.sort()
        # create new dict to reassign values to sorted columns
        for key in keys:
            new_dict[key] = D.get(key)
        L.append(new_dict)
    return L


def write_xml_file(filename, data):
    """
    Feel free to write what you want here.
    """
    #create main data element that holds all of data
    element_main = ET.Element('data')
    # loop through the data and add subelements
    for i in data:
        element1 = ET.SubElement(element_main, 'record')
        # add text to sub elements
        for key in i.keys():
            elem_sub = ET.SubElement(element1, key)
            elem_sub.text = i[key]
    # convert xml to string and then write to file
    final_xml = ET.tostring(element_main)

    with open(filename, "wb") as file:
        file.write(final_xml)



