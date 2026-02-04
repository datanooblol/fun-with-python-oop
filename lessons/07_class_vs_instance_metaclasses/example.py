"""
Lesson 07: Metaclasses
Understanding what creates classes and how to customize class creation.
"""


# ============================================================================
# Example 1: Everything is an Object (Even Classes!)
# ============================================================================

class Dog:
    """A simple Dog class."""
    
    def bark(self) -> None:
        """Make the dog bark."""
        print("Woof!")


def example_1_classes_are_objects() -> None:
    """Demonstrate that classes themselves are objects.
    
    Returns:
        None
    """
    print("=== Example 1: Classes Are Objects ===")
    
    # Create an instance
    my_dog = Dog()
    print(f"my_dog is an instance of: {type(my_dog)}")  # <class 'Dog'>
    
    # But what is Dog itself?
    print(f"Dog is an instance of: {type(Dog)}")  # <class 'type'>
    
    # type is the metaclass that creates classes!
    print(f"type is an instance of: {type(type)}")  # <class 'type'>
    print()


# ============================================================================
# Example 2: Creating Classes Dynamically with type()
# ============================================================================

def example_2_type_creates_classes() -> None:
    """Show how type() can create classes dynamically.
    
    Returns:
        None
    """
    print("=== Example 2: type() Creates Classes ===")
    
    # Normal way to create a class
    class Cat:
        def meow(self) -> None:
            print("Meow!")
    
    # Dynamic way using type(name, bases, dict)
    def meow_method(self) -> None:
        print("Meow!")
    
    DynamicCat = type('DynamicCat', (), {'meow': meow_method})
    
    # Both work the same!
    cat1 = Cat()
    cat2 = DynamicCat()
    
    cat1.meow()  # Meow!
    cat2.meow()  # Meow!
    
    print(f"Cat created by: {type(Cat)}")  # <class 'type'>
    print(f"DynamicCat created by: {type(DynamicCat)}")  # <class 'type'>
    print()


# ============================================================================
# Example 3: Custom Metaclass - Basic Structure
# ============================================================================

class SimpleMeta(type):
    """A simple metaclass that prints when a class is created.
    
    Metaclasses inherit from type and control class creation.
    """
    
    def __new__(mcs, name: str, bases: tuple, attrs: dict) -> type:
        """Create a new class.
        
        Args:
            mcs (type): The metaclass itself (like 'cls' in regular classes).
            name (str): Name of the class being created.
            bases (tuple): Tuple of base classes.
            attrs (dict): Dictionary of class attributes and methods.
            
        Returns:
            type: The newly created class.
        """
        print(f"Creating class: {name}")
        return super().__new__(mcs, name, bases, attrs)


class MyClass(metaclass=SimpleMeta):
    """A class using SimpleMeta as its metaclass."""
    pass


def example_3_custom_metaclass() -> None:
    """Demonstrate basic custom metaclass.
    
    Returns:
        None
    """
    print("=== Example 3: Custom Metaclass ===")
    # "Creating class: MyClass" was already printed when class was defined!
    
    obj = MyClass()
    print(f"MyClass is an instance of: {type(MyClass)}")  # <class 'SimpleMeta'>
    print(f"obj is an instance of: {type(obj)}")  # <class 'MyClass'>
    print()


# ============================================================================
# Example 4: Practical Use - Auto-Register Classes
# ============================================================================

class RegistryMeta(type):
    """Metaclass that automatically registers all classes in a registry.
    
    Useful for plugin systems, factories, etc.
    """
    
    registry: dict[str, type] = {}
    
    def __new__(mcs, name: str, bases: tuple, attrs: dict) -> type:
        """Create class and register it.
        
        Args:
            mcs (type): The metaclass.
            name (str): Class name.
            bases (tuple): Base classes.
            attrs (dict): Class attributes.
            
        Returns:
            type: The created class.
        """
        cls = super().__new__(mcs, name, bases, attrs)
        
        # Don't register the base class itself
        if name != 'Plugin':
            mcs.registry[name] = cls
        
        return cls


class Plugin(metaclass=RegistryMeta):
    """Base class for all plugins."""
    
    def execute(self) -> None:
        """Execute the plugin."""
        pass


class EmailPlugin(Plugin):
    """Plugin for sending emails."""
    
    def execute(self) -> None:
        """Send an email."""
        print("Sending email...")


class SMSPlugin(Plugin):
    """Plugin for sending SMS."""
    
    def execute(self) -> None:
        """Send an SMS."""
        print("Sending SMS...")


class LogPlugin(Plugin):
    """Plugin for logging."""
    
    def execute(self) -> None:
        """Write to log."""
        print("Writing to log...")


def example_4_registry_pattern() -> None:
    """Demonstrate auto-registration with metaclass.
    
    Returns:
        None
    """
    print("=== Example 4: Auto-Registry Pattern ===")
    
    # All plugins are automatically registered!
    print(f"Registered plugins: {list(RegistryMeta.registry.keys())}")
    
    # Execute all plugins dynamically
    for name, plugin_class in RegistryMeta.registry.items():
        print(f"Running {name}:")
        plugin = plugin_class()
        plugin.execute()
    print()


# ============================================================================
# Example 5: Practical Use - Enforce Rules on Classes
# ============================================================================

class StrictMeta(type):
    """Metaclass that enforces rules on class definitions.
    
    Ensures all methods have docstrings.
    """
    
    def __new__(mcs, name: str, bases: tuple, attrs: dict) -> type:
        """Create class and validate it follows rules.
        
        Args:
            mcs (type): The metaclass.
            name (str): Class name.
            bases (tuple): Base classes.
            attrs (dict): Class attributes.
            
        Returns:
            type: The created class.
            
        Raises:
            TypeError: If a method lacks a docstring.
        """
        # Check all methods have docstrings
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('_'):
                if not attr_value.__doc__:
                    raise TypeError(
                        f"Method '{attr_name}' in class '{name}' must have a docstring"
                    )
        
        return super().__new__(mcs, name, bases, attrs)


class GoodClass(metaclass=StrictMeta):
    """A class that follows the rules."""
    
    def process(self) -> None:
        """Process data."""
        print("Processing...")


# This would raise TypeError at class definition time:
# class BadClass(metaclass=StrictMeta):
#     def process(self):  # No docstring!
#         print("Processing...")


def example_5_enforce_rules() -> None:
    """Demonstrate enforcing rules with metaclass.
    
    Returns:
        None
    """
    print("=== Example 5: Enforce Rules ===")
    
    obj = GoodClass()
    obj.process()
    
    print("GoodClass passed all validation rules!")
    print("(Uncomment BadClass to see validation error)")
    print()


# ============================================================================
# Example 6: Singleton Pattern with Metaclass
# ============================================================================

class SingletonMeta(type):
    """Metaclass that ensures only one instance of a class exists.
    
    Classic Singleton pattern implementation.
    """
    
    _instances: dict[type, object] = {}
    
    def __call__(cls, *args, **kwargs) -> object:
        """Control instance creation.
        
        Args:
            cls (type): The class being instantiated.
            *args: Positional arguments.
            **kwargs: Keyword arguments.
            
        Returns:
            object: The single instance of the class.
        """
        if cls not in cls._instances:
            # Create instance only if it doesn't exist
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    """Database connection (only one should exist)."""
    
    def __init__(self) -> None:
        """Initialize database connection."""
        print("Connecting to database...")
        self.connection = "DB_CONNECTION_OBJECT"
    
    def query(self, sql: str) -> None:
        """Execute a query.
        
        Args:
            sql (str): SQL query string.
            
        Returns:
            None
        """
        print(f"Executing: {sql}")


def example_6_singleton_pattern() -> None:
    """Demonstrate Singleton pattern with metaclass.
    
    Returns:
        None
    """
    print("=== Example 6: Singleton Pattern ===")
    
    db1 = Database()  # Connects to database
    db2 = Database()  # Reuses existing connection
    db3 = Database()  # Reuses existing connection
    
    print(f"db1 is db2: {db1 is db2}")  # True
    print(f"db2 is db3: {db2 is db3}")  # True
    print(f"All are the same object: {id(db1) == id(db2) == id(db3)}")
    print()


# ============================================================================
# Run All Examples
# ============================================================================

if __name__ == "__main__":
    example_1_classes_are_objects()
    example_2_type_creates_classes()
    example_3_custom_metaclass()
    example_4_registry_pattern()
    example_5_enforce_rules()
    example_6_singleton_pattern()
    
    print("=" * 60)
    print("Key Takeaway: Metaclasses control HOW classes are created.")
    print("Use them when you need to modify class behavior at creation time.")
    print("=" * 60)
