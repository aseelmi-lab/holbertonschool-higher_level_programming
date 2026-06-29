#!/usr/bin/python3
"""Module for XML serialization and deserialization."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The output XML filename.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserializes a dictionary from an XML file.

    Args:
        filename (str): The input XML filename.

    Returns:
        dict: The deserialized Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
