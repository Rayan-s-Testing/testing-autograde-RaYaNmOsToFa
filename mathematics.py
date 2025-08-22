class Mathematics:
    check = 1
    def __init__(self, side=0):
        """Initializes the Mathematics class."""
        self.side = 0
    
    def add(self, a, b):
        """Returns the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Returns the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Returns the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Returns the quotient of a and b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b