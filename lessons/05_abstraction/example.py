"""
Lesson 05: Abstraction
Demonstrates: Abstract base classes, abstract methods, enforcing implementation contracts
"""

from abc import ABC, abstractmethod

# Example 1: Basic Abstract Base Class
# ABC = Abstract Base Class - cannot be instantiated directly
class Animal(ABC):
    """Abstract animal class - defines contract for all animals."""
    
    def __init__(self, name: str, age: int) -> None:
        """Initialize Animal instance.
        
        Args:
            name (str): Animal's name.
            age (int): Animal's age.
        """
        self.name = name
        self.age = age
    
    @abstractmethod
    def speak(self) -> str:
        """Abstract method - must be implemented by subclasses.
        
        Returns:
            str: Animal sound.
        """
        pass
    
    @abstractmethod
    def move(self) -> str:
        """Abstract method - must be implemented by subclasses.
        
        Returns:
            str: Movement description.
        """
        pass
    
    def info(self) -> str:
        """Concrete method - can be used by all subclasses.
        
        Returns:
            str: Animal information.
        """
        return f"{self.name} is {self.age} years old"

class Dog(Animal):
    """Dog class - must implement all abstract methods."""
    
    def speak(self) -> str:
        """Implement speak method.
        
        Returns:
            str: Dog sound.
        """
        return "Woof!"
    
    def move(self) -> str:
        """Implement move method.
        
        Returns:
            str: Movement description.
        """
        return f"{self.name} is running on four legs"

class Bird(Animal):
    """Bird class - must implement all abstract methods."""
    
    def speak(self) -> str:
        """Implement speak method.
        
        Returns:
            str: Bird sound.
        """
        return "Chirp!"
    
    def move(self) -> str:
        """Implement move method.
        
        Returns:
            str: Movement description.
        """
        return f"{self.name} is flying"

# Cannot instantiate abstract class
# animal = Animal("Generic", 5)  # TypeError: Can't instantiate abstract class

dog = Dog("Buddy", 3)
bird = Bird("Tweety", 1)

print("Abstract Base Class Demo:")
print(f"{dog.info()}: {dog.speak()}, {dog.move()}")
print(f"{bird.info()}: {bird.speak()}, {bird.move()}")


# Example 2: Abstract Properties
class Shape(ABC):
    """Abstract shape class with abstract properties."""
    
    @property
    @abstractmethod
    def area(self) -> float:
        """Abstract property - must be implemented.
        
        Returns:
            float: Shape area.
        """
        pass
    
    @property
    @abstractmethod
    def perimeter(self) -> float:
        """Abstract property - must be implemented.
        
        Returns:
            float: Shape perimeter.
        """
        pass
    
    def describe(self) -> str:
        """Concrete method using abstract properties.
        
        Returns:
            str: Shape description.
        """
        return f"{self.__class__.__name__}: Area={self.area:.2f}, Perimeter={self.perimeter:.2f}"

class Rectangle(Shape):
    """Rectangle implementation."""
    
    def __init__(self, width: float, height: float) -> None:
        """Initialize Rectangle.
        
        Args:
            width (float): Rectangle width.
            height (float): Rectangle height.
        """
        self._width = width
        self._height = height
    
    @property
    def area(self) -> float:
        """Calculate rectangle area.
        
        Returns:
            float: Area value.
        """
        return self._width * self._height
    
    @property
    def perimeter(self) -> float:
        """Calculate rectangle perimeter.
        
        Returns:
            float: Perimeter value.
        """
        return 2 * (self._width + self._height)

class Circle(Shape):
    """Circle implementation."""
    
    def __init__(self, radius: float) -> None:
        """Initialize Circle.
        
        Args:
            radius (float): Circle radius.
        """
        self._radius = radius
    
    @property
    def area(self) -> float:
        """Calculate circle area.
        
        Returns:
            float: Area value.
        """
        return 3.14159 * self._radius ** 2
    
    @property
    def perimeter(self) -> float:
        """Calculate circle circumference.
        
        Returns:
            float: Circumference value.
        """
        return 2 * 3.14159 * self._radius

shapes = [Rectangle(5, 3), Circle(4)]
print("\n\nAbstract Properties Demo:")
for shape in shapes:
    print(shape.describe())


# Example 3: Multiple Abstract Methods - Payment Gateway Contract
class PaymentGateway(ABC):
    """Abstract payment gateway - enforces implementation contract."""
    
    @abstractmethod
    def authenticate(self, credentials: dict) -> bool:
        """Authenticate with payment provider.
        
        Args:
            credentials (dict): Authentication credentials.
            
        Returns:
            bool: True if authenticated, False otherwise.
        """
        pass
    
    @abstractmethod
    def process_payment(self, amount: float, card_info: dict) -> dict:
        """Process payment transaction.
        
        Args:
            amount (float): Payment amount.
            card_info (dict): Card information.
            
        Returns:
            dict: Transaction result.
        """
        pass
    
    @abstractmethod
    def refund(self, transaction_id: str, amount: float) -> dict:
        """Process refund.
        
        Args:
            transaction_id (str): Original transaction ID.
            amount (float): Refund amount.
            
        Returns:
            dict: Refund result.
        """
        pass
    
    def log_transaction(self, transaction: dict) -> None:
        """Concrete method - common logging functionality.
        
        Args:
            transaction (dict): Transaction details.
        """
        print(f"[LOG] Transaction: {transaction}")

class StripeGateway(PaymentGateway):
    """Stripe payment gateway implementation."""
    
    def authenticate(self, credentials: dict) -> bool:
        """Authenticate with Stripe.
        
        Args:
            credentials (dict): Stripe API credentials.
            
        Returns:
            bool: Authentication result.
        """
        print(f"Authenticating with Stripe using key: {credentials.get('api_key', 'N/A')}")
        return True
    
    def process_payment(self, amount: float, card_info: dict) -> dict:
        """Process payment via Stripe.
        
        Args:
            amount (float): Payment amount.
            card_info (dict): Card information.
            
        Returns:
            dict: Transaction result.
        """
        result = {
            "status": "success",
            "transaction_id": "stripe_12345",
            "amount": amount,
            "provider": "Stripe"
        }
        self.log_transaction(result)
        return result
    
    def refund(self, transaction_id: str, amount: float) -> dict:
        """Process refund via Stripe.
        
        Args:
            transaction_id (str): Transaction ID.
            amount (float): Refund amount.
            
        Returns:
            dict: Refund result.
        """
        return {
            "status": "refunded",
            "transaction_id": transaction_id,
            "amount": amount
        }

class PayPalGateway(PaymentGateway):
    """PayPal payment gateway implementation."""
    
    def authenticate(self, credentials: dict) -> bool:
        """Authenticate with PayPal.
        
        Args:
            credentials (dict): PayPal credentials.
            
        Returns:
            bool: Authentication result.
        """
        print(f"Authenticating with PayPal using email: {credentials.get('email', 'N/A')}")
        return True
    
    def process_payment(self, amount: float, card_info: dict) -> dict:
        """Process payment via PayPal.
        
        Args:
            amount (float): Payment amount.
            card_info (dict): Card information.
            
        Returns:
            dict: Transaction result.
        """
        result = {
            "status": "success",
            "transaction_id": "paypal_67890",
            "amount": amount,
            "provider": "PayPal"
        }
        self.log_transaction(result)
        return result
    
    def refund(self, transaction_id: str, amount: float) -> dict:
        """Process refund via PayPal.
        
        Args:
            transaction_id (str): Transaction ID.
            amount (float): Refund amount.
            
        Returns:
            dict: Refund result.
        """
        return {
            "status": "refunded",
            "transaction_id": transaction_id,
            "amount": amount
        }

stripe = StripeGateway()
paypal = PayPalGateway()

print("\n\nPayment Gateway Contract Demo:")
stripe.authenticate({"api_key": "sk_test_123"})
stripe.process_payment(99.99, {"card": "4242"})

paypal.authenticate({"email": "user@example.com"})
paypal.process_payment(49.99, {"card": "5555"})


# Example 4: Abstract Class with Partial Implementation
class DatabaseConnection(ABC):
    """Abstract database connection with some concrete methods."""
    
    def __init__(self, host: str, port: int) -> None:
        """Initialize database connection.
        
        Args:
            host (str): Database host.
            port (int): Database port.
        """
        self.host = host
        self.port = port
        self.connected = False
    
    @abstractmethod
    def connect(self) -> bool:
        """Connect to database - must be implemented.
        
        Returns:
            bool: Connection status.
        """
        pass
    
    @abstractmethod
    def disconnect(self) -> None:
        """Disconnect from database - must be implemented."""
        pass
    
    @abstractmethod
    def execute_query(self, query: str) -> list:
        """Execute database query - must be implemented.
        
        Args:
            query (str): SQL query.
            
        Returns:
            list: Query results.
        """
        pass
    
    def get_connection_string(self) -> str:
        """Concrete method - build connection string.
        
        Returns:
            str: Connection string.
        """
        return f"{self.host}:{self.port}"
    
    def is_connected(self) -> bool:
        """Concrete method - check connection status.
        
        Returns:
            bool: Connection status.
        """
        return self.connected

class MySQLConnection(DatabaseConnection):
    """MySQL database connection implementation."""
    
    def connect(self) -> bool:
        """Connect to MySQL database.
        
        Returns:
            bool: Connection status.
        """
        print(f"Connecting to MySQL at {self.get_connection_string()}")
        self.connected = True
        return True
    
    def disconnect(self) -> None:
        """Disconnect from MySQL database."""
        print("Disconnecting from MySQL")
        self.connected = False
    
    def execute_query(self, query: str) -> list:
        """Execute MySQL query.
        
        Args:
            query (str): SQL query.
            
        Returns:
            list: Query results.
        """
        print(f"Executing MySQL query: {query}")
        return [{"id": 1, "name": "Result"}]

class PostgreSQLConnection(DatabaseConnection):
    """PostgreSQL database connection implementation."""
    
    def connect(self) -> bool:
        """Connect to PostgreSQL database.
        
        Returns:
            bool: Connection status.
        """
        print(f"Connecting to PostgreSQL at {self.get_connection_string()}")
        self.connected = True
        return True
    
    def disconnect(self) -> None:
        """Disconnect from PostgreSQL database."""
        print("Disconnecting from PostgreSQL")
        self.connected = False
    
    def execute_query(self, query: str) -> list:
        """Execute PostgreSQL query.
        
        Args:
            query (str): SQL query.
            
        Returns:
            list: Query results.
        """
        print(f"Executing PostgreSQL query: {query}")
        return [{"id": 1, "name": "Result"}]

mysql = MySQLConnection("localhost", 3306)
postgres = PostgreSQLConnection("localhost", 5432)

print("\n\nDatabase Connection Contract Demo:")
mysql.connect()
mysql.execute_query("SELECT * FROM users")
print(f"MySQL connected: {mysql.is_connected()}")
mysql.disconnect()

postgres.connect()
postgres.execute_query("SELECT * FROM users")
postgres.disconnect()


# Example 5: Real-world Scenario - Data Serializer Contract
class DataSerializer(ABC):
    """Abstract data serializer - enforces serialization contract."""
    
    @abstractmethod
    def serialize(self, data: dict) -> str:
        """Serialize data to string format.
        
        Args:
            data (dict): Data to serialize.
            
        Returns:
            str: Serialized data.
        """
        pass
    
    @abstractmethod
    def deserialize(self, data_string: str) -> dict:
        """Deserialize string to data.
        
        Args:
            data_string (str): Serialized data.
            
        Returns:
            dict: Deserialized data.
        """
        pass
    
    def validate_data(self, data: dict) -> bool:
        """Concrete method - validate data structure.
        
        Args:
            data (dict): Data to validate.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        return isinstance(data, dict) and len(data) > 0

class JSONSerializer(DataSerializer):
    """JSON serializer implementation."""
    
    def serialize(self, data: dict) -> str:
        """Serialize to JSON.
        
        Args:
            data (dict): Data to serialize.
            
        Returns:
            str: JSON string.
        """
        import json
        return json.dumps(data)
    
    def deserialize(self, data_string: str) -> dict:
        """Deserialize from JSON.
        
        Args:
            data_string (str): JSON string.
            
        Returns:
            dict: Deserialized data.
        """
        import json
        return json.loads(data_string)

class XMLSerializer(DataSerializer):
    """XML serializer implementation."""
    
    def serialize(self, data: dict) -> str:
        """Serialize to XML.
        
        Args:
            data (dict): Data to serialize.
            
        Returns:
            str: XML string.
        """
        xml = "<data>"
        for key, value in data.items():
            xml += f"<{key}>{value}</{key}>"
        xml += "</data>"
        return xml
    
    def deserialize(self, data_string: str) -> dict:
        """Deserialize from XML (simplified).
        
        Args:
            data_string (str): XML string.
            
        Returns:
            dict: Deserialized data.
        """
        # Simplified XML parsing for demonstration
        return {"parsed": "from XML"}

json_serializer = JSONSerializer()
xml_serializer = XMLSerializer()

data = {"name": "Alice", "age": 30}

print("\n\nData Serializer Contract Demo:")
json_str = json_serializer.serialize(data)
print(f"JSON: {json_str}")
print(f"Deserialized: {json_serializer.deserialize(json_str)}")

xml_str = xml_serializer.serialize(data)
print(f"XML: {xml_str}")


# Main execution
if __name__ == "__main__":
    print("\n=== Abstraction Demo ===\n")
    
    # Demonstrate that abstract classes cannot be instantiated
    print("Abstract Class Enforcement:")
    try:
        animal = Animal("Generic", 5)
    except TypeError as e:
        print(f"Cannot instantiate abstract class: {e}")
    
    # Demonstrate incomplete implementation
    print("\nIncomplete Implementation:")
    print("If a subclass doesn't implement all abstract methods,")
    print("Python raises TypeError when trying to instantiate it")
    
    # Demonstrate @abstractmethod vs NotImplementedError
    print("\n@abstractmethod vs NotImplementedError:")
    print("\nOption 1: @abstractmethod with pass")
    print("  - Error at INSTANTIATION time")
    print("  - Cannot create object at all")
    print("  - Better: Fail fast!")
    
    print("\nOption 2: NotImplementedError without @abstractmethod")
    print("  - Error at RUNTIME (when method is called)")
    print("  - Object created successfully")
    print("  - Worse: Error happens later")
    
    # Example of NotImplementedError approach (not recommended)
    class OldStyleBase:
        """Old-style base class without ABC."""
        def speak(self) -> str:
            raise NotImplementedError("Subclass must implement speak()")
    
    class IncompleteChild(OldStyleBase):
        """Child that forgets to implement speak."""
        pass
    
    print("\nDemonstration:")
    try:
        # This succeeds! Object is created
        obj = IncompleteChild()
        print("IncompleteChild object created successfully (BAD!)")
        # Error only happens when we call the method
        obj.speak()
    except NotImplementedError as e:
        print(f"Error at runtime: {e}")
    
    print("\nWith @abstractmethod, the object wouldn't be created at all!")
    
    # Show the contract benefit
    print("\nContract Benefits:")
    print("- Ensures all subclasses implement required methods")
    print("- Provides clear interface for developers")
    print("- Catches missing implementations at instantiation time")
    print("- Enables polymorphism with guaranteed interface")
