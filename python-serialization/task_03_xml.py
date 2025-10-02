#!/usr/bin/python3
"""Module for serializing and deserializing to XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML format and save to a file.

    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The name of the file to save the XML data
    """

    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)

        if isinstance(value, bool):
            child.set('type', 'bool')
            child.text = str(value)
        elif isinstance(value, int):
            child.set('type', 'int')
            child.text = str(value)
        elif isinstance(value, float):
            child.set('type', 'float')
            child.text = str(value)
        elif isinstance(value, str):
            child.set('type', 'str')
            child.text = value
        elif value is None:
            child.set('type', 'none')
            child.text = ''
        else:
            child.set('type', 'str')
            child.text = str(value)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file and return a Python dictionary.

    Args:
        filename (str): The name of the XML file to read

    Returns:
        dict: The deserialized dictionary
    """

    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    for child in root:
        key = child.tag
        value_type = child.get('type', 'str')
        text = child.text

        if value_type == 'bool':
            value = text == 'True'
        elif value_type == 'int':
            value = int(text) if text else 0
        elif value_type == 'float':
            value = float(text) if text else 0.0
        elif value_type == 'none':
            value = None
        else:
            value = text if text is not None else ''

        dictionary[key] = value

    return dictionary
