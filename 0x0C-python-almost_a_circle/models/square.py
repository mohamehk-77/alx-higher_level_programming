# models/square.py
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new instance of the Square class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size."""
        self.validate_integer("width", value)
        self.validate_positive("width", value)
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Return a dictionary representation of the Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Override the __str__ method to provide a custom string representation."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
