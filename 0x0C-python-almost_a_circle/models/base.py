#!/usr/bin/python3
"""base class"""
import json
import csv
import turtle
import random


class Base:
    """Base class for all models"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON-formatted string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            list_data = []
            if list_objs is not None and len(list_objs) > 0:
                for obj in list_objs:
                    list_data.append(obj.to_dictionary())
            f.write(cls.to_json_string(list_data))

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON-formatted string to a list of dictionaries"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads a list of objects from a file in JSON format"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="utf-8") as f:
                data = cls.from_json_string(f.read())
                return [cls.create(**item) for item in data]
        except FileNotFoundError:
            return []

    def update(self, *args, **kwargs):
        """Updates the attributes of the instance"""
        if args and len(args) > 0:
            attr_list = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                if i < len(attr_list):
                    setattr(self, attr_list[i], args[i])
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of the instance"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs to CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = cls.get_fieldnames()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes list_objs from CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                return [cls.create(**row) for row in reader]
        except FileNotFoundError:
            return []

    @classmethod
    def get_fieldnames(cls):
        """Returns a list of fieldnames for CSV serialization"""
        if cls.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            return ["id", "size", "x", "y"]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all the Rectangles and Squares using Turtle graphics"""
        screen = turtle.Screen()
        screen.bgcolor("white")
        for rect in list_rectangles:
            rect.draw()
        for square in list_squares:
            square.draw()
        turtle.done()


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new instance of the Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self):
        """Draw the Rectangle"""
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)

    def __str__(self):
        """Return the string representation of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new instance of the Square class"""
        super().__init__(size, size, x, y, id)

    def draw(self):
        """Draw the Square"""
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(self.width)
            turtle.right(90)

    def __str__(self):
        """Return the string representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)


if __name__ == "__main__":
    # Example usage
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

    # Draw rectangles and squares
    list_rectangles = [Rectangle(100, 40), Rectangle(
        90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)
