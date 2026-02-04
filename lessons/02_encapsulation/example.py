"""
Lesson 02: Encapsulation
Demonstrates: Private/protected attributes, properties, getters/setters, data hiding
"""

# Example 1: Public vs Private Attributes
# Name Mangling Pattern: instance._<ClassName>__<private_attr>
# When you write: self.__pin = "1234"
# Python stores it as: self._BankAccount__pin
class BankAccount:
    """Bank account demonstrating attribute access levels."""
    
    def __init__(self, owner: str, balance: float) -> None:
        """Initialize a BankAccount instance.
        
        Args:
            owner (str): Account owner's name.
            balance (float): Initial balance.
        """
        self.owner = owner              # Public: accessible anywhere
        self._account_number = "12345"  # Protected: convention only (not enforced)
        self.__pin = "1234"             # Private: name mangled to _BankAccount__pin
    
    def verify_pin(self, pin: str) -> bool:
        """Verify the PIN.
        
        Args:
            pin (str): PIN to verify.
            
        Returns:
            bool: True if PIN matches, False otherwise.
        """
        return self.__pin == pin

account = BankAccount("Alice", 1000)
print(f"Owner (public): {account.owner}")
print(f"Account number (protected): {account._account_number}")
# print(account.__pin)  # AttributeError: 'BankAccount' object has no attribute '__pin'
print(f"PIN verification: {account.verify_pin('1234')}")


# Example 2: Property Decorators (Pythonic Getters/Setters)
class Temperature:
    """Temperature class with validation using properties."""
    
    def __init__(self, celsius: float) -> None:
        """Initialize Temperature instance.
        
        Args:
            celsius (float): Temperature in Celsius.
        """
        self._celsius = celsius
    
    @property
    def celsius(self) -> float:
        """Get temperature in Celsius.
        
        Returns:
            float: Temperature in Celsius.
        """
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float) -> None:
        """Set temperature in Celsius with validation.
        
        Args:
            value (float): Temperature in Celsius.
            
        Raises:
            ValueError: If temperature is below absolute zero.
        """
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        """Get temperature in Fahrenheit.
        
        Returns:
            float: Temperature in Fahrenheit.
        """
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        """Set temperature using Fahrenheit.
        
        Args:
            value (float): Temperature in Fahrenheit.
        """
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"\n{temp.celsius}°C = {temp.fahrenheit}°F")
temp.fahrenheit = 100
print(f"After setting to 100°F: {temp.celsius}°C")


# Example 3: Read-only Properties
class Circle:
    """Circle with read-only computed properties."""
    
    def __init__(self, radius: float) -> None:
        """Initialize Circle instance.
        
        Args:
            radius (float): Circle radius.
        """
        self._radius = radius
    
    @property
    def radius(self) -> float:
        """Get circle radius.
        
        Returns:
            float: Circle radius.
        """
        return self._radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        """Set circle radius with validation.
        
        Args:
            value (float): New radius value.
            
        Raises:
            ValueError: If radius is negative.
        """
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self) -> float:
        """Calculate circle area (read-only).
        
        Returns:
            float: Circle area.
        """
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self) -> float:
        """Calculate circle circumference (read-only).
        
        Returns:
            float: Circle circumference.
        """
        return 2 * 3.14159 * self._radius

circle = Circle(5)
print(f"\nRadius: {circle.radius}")
print(f"Area: {circle.area}")
print(f"Circumference: {circle.circumference}")
circle.radius = 10
print(f"After radius change - Area: {circle.area}")


# Example 4: Real-world Scenario - User Account with Validation
class User:
    """User account with encapsulated data and validation."""
    
    def __init__(self, username: str, email: str, age: int) -> None:
        """Initialize User instance.
        
        Args:
            username (str): User's username.
            email (str): User's email address.
            age (int): User's age.
        """
        self._username = username
        self._email = email
        self._age = age
        self.__password_hash = None  # Private, never exposed directly
    
    @property
    def username(self) -> str:
        """Get username.
        
        Returns:
            str: Username.
        """
        return self._username
    
    @property
    def email(self) -> str:
        """Get email.
        
        Returns:
            str: Email address.
        """
        return self._email
    
    @email.setter
    def email(self, value: str) -> None:
        """Set email with validation.
        
        Args:
            value (str): New email address.
            
        Raises:
            ValueError: If email format is invalid.
        """
        if "@" not in value:
            raise ValueError("Invalid email format")
        self._email = value
    
    @property
    def age(self) -> int:
        """Get age.
        
        Returns:
            int: User's age.
        """
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        """Set age with validation.
        
        Args:
            value (int): New age value.
            
        Raises:
            ValueError: If age is invalid.
        """
        if value < 0 or value > 150:
            raise ValueError("Invalid age")
        self._age = value
    
    def set_password(self, password: str) -> None:
        """Set password (stores hash, not actual password).
        
        Args:
            password (str): Password to set.
        """
        self.__password_hash = hash(password)
        print("Password set successfully")
    
    def check_password(self, password: str) -> bool:
        """Check if password matches.
        
        Args:
            password (str): Password to check.
            
        Returns:
            bool: True if password matches, False otherwise.
        """
        return self.__password_hash == hash(password)

user = User("alice123", "alice@example.com", 25)
print(f"\nUser: {user.username}, Email: {user.email}, Age: {user.age}")
user.set_password("secret123")
print(f"Password check: {user.check_password('secret123')}")
user.email = "newemail@example.com"
print(f"Updated email: {user.email}")


# Example 5: Public, Protected, and Private Methods
# Method Naming Pattern: same as attributes
# public_method() - accessible anywhere
# _protected_method() - convention: internal use
# __private_method() - name mangled to _ClassName__private_method()
class PaymentProcessor:
    """Payment processor demonstrating method access levels."""
    
    def __init__(self, merchant_id: str) -> None:
        """Initialize PaymentProcessor.
        
        Args:
            merchant_id (str): Merchant identifier.
        """
        self.merchant_id = merchant_id
        self._transaction_count = 0
    
    def process_payment(self, amount: float, card_number: str) -> str:
        """Public method: Process a payment (accessible from anywhere).
        
        Args:
            amount (float): Payment amount.
            card_number (str): Credit card number.
            
        Returns:
            str: Transaction result.
        """
        if self._validate_card(card_number):
            self.__log_transaction(amount)
            return f"Payment of ${amount} processed successfully"
        return "Payment failed: Invalid card"
    
    def _validate_card(self, card_number: str) -> bool:
        """Protected method: Validate card (convention: internal use).
        
        Args:
            card_number (str): Credit card number.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        # Simple validation: check if 16 digits
        return len(card_number) == 16 and card_number.isdigit()
    
    def __log_transaction(self, amount: float) -> None:
        """Private method: Log transaction (name mangled).
        
        Args:
            amount (float): Transaction amount.
        """
        self._transaction_count += 1
        print(f"[INTERNAL LOG] Transaction #{self._transaction_count}: ${amount}")
    
    def get_transaction_count(self) -> int:
        """Public method: Get transaction count.
        
        Returns:
            int: Number of transactions.
        """
        return self._transaction_count

processor = PaymentProcessor("MERCH123")
print(f"\n{processor.process_payment(100.50, '1234567812345678')}")
print(f"Transaction count: {processor.get_transaction_count()}")

# Can call protected method (but shouldn't - it's a convention)
print(f"\nCalling _validate_card (not recommended): {processor._validate_card('1234567812345678')}")

# Cannot call private method directly
print("Trying to call __log_transaction: ", end="")
try:
    processor.__log_transaction(50.0)
except AttributeError as e:
    print(f"AttributeError")

# But can access via name mangling (not recommended)
print("Calling via mangled name _PaymentProcessor__log_transaction:")
processor._PaymentProcessor__log_transaction(50.0)


# Main execution
if __name__ == "__main__":
    print("\n=== Encapsulation Demo ===\n")
    
    # Demonstrate name mangling in detail
    print("Name Mangling Explained:")
    print("Pattern: instance._<ClassName>__<private_attr>")
    print(f"Example: account._BankAccount__pin\n")
    
    print(f"Trying account.__pin: ", end="")
    try:
        print(account.__pin)
    except AttributeError as e:
        print(f"AttributeError - {e}")
    
    print(f"\nPython internally renames __pin to: _BankAccount__pin")
    print(f"Accessing via mangled name: {account._BankAccount__pin}")
    print(f"\nKey Point: This is NOT true privacy - just name mangling!")
    print(f"Purpose: Avoid accidental name conflicts in subclasses")
    print(f"Python philosophy: 'We are all consenting adults here'")
    
    # Show all attributes
    print(f"\nAll attributes: {[attr for attr in dir(account) if not attr.startswith('__')]}")
    
    # Demonstrate property benefits
    print("\nProperty Benefits:")
    try:
        temp.celsius = -300  # Will raise ValueError
    except ValueError as e:
        print(f"Validation works: {e}")
