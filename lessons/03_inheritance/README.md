# Lesson 03: Inheritance

## 📚 Concept

Inheritance allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass), promoting code reuse and establishing hierarchical relationships. Python supports both single inheritance (one parent) and multiple inheritance (multiple parents). When multiple parents have the same method, Python uses Method Resolution Order (MRO) with the C3 Linearization algorithm to determine which method to call.

## 🎯 Key Points

- **Single inheritance**: Child class inherits from one parent (`class Dog(Animal)`)
- **Multiple inheritance**: Child class inherits from multiple parents (`class Child(Father, Mother)`)
- **Method overriding**: Child class can replace parent's method with its own implementation
- **super()**: Calls parent class methods to extend (not replace) functionality
- **MRO (Method Resolution Order)**: Determines the search order for methods in multiple inheritance
- **Automatic inheritance**: If child doesn't define `__init__`, parent's `__init__` is used automatically

## 💡 When to Use

- **Code reuse**: Create a base `Vehicle` class, then inherit for `Car`, `Truck`, `Motorcycle` without duplicating common code
- **Specialization**: Start with generic `Employee` class, then create specialized `Manager`, `Developer`, `Designer` subclasses
- **Multiple capabilities**: Use multiple inheritance like `class FlyingCar(Car, Aircraft)` to combine features from both parents
- **Framework design**: Build extensible systems where users can inherit from your base classes and customize behavior

## 🔍 Example Overview

The `example.py` demonstrates inheritance patterns:

- **Example 1**: Single inheritance - Dog inherits from Animal
- **Example 2**: Using super() - ElectricCar extends Vehicle with additional attributes
- **Example 3**: Multiple inheritance - Child inherits from both Father and Mother
- **Example 4**: MRO demonstration - Diamond problem with A, B, C, D classes
- **Example 5**: Real-world hierarchy - Person → Employee → Manager chain

## 🎬 What Happens Behind the Scenes?

### Single Inheritance: Automatic __init__ Inheritance

When a child class doesn't define `__init__`, Python automatically uses the parent's:

```mermaid
sequenceDiagram
    participant Code as Your Code
    participant Python as Python Interpreter
    participant Dog as Dog Class
    participant Animal as Animal Class

    Code->>Python: dog = Dog("Buddy", 3)
    Python->>Dog: Check for Dog.__init__
    Dog-->>Python: Not found
    Python->>Animal: Use Animal.__init__
    Animal->>Animal: Set self.name = "Buddy"
    Animal->>Animal: Set self.age = 3
    Animal-->>Python: Return initialized object
    Python-->>Code: dog object ready
```

### Using super() for Extended Initialization

When a child class defines its own `__init__`, it must call `super().__init__()`:

```mermaid
sequenceDiagram
    participant Code as Your Code
    participant ElectricCar as ElectricCar.__init__
    participant Super as super()
    participant Vehicle as Vehicle.__init__
    participant Memory as Object Memory

    Code->>ElectricCar: ElectricCar("Tesla", "Model 3", 75)
    ElectricCar->>Super: super().__init__("Tesla", "Model 3")
    Super->>Vehicle: Call parent __init__
    Vehicle->>Memory: Set self.brand = "Tesla"
    Vehicle->>Memory: Set self.model = "Model 3"
    Vehicle-->>ElectricCar: Parent initialization complete
    ElectricCar->>Memory: Set self.battery_capacity = 75
    ElectricCar-->>Code: Return fully initialized object
```

**Why super() is needed:**
- Without `super().__init__()`: Parent attributes (`brand`, `model`) are NOT set
- With `super().__init__()`: Parent initializes its attributes, then child adds more

### Multiple Inheritance and MRO

The diamond problem occurs when multiple inheritance paths lead to the same base class:

```mermaid
graph TD
    A[Class A<br/>method] --> B[Class B<br/>method - overrides A]
    A --> C[Class C<br/>method - overrides A]
    B --> D[Class D<br/>inherits B, C]
    C --> D
    
    style D fill:#f9f,stroke:#333,stroke-width:4px
    style A fill:#bbf,stroke:#333,stroke-width:2px
```

**MRO Resolution:**

```mermaid
graph LR
    D[D] --> B[B]
    B --> C[C]
    C --> A[A]
    A --> O[object]
    
    style D fill:#f96,stroke:#333,stroke-width:3px
    style B fill:#9f6,stroke:#333,stroke-width:2px
    style C fill:#69f,stroke:#333,stroke-width:2px
```

**Search order: D → B → C → A → object**

### Method Lookup Process

When you call `d.method()`:

```mermaid
sequenceDiagram
    participant Code as d.method()
    participant D as Class D
    participant B as Class B
    participant C as Class C
    participant A as Class A

    Code->>D: Search for method()
    D-->>Code: Not found in D
    Code->>B: Check next in MRO (B)
    B-->>Code: Found! Return "Method from B"
    
    Note over C,A: C and A are never checked<br/>because B already has the method
```

### MRO Algorithm (C3 Linearization)

Python uses C3 Linearization to create MRO:

**Rules:**
1. **Child before parents**: The class itself comes first
2. **Left-to-right**: Parents are checked in the order listed
3. **Parents before grandparents**: Check immediate parents before their parents
4. **No duplicates**: Each class appears exactly once

**Example: `class Child(Father, Mother)`**

```mermaid
graph TD
    Child[Child] --> Father[Father]
    Child --> Mother[Mother]
    Father --> object1[object]
    Mother --> object2[object]
    
    MRO[MRO: Child → Father → Mother → object]
    
    style Child fill:#f96
    style MRO fill:#9f9,stroke:#333,stroke-width:3px
```

**Why this order?**
- Start with `Child` (the class itself)
- Then `Father` (first parent listed)
- Then `Mother` (second parent listed)
- Finally `object` (base of everything, appears only once)

### Memory Structure in Inheritance

```mermaid
graph TD
    A[dog object] --> B[Instance __dict__]
    B --> C[name: 'Buddy']
    B --> D[age: 3]
    
    A --> E[__class__: Dog]
    E --> F[Dog methods]
    F --> G[speak: 'Woof!']
    F --> H[fetch: ...]
    
    E --> I[__bases__: Animal]
    I --> J[Animal methods]
    J --> K[speak: 'Some sound']
    J --> L[info: ...]
    
    M[dog.speak] -.lookup.-> F
    N[dog.info] -.lookup.-> F
    F -.not found.-> J
    J -.found!.-> L
```

**Key insight**: 
- Instance data is stored in the object's `__dict__`
- Methods are looked up through the class hierarchy
- MRO determines the search path

## 🚀 Run the Example

```bash
python lessons/03_inheritance/example.py
```

## 📖 Further Reading

- [Python Inheritance Documentation](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Method Resolution Order (MRO)](https://www.python.org/download/releases/2.3/mro/)
- [The Python 2.3 Method Resolution Order (C3)](https://www.python.org/download/releases/2.3/mro/)
- [PEP 253 - Subtyping Built-in Types](https://peps.python.org/pep-0253/)
- **Real-world usage**: Django models use inheritance for model hierarchies, unittest.TestCase is inherited for test classes, Exception classes use inheritance for error hierarchies
