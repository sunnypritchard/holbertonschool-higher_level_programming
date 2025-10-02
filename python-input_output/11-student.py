#!/usr/bin/python3
"""Module that defines a class Student.
"""


class Student:
    """Class that defines a student by first name, last name and age.
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        return self.__dict__

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only the attributes named in the list
        will be included in the dictionary. Otherwise, all attributes will be
        included.

        Args:
            attrs (list, optional): List of attribute names to include.
                                    Defaults to None.

        Returns:
            dict: The dictionary representation of the Student instance.
        """
        if (
            isinstance(attrs, list)
            and all(isinstance(attr, str) for attr in attrs)
        ):
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary containing the attributes to replace.
        """
        for key, value in json.items():
            setattr(self, key, value)
