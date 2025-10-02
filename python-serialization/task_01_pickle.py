#!/usr/bin/python3
"""Module for serialization and deserialization using pickle."""
import pickle


class CustomObject:
    """A custom class that demonstrates serialization with pickle."""

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the person
            age (int): The age of the person
            is_student (bool): Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes in a formatted way."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
        print()  # Empty line after display

    def serialize(self, filename):
        """
        Serialize the current object instance to a file.

        Args:
            filename (str): The name of the file to save the serialized object

        Returns:
            bool: True if successful, None if an error occurred
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            return True
        except (IOError, pickle.PicklingError) as e:
            print(f"Error serializing object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): The name of the file containing the
                serialized object

        Returns:
            CustomObject: The deserialized object, or None if an error occurred
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except (IOError, FileNotFoundError,
                pickle.UnpicklingError, EOFError) as e:
            print(f"Error deserializing object: {e}")
            return None
