"""
Lesson 01: Classes and Objects
Demonstrates: Basic class definition, object instantiation, attributes, and methods
"""

# Example 1: Basic Class Definition
class Dog:
    """A simple Dog class."""
    
    def bark(self) -> str:
        """Make the dog bark.
        
        Returns:
            str: The bark sound.
        """
        return "Woof!"

dog1 = Dog()
print(f"Dog says: {dog1.bark()}")


# Example 2: Constructor and Instance Attributes
class Person:
    """Represents a person with name and age."""
    
    def __init__(self, name: str, age: int) -> None:
        """Initialize a Person instance.
        
        Args:
            name (str): The person's name.
            age (int): The person's age.
        """
        self.name = name
        self.age = age
    
    def introduce(self) -> str:
        """Introduce the person.
        
        Returns:
            str: Introduction message.
        """
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
print(person1.introduce())
print(person2.introduce())


# Example 3: Class Attributes vs Instance Attributes
class BankAccount:
    """Bank account with class and instance attributes."""
    
    bank_name: str = "PyBank"  # Class attribute (shared by all instances)
    total_accounts: int = 0     # Class attribute
    
    def __init__(self, owner: str, balance: float = 0) -> None:
        """Initialize a BankAccount instance.
        
        Args:
            owner (str): Account owner's name.
            balance (float): Initial balance. Defaults to 0.
        """
        self.owner = owner          # Instance attribute (unique to each instance)
        self.balance = balance      # Instance attribute
        BankAccount.total_accounts += 1
    
    def deposit(self, amount: float) -> str:
        """Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit.
            
        Returns:
            str: Transaction message.
        """
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount: float) -> str:
        """Withdraw money from the account.
        
        Args:
            amount (float): Amount to withdraw.
            
        Returns:
            str: Transaction message or error.
        """
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.balance}"

acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

print(f"\nBank: {BankAccount.bank_name}")
print(f"Total accounts: {BankAccount.total_accounts}")
print(acc1.deposit(200))
print(acc2.withdraw(100))


# Example 4: Real-world Scenario - Product Inventory
class Product:
    """Product inventory management system."""
    
    def __init__(self, name: str, price: float, stock: int) -> None:
        """Initialize a Product instance.
        
        Args:
            name (str): Product name.
            price (float): Product price.
            stock (int): Initial stock quantity.
        """
        self.name = name
        self.price = price
        self.stock = stock
    
    def sell(self, quantity: int) -> str:
        """Sell product units.
        
        Args:
            quantity (int): Number of units to sell.
            
        Returns:
            str: Sale confirmation or error message.
        """
        if quantity > self.stock:
            return f"Only {self.stock} units available"
        self.stock -= quantity
        total = self.price * quantity
        return f"Sold {quantity} {self.name}(s) for ${total}. Stock left: {self.stock}"
    
    def restock(self, quantity: int) -> str:
        """Restock product units.
        
        Args:
            quantity (int): Number of units to add.
            
        Returns:
            str: Restock confirmation.
        """
        self.stock += quantity
        return f"Restocked {quantity} units. Total stock: {self.stock}"

laptop = Product("Laptop", 999, 10)
phone = Product("Phone", 699, 25)

print(f"\n{laptop.sell(3)}")
print(laptop.restock(5))
print(phone.sell(30))


# Main execution
if __name__ == "__main__":
    print("\n=== Classes and Objects Demo ===\n")
    
    # Demonstrate object identity
    print("Object Identity:")
    print(f"person1 is person2: {person1 is person2}")
    print(f"person1 id: {id(person1)}")
    print(f"person2 id: {id(person2)}")
    
    # Demonstrate class vs instance attributes
    print(f"\nClass attribute access:")
    print(f"acc1.bank_name: {acc1.bank_name}")
    print(f"acc2.bank_name: {acc2.bank_name}")
    print(f"BankAccount.bank_name: {BankAccount.bank_name}")
