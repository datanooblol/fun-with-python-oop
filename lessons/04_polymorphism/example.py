"""
Lesson 04: Polymorphism
Demonstrates: Duck typing, method overloading, operator overloading, polymorphic behavior
"""

# Example 1: Duck Typing - "If it walks like a duck and quacks like a duck..."
# Python doesn't care about the type, only that the object has the required methods
class Duck:
    """Duck class."""
    
    def speak(self) -> str:
        """Duck speaks.
        
        Returns:
            str: Duck sound.
        """
        return "Quack!"
    
    def fly(self) -> str:
        """Duck flies.
        
        Returns:
            str: Flying action.
        """
        return "Duck is flying"

class Dog:
    """Dog class."""
    
    def speak(self) -> str:
        """Dog speaks.
        
        Returns:
            str: Dog sound.
        """
        return "Woof!"
    
    def fly(self) -> str:
        """Dog 'flies' (humorously).
        
        Returns:
            str: Flying action.
        """
        return "Dog can't fly, but trying!"

class Airplane:
    """Airplane class."""
    
    def speak(self) -> str:
        """Airplane speaks.
        
        Returns:
            str: Airplane sound.
        """
        return "Whoooosh!"
    
    def fly(self) -> str:
        """Airplane flies.
        
        Returns:
            str: Flying action.
        """
        return "Airplane is flying at 500mph"

def make_it_speak_and_fly(thing: object) -> None:
    """Polymorphic function - works with any object that has speak() and fly().
    
    Args:
        thing (object): Any object with speak() and fly() methods.
    """
    print(f"{thing.speak()}")
    print(f"{thing.fly()}")

duck = Duck()
dog = Dog()
plane = Airplane()

print("Duck Typing Demo:")
make_it_speak_and_fly(duck)
print()
make_it_speak_and_fly(dog)
print()
make_it_speak_and_fly(plane)


# Example 2: Polymorphism with Inheritance
class Shape:
    """Base shape class."""
    
    def area(self) -> float:
        """Calculate area.
        
        Returns:
            float: Area value.
        """
        return 0.0
    
    def perimeter(self) -> float:
        """Calculate perimeter.
        
        Returns:
            float: Perimeter value.
        """
        return 0.0

class Rectangle(Shape):
    """Rectangle shape."""
    
    def __init__(self, width: float, height: float) -> None:
        """Initialize Rectangle.
        
        Args:
            width (float): Rectangle width.
            height (float): Rectangle height.
        """
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """Calculate rectangle area.
        
        Returns:
            float: Area value.
        """
        return self.width * self.height
    
    def perimeter(self) -> float:
        """Calculate rectangle perimeter.
        
        Returns:
            float: Perimeter value.
        """
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle shape."""
    
    def __init__(self, radius: float) -> None:
        """Initialize Circle.
        
        Args:
            radius (float): Circle radius.
        """
        self.radius = radius
    
    def area(self) -> float:
        """Calculate circle area.
        
        Returns:
            float: Area value.
        """
        return 3.14159 * self.radius ** 2
    
    def perimeter(self) -> float:
        """Calculate circle circumference.
        
        Returns:
            float: Circumference value.
        """
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    """Triangle shape."""
    
    def __init__(self, base: float, height: float, side1: float, side2: float) -> None:
        """Initialize Triangle.
        
        Args:
            base (float): Triangle base.
            height (float): Triangle height.
            side1 (float): First side length.
            side2 (float): Second side length.
        """
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    def area(self) -> float:
        """Calculate triangle area.
        
        Returns:
            float: Area value.
        """
        return 0.5 * self.base * self.height
    
    def perimeter(self) -> float:
        """Calculate triangle perimeter.
        
        Returns:
            float: Perimeter value.
        """
        return self.base + self.side1 + self.side2

def print_shape_info(shape: Shape) -> None:
    """Polymorphic function - works with any Shape subclass.
    
    Args:
        shape (Shape): Any shape object.
    """
    print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")

shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(6, 4, 5, 5)
]

print("\n\nPolymorphism with Inheritance:")
for shape in shapes:
    print_shape_info(shape)


# Example 3: Operator Overloading (Magic Methods)
class Vector:
    """2D Vector class with operator overloading."""
    
    def __init__(self, x: float, y: float) -> None:
        """Initialize Vector.
        
        Args:
            x (float): X coordinate.
            y (float): Y coordinate.
        """
        self.x = x
        self.y = y
    
    def __add__(self, other: 'Vector') -> 'Vector':
        """Add two vectors using + operator.
        
        Args:
            other (Vector): Another vector.
            
        Returns:
            Vector: Sum of vectors.
        """
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        """Subtract vectors using - operator.
        
        Args:
            other (Vector): Another vector.
            
        Returns:
            Vector: Difference of vectors.
        """
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float) -> 'Vector':
        """Multiply vector by scalar using * operator.
        
        Args:
            scalar (float): Scalar value.
            
        Returns:
            Vector: Scaled vector.
        """
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other: 'Vector') -> bool:
        """Check equality using == operator.
        
        Args:
            other (Vector): Another vector.
            
        Returns:
            bool: True if equal, False otherwise.
        """
        return self.x == other.x and self.y == other.y
    
    def __str__(self) -> str:
        """String representation.
        
        Returns:
            str: Vector as string.
        """
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        """Developer representation.
        
        Returns:
            str: Vector representation.
        """
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print("\n\nOperator Overloading:")
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3 = {v1 * 3}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")


# Example 4: Method Overloading (Python style with default arguments)
class Calculator:
    """Calculator with method overloading using default arguments."""
    
    def add(self, a: float, b: float = 0, c: float = 0) -> float:
        """Add numbers (supports 1, 2, or 3 arguments).
        
        Args:
            a (float): First number.
            b (float): Second number (optional).
            c (float): Third number (optional).
            
        Returns:
            float: Sum of numbers.
        """
        return a + b + c
    
    def multiply(self, *args: float) -> float:
        """Multiply any number of arguments.
        
        Args:
            *args (float): Variable number of arguments.
            
        Returns:
            float: Product of all numbers.
        """
        result = 1
        for num in args:
            result *= num
        return result

calc = Calculator()
print("\n\nMethod Overloading (Python style):")
print(f"add(5) = {calc.add(5)}")
print(f"add(5, 3) = {calc.add(5, 3)}")
print(f"add(5, 3, 2) = {calc.add(5, 3, 2)}")
print(f"multiply(2, 3) = {calc.multiply(2, 3)}")
print(f"multiply(2, 3, 4) = {calc.multiply(2, 3, 4)}")
print(f"multiply(2, 3, 4, 5) = {calc.multiply(2, 3, 4, 5)}")


# Example 5: Real-world Scenario - Payment Processing
class PaymentProcessor:
    """Base payment processor."""
    
    def process_payment(self, amount: float) -> str:
        """Process payment.
        
        Args:
            amount (float): Payment amount.
            
        Returns:
            str: Payment result.
        """
        return f"Processing ${amount}"

class CreditCardProcessor(PaymentProcessor):
    """Credit card payment processor."""
    
    def __init__(self, card_number: str) -> None:
        """Initialize credit card processor.
        
        Args:
            card_number (str): Credit card number.
        """
        self.card_number = card_number
    
    def process_payment(self, amount: float) -> str:
        """Process credit card payment.
        
        Args:
            amount (float): Payment amount.
            
        Returns:
            str: Payment result.
        """
        return f"Charging ${amount} to credit card ending in {self.card_number[-4:]}"

class PayPalProcessor(PaymentProcessor):
    """PayPal payment processor."""
    
    def __init__(self, email: str) -> None:
        """Initialize PayPal processor.
        
        Args:
            email (str): PayPal email.
        """
        self.email = email
    
    def process_payment(self, amount: float) -> str:
        """Process PayPal payment.
        
        Args:
            amount (float): Payment amount.
            
        Returns:
            str: Payment result.
        """
        return f"Charging ${amount} to PayPal account {self.email}"

class CryptoProcessor(PaymentProcessor):
    """Cryptocurrency payment processor."""
    
    def __init__(self, wallet_address: str) -> None:
        """Initialize crypto processor.
        
        Args:
            wallet_address (str): Crypto wallet address.
        """
        self.wallet_address = wallet_address
    
    def process_payment(self, amount: float) -> str:
        """Process crypto payment.
        
        Args:
            amount (float): Payment amount.
            
        Returns:
            str: Payment result.
        """
        return f"Charging ${amount} to crypto wallet {self.wallet_address[:10]}..."

def checkout(processor: PaymentProcessor, amount: float) -> None:
    """Polymorphic checkout function.
    
    Args:
        processor (PaymentProcessor): Any payment processor.
        amount (float): Payment amount.
    """
    print(processor.process_payment(amount))

processors = [
    CreditCardProcessor("1234567890123456"),
    PayPalProcessor("user@example.com"),
    CryptoProcessor("0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb")
]

print("\n\nPolymorphic Payment Processing:")
for processor in processors:
    checkout(processor, 99.99)


# Main execution
if __name__ == "__main__":
    print("\n=== Polymorphism Demo ===\n")
    
    # Demonstrate duck typing
    print("Duck Typing: Python doesn't check types, only methods")
    print("All three objects (Duck, Dog, Airplane) work with make_it_speak_and_fly()")
    
    # Demonstrate polymorphism benefits
    print("\nPolymorphism Benefits:")
    print("- Write functions that work with multiple types")
    print("- Add new types without changing existing code")
    print("- More flexible and maintainable code")
