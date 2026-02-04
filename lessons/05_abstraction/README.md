# Lesson 05: Abstraction

## 📚 Concept

Abstraction is the practice of hiding implementation details and exposing only essential features through a contract (interface). In Python, abstraction is implemented using Abstract Base Classes (ABC) with the `@abstractmethod` decorator. Abstract classes cannot be instantiated directly and force subclasses to implement specific methods, ensuring all implementations follow the same contract. This guarantees that polymorphic code can safely call methods knowing they exist in all subclasses.

## 🎯 Key Points

- **Abstract Base Class (ABC)**: A class that cannot be instantiated directly
- **@abstractmethod**: Decorator that forces subclasses to implement the method
- **Contract enforcement**: Python raises `TypeError` at instantiation if abstract methods aren't implemented
- **Fail fast**: Errors caught when creating objects, not when calling methods
- **Mixed implementation**: Abstract classes can have both abstract and concrete methods
- **Abstract properties**: Use `@property` with `@abstractmethod` for required properties
- **Best practice**: Use `pass` in abstract method body, not `raise NotImplementedError`

## 💡 When to Use

- **Plugin architecture**: Define a `Plugin` ABC that all plugins must implement with `load()`, `execute()`, `unload()` methods
- **Database drivers**: Create `DatabaseConnection` ABC ensuring all drivers implement `connect()`, `disconnect()`, `execute_query()`
- **Payment gateways**: Define `PaymentProcessor` ABC requiring `authenticate()`, `process_payment()`, `refund()` methods
- **Data serializers**: Build `Serializer` ABC forcing implementations to provide `serialize()` and `deserialize()` methods

## 🔍 Example Overview

The `example.py` demonstrates abstraction techniques:

- **Example 1**: Basic ABC - Animal with abstract `speak()` and `move()` methods
- **Example 2**: Abstract properties - Shape with abstract `area` and `perimeter` properties
- **Example 3**: Payment gateway contract - Multiple abstract methods enforcing complete API
- **Example 4**: Partial implementation - DatabaseConnection with both abstract and concrete methods
- **Example 5**: Real-world data serializer - JSON/XML serializers following same contract

## 🎬 What Happens Behind the Scenes?

### Abstract Class Instantiation Prevention

When you try to instantiate an abstract class, Python checks for unimplemented abstract methods:

```mermaid
sequenceDiagram
    participant Code as Your Code
    participant Python as Python Interpreter
    participant ABC as ABC Metaclass
    participant Class as Animal Class

    Code->>Python: animal = Animal("Generic", 5)
    Python->>ABC: Check if class is abstract
    ABC->>Class: Get abstract methods
    Class-->>ABC: [speak, move]
    ABC->>ABC: Check if methods implemented
    ABC-->>Python: Has unimplemented methods!
    Python-->>Code: TypeError: Can't instantiate abstract class
    
    Note over Python: Instantiation blocked!<br/>Object never created
```

### Subclass Implementation Check

```mermaid
sequenceDiagram
    participant Code as Your Code
    participant Python as Python Interpreter
    participant ABC as ABC Metaclass
    participant Dog as Dog Class

    Code->>Python: dog = Dog("Buddy", 3)
    Python->>ABC: Check if class is abstract
    ABC->>Dog: Get abstract methods
    Dog-->>ABC: [] (all implemented)
    ABC-->>Python: No abstract methods!
    Python->>Dog: Create instance
    Dog-->>Code: Return dog object
    
    Note over Python: All methods implemented<br/>Object created successfully
```

### @abstractmethod vs NotImplementedError

**Approach 1: @abstractmethod with pass (Recommended)**

```mermaid
graph TD
    A[Define abstract class] --> B[Try to instantiate]
    B --> C{Has unimplemented<br/>abstract methods?}
    C -->|Yes| D[TypeError at instantiation]
    C -->|No| E[Object created]
    
    style D fill:#f96,stroke:#333,stroke-width:3px
    style E fill:#9f9,stroke:#333,stroke-width:2px
```

**Approach 2: NotImplementedError without @abstractmethod (Not Recommended)**

```mermaid
graph TD
    A[Define base class] --> B[Try to instantiate]
    B --> C[Object created successfully]
    C --> D[Call method]
    D --> E{Method implemented?}
    E -->|No| F[NotImplementedError at runtime]
    E -->|Yes| G[Method executes]
    
    style F fill:#f96,stroke:#333,stroke-width:3px
    style C fill:#ff9,stroke:#333,stroke-width:2px
```

### Contract Enforcement Flow

```mermaid
graph TD
    A[Abstract Base Class<br/>PaymentGateway] --> B[authenticate]
    A --> C[process_payment]
    A --> D[refund]
    A --> E[log_transaction<br/>concrete method]
    
    B --> F[StripeGateway]
    C --> F
    D --> F
    E --> F
    
    B --> G[PayPalGateway]
    C --> G
    D --> G
    E --> G
    
    F --> H{All methods<br/>implemented?}
    G --> I{All methods<br/>implemented?}
    
    H -->|Yes| J[✓ Can instantiate]
    H -->|No| K[✗ TypeError]
    I -->|Yes| L[✓ Can instantiate]
    I -->|No| M[✗ TypeError]
    
    style A fill:#bbf,stroke:#333,stroke-width:3px
    style J fill:#9f9,stroke:#333,stroke-width:2px
    style L fill:#9f9,stroke:#333,stroke-width:2px
    style K fill:#f96,stroke:#333,stroke-width:2px
    style M fill:#f96,stroke:#333,stroke-width:2px
```

### Abstract Properties Mechanism

```mermaid
sequenceDiagram
    participant Code as shape.area
    participant Python as Python Interpreter
    participant Property as area property
    participant Method as Concrete implementation

    Code->>Python: Access shape.area
    Python->>Property: Check if property exists
    Property-->>Python: Found property
    Python->>Method: Call getter method
    Method->>Method: Calculate area
    Method-->>Code: Return calculated value
    
    Note over Property: Property defined as abstract<br/>Must be implemented in subclass
```

### Memory Structure: Abstract Classes

```mermaid
graph TD
    A[Animal ABC] --> B[__abstractmethods__]
    B --> C[speak, move]
    
    A --> D[Concrete methods]
    D --> E[__init__, info]
    
    F[Dog instance] --> G[Dog class]
    G --> H[speak implementation]
    G --> I[move implementation]
    G -.inherits.-> A
    
    J[Try: Animal instance] -.blocked by.-> B
    
    style A fill:#bbf,stroke:#333,stroke-width:3px
    style B fill:#f96,stroke:#333,stroke-width:2px
    style F fill:#9f9,stroke:#333,stroke-width:2px
    style J fill:#f99,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5
```

### Step-by-Step: Creating Subclass

When you define a subclass of an ABC:

1. **Python checks parent class** - Identifies it inherits from ABC
2. **Collects abstract methods** - Builds list of required methods
3. **Checks subclass implementation** - Verifies each abstract method is implemented
4. **Updates abstract methods set** - Removes implemented methods from the list
5. **At instantiation** - If list is empty, allow creation; otherwise raise TypeError

### Comparison: With vs Without ABC

**Without ABC (Duck Typing):**
```python
class PaymentGateway:
    def process_payment(self, amount):
        raise NotImplementedError()

class IncompleteGateway(PaymentGateway):
    pass  # Forgot to implement!

gateway = IncompleteGateway()  # ✓ Success (BAD!)
gateway.process_payment(100)    # ✗ Error here (TOO LATE!)
```

**With ABC (Contract Enforcement):**
```python
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class IncompleteGateway(PaymentGateway):
    pass  # Forgot to implement!

gateway = IncompleteGateway()  # ✗ TypeError immediately (GOOD!)
```

### Why Use `pass` Instead of `raise NotImplementedError`?

```mermaid
graph LR
    A[@abstractmethod + pass] --> B[Error at instantiation]
    B --> C[Fail Fast ✓]
    
    D[NotImplementedError only] --> E[Error at method call]
    E --> F[Fail Late ✗]
    
    style C fill:#9f9,stroke:#333,stroke-width:3px
    style F fill:#f96,stroke:#333,stroke-width:3px
```

**Timing comparison:**
- `@abstractmethod + pass`: Error when you write `obj = MyClass()` ✓
- `NotImplementedError`: Error when you write `obj.method()` ✗

## 🚀 Run the Example

```bash
python lessons/05_abstraction/example.py
```

## 📖 Further Reading

- [Python ABC Module Documentation](https://docs.python.org/3/library/abc.html)
- [PEP 3119 - Introducing Abstract Base Classes](https://peps.python.org/pep-3119/)
- [Abstract Base Classes in Python](https://docs.python.org/3/glossary.html#term-abstract-base-class)
- [Python Data Model - Special Method Names](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- **Real-world usage**: Django uses ABCs for database backends, collections.abc provides abstract container types, unittest.TestCase is an abstract base for test classes, SQLAlchemy uses ABCs for database dialects
