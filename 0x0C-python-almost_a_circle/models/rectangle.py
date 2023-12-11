# models/rectangle.py
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new instance of the Rectangle class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        self.validate_integer("width", value)
        self.validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        self.validate_integer("height", value)
        self.validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x."""
        self.validate_integer("x", value)
        self.validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y."""
        self.validate_integer("y", value)
        self.validate_non_negative("y", value)
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle with '#' symbols, considering x and y offsets."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Override the __str__ method to provide a custom string representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def validate_integer(self, attribute_name, value):
        """Validate if the given value is an integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute_name))

    def validate_positive(self, attribute_name, value):
        """Validate if the given value is positive."""
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute_name))

    def validate_non_negative(self, attribute_name, value):
        """Validate if the given value is non-negative."""
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute_name))

    def update(self, *args, **kwargs):
        """
        Update the attributes with the provided arguments.

        Args:
            *args: Arguments to update the attributes in the order [id, width, height, x, y].
            **kwargs: Keyword arguments to update the attributes by attribute name.
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
