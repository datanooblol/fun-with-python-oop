"""
Lesson 03: Inheritance
Demonstrates: Single inheritance, multiple inheritance, method overriding, super(), MRO
"""

# Example 1: Single Inheritance (Basic)
# Dog doesn't define __init__, so it automatically uses Animal's __init__
class Animal:
    """Base class for all animals."""
    
    def __init__(self, name: str, age: int) -> None:
        """Initialize Animal instance.
        
        Args:
            name (str): Animal's name.
            age (int): Animal's age.
        """
        self.name = name
        self.age = age
    
    def speak(self) -> str:
        """Make animal speak.
        
        Returns:
            str: Generic animal sound.
        """
        return "Some sound"
    
    def info(self) -> str:
        """Get animal info.
        
        Returns:
            str: Animal information.
        """
        return f"{self.name} is {self.age} years old"

class Dog(Animal):
    """Dog class inherits from Animal.
    
    Note: Dog doesn't define __init__, so Python automatically uses
    Animal's __init__. When you call Dog("Buddy", 3), it directly
    calls Animal.__init__(self, "Buddy", 3).
    """
    
    def speak(self) -> str:
        """Override speak method.
        
        Returns:
            str: Dog's bark.
        """
        return "Woof!"
    
    def fetch(self) -> str:
        """Dog-specific method.
        
        Returns:
            str: Fetch action.
        """
        return f"{self.name} is fetching the ball!"

dog = Dog("Buddy", 3)
print(f"{dog.info()}")  # Inherited from Animal
print(f"{dog.speak()}")  # Overridden in Dog
print(f"{dog.fetch()}")  # Dog-specific method


# Example 2: Using super() to Extend Parent Functionality
# ElectricCar DOES define __init__ with additional parameters,
# so it MUST call super().__init__() to initialize parent attributes
class Vehicle:
    """Base vehicle class."""
    
    def __init__(self, brand: str, model: str) -> None:
        """Initialize Vehicle instance.
        
        Args:
            brand (str): Vehicle brand.
            model (str): Vehicle model.
        """
        self.brand = brand
        self.model = model
    
    def start(self) -> str:
        """Start the vehicle.
        
        Returns:
            str: Start message.
        """
        return f"{self.brand} {self.model} is starting..."

class ElectricCar(Vehicle):
    """Electric car inherits from Vehicle.
    
    Note: ElectricCar defines its own __init__ because it needs an
    additional parameter (battery_capacity). When you define __init__,
    you MUST call super().__init__() to initialize parent's attributes
    (brand, model), otherwise they won't be set!
    """
    
    def __init__(self, brand: str, model: str, battery_capacity: int) -> None:
        """Initialize ElectricCar instance.
        
        Args:
            brand (str): Car brand.
            model (str): Car model.
            battery_capacity (int): Battery capacity in kWh.
        """
        super().__init__(brand, model)  # MUST call this to set brand and model
        self.battery_capacity = battery_capacity  # Then add child-specific attribute
    
    def start(self) -> str:
        """Override start method with electric-specific behavior.
        
        Returns:
            str: Electric car start message.
        """
        parent_msg = super().start()  # Call parent method
        return f"{parent_msg} (Electric mode, {self.battery_capacity}kWh battery)"

tesla = ElectricCar("Tesla", "Model 3", 75)
print(f"\n{tesla.start()}")


# Example 3: Multiple Inheritance (Diamond Problem)
class Father:
    """Father class."""
    
    def __init__(self, father_name: str) -> None:
        """Initialize Father instance.
        
        Args:
            father_name (str): Father's name.
        """
        self.father_name = father_name
    
    def skills(self) -> str:
        """Father's skills.
        
        Returns:
            str: Skills description.
        """
        return "Carpentry"
    
    def work(self) -> str:
        """Father's work.
        
        Returns:
            str: Work description.
        """
        return f"{self.father_name} is working on carpentry"

class Mother:
    """Mother class."""
    
    def __init__(self, mother_name: str) -> None:
        """Initialize Mother instance.
        
        Args:
            mother_name (str): Mother's name.
        """
        self.mother_name = mother_name
    
    def skills(self) -> str:
        """Mother's skills.
        
        Returns:
            str: Skills description.
        """
        return "Cooking"
    
    def care(self) -> str:
        """Mother's care.
        
        Returns:
            str: Care description.
        """
        return f"{self.mother_name} is caring for the family"

class Child(Father, Mother):
    """Child inherits from both Father and Mother."""
    
    def __init__(self, child_name: str, father_name: str, mother_name: str) -> None:
        """Initialize Child instance.
        
        Args:
            child_name (str): Child's name.
            father_name (str): Father's name.
            mother_name (str): Mother's name.
        """
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.child_name = child_name
    
    def show_family(self) -> str:
        """Show family information.
        
        Returns:
            str: Family info.
        """
        return f"I'm {self.child_name}, son of {self.father_name} and {self.mother_name}"

child = Child("Tommy", "John", "Mary")
print(f"\n{child.show_family()}")
print(f"Inherited skill: {child.skills()}")  # Which skills()? Father's! (MRO)
print(f"Child MRO: {[cls.__name__ for cls in Child.__mro__]}")
print("MRO order: Child -> Father -> Mother -> object")
print(f"{child.work()}")  # From Father
print(f"{child.care()}")  # From Mother


# Example 4: Method Resolution Order (MRO)
# MRO = Method Resolution Order
# When a class inherits from multiple parents, Python needs to decide
# which parent's method to call when there are conflicts.
# Python uses C3 Linearization algorithm to create a consistent order.
#
# Diamond Problem:
#       A
#      / \
#     B   C
#      \ /
#       D
# When D calls a method, should it use B's or C's version?
# MRO determines the search order: D -> B -> C -> A -> object

class A:
    """Base class A."""
    
    def method(self) -> str:
        """Method in A.
        
        Returns:
            str: Class identifier.
        """
        return "Method from A"

class B(A):
    """Class B inherits from A."""
    
    def method(self) -> str:
        """Override method in B.
        
        Returns:
            str: Class identifier.
        """
        return "Method from B"

class C(A):
    """Class C inherits from A."""
    
    def method(self) -> str:
        """Override method in C.
        
        Returns:
            str: Class identifier.
        """
        return "Method from C"

class D(B, C):
    """Class D inherits from both B and C (Diamond inheritance).
    
    MRO for D: D -> B -> C -> A -> object
    Why this order?
    1. Start with D (the class itself)
    2. Then B (first parent listed)
    3. Then C (second parent listed)
    4. Then A (common base class, visited only once)
    5. Finally object (base of all classes)
    
    When d.method() is called:
    - Check D: no method() defined
    - Check B: found method()! Return "Method from B"
    - (C and A are never checked because B already has it)
    """
    pass

d = D()
print(f"\n{d.method()}")  # Which method? Follow MRO!
print(f"MRO for D: {[cls.__name__ for cls in D.__mro__]}")
print("Explanation: D -> B -> C -> A -> object")
print("When calling d.method(), Python searches in MRO order and finds it in B first")


# Example 5: Real-world Scenario - Employee Hierarchy
class Person:
    """Base Person class."""
    
    def __init__(self, name: str, age: int) -> None:
        """Initialize Person instance.
        
        Args:
            name (str): Person's name.
            age (int): Person's age.
        """
        self.name = name
        self.age = age
    
    def introduce(self) -> str:
        """Introduce the person.
        
        Returns:
            str: Introduction.
        """
        return f"I'm {self.name}, {self.age} years old"

class Employee(Person):
    """Employee inherits from Person."""
    
    def __init__(self, name: str, age: int, employee_id: str, salary: float) -> None:
        """Initialize Employee instance.
        
        Args:
            name (str): Employee's name.
            age (int): Employee's age.
            employee_id (str): Employee ID.
            salary (float): Employee salary.
        """
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
    
    def introduce(self) -> str:
        """Override introduce with employee info.
        
        Returns:
            str: Employee introduction.
        """
        return f"{super().introduce()}, Employee ID: {self.employee_id}"
    
    def work(self) -> str:
        """Employee work method.
        
        Returns:
            str: Work description.
        """
        return f"{self.name} is working"

class Manager(Employee):
    """Manager inherits from Employee."""
    
    def __init__(self, name: str, age: int, employee_id: str, salary: float, team_size: int) -> None:
        """Initialize Manager instance.
        
        Args:
            name (str): Manager's name.
            age (int): Manager's age.
            employee_id (str): Employee ID.
            salary (float): Manager salary.
            team_size (int): Number of team members.
        """
        super().__init__(name, age, employee_id, salary)
        self.team_size = team_size
    
    def introduce(self) -> str:
        """Override introduce with manager info.
        
        Returns:
            str: Manager introduction.
        """
        return f"{super().introduce()}, Managing {self.team_size} people"
    
    def work(self) -> str:
        """Override work method.
        
        Returns:
            str: Manager work description.
        """
        return f"{self.name} is managing the team"

manager = Manager("Alice", 35, "E001", 80000, 5)
print(f"\n{manager.introduce()}")
print(f"{manager.work()}")


# Main execution
if __name__ == "__main__":
    print("\n=== Inheritance Demo ===\n")
    
    # Demonstrate isinstance and issubclass
    print("Type Checking:")
    print(f"dog is instance of Dog: {isinstance(dog, Dog)}")
    print(f"dog is instance of Animal: {isinstance(dog, Animal)}")
    print(f"Dog is subclass of Animal: {issubclass(Dog, Animal)}")
    
    # Demonstrate MRO in detail
    print(f"\nChild class MRO: {[cls.__name__ for cls in Child.__mro__]}")
    print("MRO order: Child -> Father -> Mother -> object")
    print("When calling child.skills(), Python searches in this order")
    
    # Demonstrate multiple inheritance attribute access
    print(f"\nMultiple Inheritance Attributes:")
    print(f"child.father_name: {child.father_name}")
    print(f"child.mother_name: {child.mother_name}")
    print(f"child.child_name: {child.child_name}")
