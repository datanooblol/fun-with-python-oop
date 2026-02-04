"""
Lesson 06: Magic Methods (Dunder Methods)
Demonstrates: __str__, __repr__, __len__, __getitem__, __call__, and other magic methods
"""

# Example 1: __str__ vs __repr__ - The Key Difference
# __str__: For end users (readable, informal)
# __repr__: For developers (unambiguous, reproducible)
#
# Format specifiers in f-strings:
# {value}    - calls str(value)
# {value!r}  - calls repr(value) - adds quotes for strings!
# {value!s}  - calls str(value) - explicit
# {value!a}  - calls ascii(value) - escapes non-ASCII
class Person:
    """Person class demonstrating __str__ and __repr__."""
    
    def __init__(self, name: str, age: int, email: str) -> None:
        """Initialize Person instance.
        
        Args:
            name (str): Person's name.
            age (int): Person's age.
            email (str): Person's email.
        """
        self.name = name
        self.age = age
        self.email = email
    
    def __str__(self) -> str:
        """String representation for END USERS (readable).
        
        Called by: str(obj), print(obj), f"{obj}"
        Goal: Human-readable, friendly output
        
        Returns:
            str: User-friendly string.
        """
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self) -> str:
        """String representation for DEVELOPERS (unambiguous).
        
        Called by: repr(obj), interactive console, debugger
        Goal: Unambiguous, ideally can recreate object
        
        Note: Using !r in f-string calls repr() on each value.
        This adds quotes around strings: 'Alice' instead of Alice
        Makes it clear that name is a string, not a variable.
        
        Returns:
            str: Developer-friendly representation.
        """
        # {self.name!r} is equivalent to {repr(self.name)}
        # For string "Alice", !r produces 'Alice' (with quotes)
        # For number 30, !r produces 30 (no change)
        return f"Person(name={self.name!r}, age={self.age!r}, email={self.email!r})"

person = Person("Alice", 30, "alice@example.com")

print("__str__ vs __repr__ Demo:")
print(f"str(person):  {str(person)}")      # Calls __str__
print(f"repr(person): {repr(person)}")     # Calls __repr__
print(f"print(person): ", end="")
print(person)                               # Calls __str__
print(f"In list: {[person]}")              # Calls __repr__ for items in containers!

print("\n!r Format Specifier Demo:")
name = "Alice"
print(f"Without !r: {name}")               # Output: Alice
print(f"With !r:    {name!r}")             # Output: 'Alice' (with quotes!)
print(f"Using repr(): {repr(name)}")       # Output: 'Alice' (same as !r)

age = 30
print(f"\nNumber without !r: {age}")      # Output: 30
print(f"Number with !r:    {age!r}")       # Output: 30 (no difference for numbers)


# Example 2: What Happens Without __str__ or __repr__?
class PersonNoMagic:
    """Person without magic methods."""
    
    def __init__(self, name: str, age: int) -> None:
        """Initialize PersonNoMagic instance.
        
        Args:
            name (str): Person's name.
            age (int): Person's age.
        """
        self.name = name
        self.age = age

class PersonOnlyStr:
    """Person with only __str__."""
    
    def __init__(self, name: str, age: int) -> None:
        """Initialize PersonOnlyStr instance.
        
        Args:
            name (str): Person's name.
            age (int): Person's age.
        """
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        """String representation.
        
        Returns:
            str: User-friendly string.
        """
        return f"{self.name}, {self.age} years old"

class PersonOnlyRepr:
    """Person with only __repr__."""
    
    def __init__(self, name: str, age: int) -> None:
        """Initialize PersonOnlyRepr instance.
        
        Args:
            name (str): Person's name.
            age (int): Person's age.
        """
        self.name = name
        self.age = age
    
    def __repr__(self) -> str:
        """Developer representation.
        
        Returns:
            str: Developer-friendly representation.
        """
        return f"PersonOnlyRepr(name={self.name!r}, age={self.age!r})"

no_magic = PersonNoMagic("Bob", 25)
only_str = PersonOnlyStr("Charlie", 35)
only_repr = PersonOnlyRepr("Diana", 28)

print("\n\nFallback Behavior:")
print(f"No magic methods:")
print(f"  str():  {str(no_magic)}")   # Falls back to __repr__, then default
print(f"  repr(): {repr(no_magic)}")  # Default: <__main__.PersonNoMagic object at 0x...>

print(f"\nOnly __str__:")
print(f"  str():  {str(only_str)}")   # Uses __str__
print(f"  repr(): {repr(only_str)}")  # Falls back to default (no __repr__)

print(f"\nOnly __repr__:")
print(f"  str():  {str(only_repr)}")  # Falls back to __repr__!
print(f"  repr(): {repr(only_repr)}") # Uses __repr__


# Example 3: __getitem__ vs __getattr__ - Different Purposes!
# __getitem__: For INDEXING with brackets obj[key]
# __getattr__: For ATTRIBUTE ACCESS with dot obj.attribute
class Playlist:
    """Music playlist with container magic methods.
    
    __getitem__: playlist[0] - access by index
    __getattr__: playlist.name - access by attribute name
    """
    
    def __init__(self, name: str) -> None:
        """Initialize Playlist instance.
        
        Args:
            name (str): Playlist name.
        """
        self.name = name
        self._songs = []
    
    def add_song(self, song: str) -> None:
        """Add song to playlist.
        
        Args:
            song (str): Song name.
        """
        self._songs.append(song)
    
    def __len__(self) -> int:
        """Return number of songs.
        
        Called by: len(obj)
        
        Returns:
            int: Number of songs.
        """
        return len(self._songs)
    
    def __getitem__(self, index: int) -> str:
        """Get song by INDEX (bracket notation).
        
        Called by: obj[index], for loops, slicing
        Use case: playlist[0], playlist[1:3]
        
        Args:
            index (int): Song index.
            
        Returns:
            str: Song name.
        """
        return self._songs[index]
    
    def __setitem__(self, index: int, value: str) -> None:
        """Set song at index.
        
        Called by: obj[index] = value
        
        Args:
            index (int): Song index.
            value (str): New song name.
        """
        self._songs[index] = value
    
    def __delitem__(self, index: int) -> None:
        """Delete song at index.
        
        Called by: del obj[index]
        
        Args:
            index (int): Song index.
        """
        del self._songs[index]
    
    def __contains__(self, song: str) -> bool:
        """Check if song is in playlist.
        
        Called by: item in obj
        
        Args:
            song (str): Song name.
            
        Returns:
            bool: True if song exists, False otherwise.
        """
        return song in self._songs
    
    def __iter__(self):
        """Make playlist iterable.
        
        Called by: for item in obj
        
        Returns:
            iterator: Songs iterator.
        """
        return iter(self._songs)
    
    def __str__(self) -> str:
        """String representation.
        
        Returns:
            str: Playlist description.
        """
        return f"Playlist '{self.name}' with {len(self)} songs"
    
    def __repr__(self) -> str:
        """Developer representation.
        
        Returns:
            str: Playlist representation.
        """
        return f"Playlist(name={self.name!r}, songs={self._songs!r})"

playlist = Playlist("My Favorites")
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")

print("\n\nContainer Magic Methods Demo:")
print(f"Length: {len(playlist)}")           # __len__
print(f"First song: {playlist[0]}")         # __getitem__
print(f"'Song B' in playlist: {'Song B' in playlist}")  # __contains__

print("Iterating:")
for song in playlist:                        # __iter__ and __getitem__
    print(f"  - {song}")

playlist[1] = "Song B Updated"               # __setitem__
print(f"After update: {playlist[1]}")

del playlist[2]                              # __delitem__
print(f"After deletion, length: {len(playlist)}")


# Example 3b: __getattr__, __setattr__, __delattr__ - Attribute Access
# These are for DOT notation (obj.attr), not brackets (obj[key])
class DynamicConfig:
    """Configuration object with dynamic attribute access.
    
    __getattr__:  Called when attribute is NOT found normally
    __setattr__:  Called for ALL attribute assignments
    __delattr__:  Called when deleting attributes
    """
    
    def __init__(self) -> None:
        """Initialize DynamicConfig instance."""
        # Use object.__setattr__ to avoid infinite recursion
        object.__setattr__(self, '_data', {})
    
    def __getattr__(self, name: str):
        """Get attribute by NAME (dot notation).
        
        Called by: obj.attribute (when attribute doesn't exist normally)
        Only called if attribute is NOT found in obj.__dict__
        
        Args:
            name (str): Attribute name.
            
        Returns:
            Any: Attribute value.
            
        Raises:
            AttributeError: If attribute not found.
        """
        print(f"__getattr__ called for: {name}")
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"'{type(self).__name__}' has no attribute '{name}'")
    
    def __setattr__(self, name: str, value) -> None:
        """Set attribute by NAME (dot notation).
        
        Called by: obj.attribute = value (for ALL assignments!)
        Be careful: can cause infinite recursion if not handled properly
        
        Args:
            name (str): Attribute name.
            value: Attribute value.
        """
        print(f"__setattr__ called for: {name} = {value}")
        # Store in _data dictionary instead of normal attribute
        self._data[name] = value
    
    def __delattr__(self, name: str) -> None:
        """Delete attribute by NAME (dot notation).
        
        Called by: del obj.attribute
        
        Args:
            name (str): Attribute name.
            
        Raises:
            AttributeError: If attribute not found.
        """
        print(f"__delattr__ called for: {name}")
        if name in self._data:
            del self._data[name]
        else:
            raise AttributeError(f"'{type(self).__name__}' has no attribute '{name}'")
    
    def __repr__(self) -> str:
        """Developer representation.
        
        Returns:
            str: Config representation.
        """
        return f"DynamicConfig(data={self._data!r})"

config = DynamicConfig()

print("\n\n__getattr__, __setattr__, __delattr__ Demo:")
config.database = "PostgreSQL"    # Calls __setattr__
config.port = 5432                 # Calls __setattr__
print(f"Database: {config.database}")  # Calls __getattr__
print(f"Port: {config.port}")          # Calls __getattr__

del config.port                    # Calls __delattr__
print(f"After deletion: {config}")

print("\nComparison:")
print("__getitem__/__setitem__: For INDEXING - obj[key]")
print("__getattr__/__setattr__: For ATTRIBUTES - obj.attr")


# Example 4: Callable Objects with __call__
class Multiplier:
    """Callable object that multiplies by a factor."""
    
    def __init__(self, factor: int) -> None:
        """Initialize Multiplier instance.
        
        Args:
            factor (int): Multiplication factor.
        """
        self.factor = factor
    
    def __call__(self, x: int) -> int:
        """Make object callable like a function.
        
        Called by: obj(args)
        
        Args:
            x (int): Number to multiply.
            
        Returns:
            int: Result of multiplication.
        """
        return x * self.factor
    
    def __repr__(self) -> str:
        """Developer representation.
        
        Returns:
            str: Multiplier representation.
        """
        return f"Multiplier(factor={self.factor})"

times_three = Multiplier(3)
times_five = Multiplier(5)

print("\n\n__call__ Demo (Callable Objects):")
print(f"times_three(10) = {times_three(10)}")  # Calls __call__
print(f"times_five(7) = {times_five(7)}")      # Calls __call__
print(f"Is callable? {callable(times_three)}")


# Example 5: Comparison Magic Methods
class Version:
    """Version number with comparison support."""
    
    def __init__(self, major: int, minor: int, patch: int) -> None:
        """Initialize Version instance.
        
        Args:
            major (int): Major version.
            minor (int): Minor version.
            patch (int): Patch version.
        """
        self.major = major
        self.minor = minor
        self.patch = patch
    
    def _as_tuple(self) -> tuple:
        """Convert to tuple for comparison.
        
        Returns:
            tuple: Version as tuple.
        """
        return (self.major, self.minor, self.patch)
    
    def __eq__(self, other: 'Version') -> bool:
        """Check equality.
        
        Called by: obj == other
        
        Args:
            other (Version): Other version.
            
        Returns:
            bool: True if equal, False otherwise.
        """
        return self._as_tuple() == other._as_tuple()
    
    def __lt__(self, other: 'Version') -> bool:
        """Check less than.
        
        Called by: obj < other
        
        Args:
            other (Version): Other version.
            
        Returns:
            bool: True if less than, False otherwise.
        """
        return self._as_tuple() < other._as_tuple()
    
    def __le__(self, other: 'Version') -> bool:
        """Check less than or equal.
        
        Called by: obj <= other
        
        Args:
            other (Version): Other version.
            
        Returns:
            bool: True if less than or equal, False otherwise.
        """
        return self._as_tuple() <= other._as_tuple()
    
    def __gt__(self, other: 'Version') -> bool:
        """Check greater than.
        
        Called by: obj > other
        
        Args:
            other (Version): Other version.
            
        Returns:
            bool: True if greater than, False otherwise.
        """
        return self._as_tuple() > other._as_tuple()
    
    def __ge__(self, other: 'Version') -> bool:
        """Check greater than or equal.
        
        Called by: obj >= other
        
        Args:
            other (Version): Other version.
            
        Returns:
            bool: True if greater than or equal, False otherwise.
        """
        return self._as_tuple() >= other._as_tuple()
    
    def __str__(self) -> str:
        """String representation.
        
        Returns:
            str: Version string.
        """
        return f"v{self.major}.{self.minor}.{self.patch}"
    
    def __repr__(self) -> str:
        """Developer representation.
        
        Returns:
            str: Version representation.
        """
        return f"Version({self.major}, {self.minor}, {self.patch})"

v1 = Version(1, 2, 3)
v2 = Version(1, 2, 5)
v3 = Version(2, 0, 0)

print("\n\nComparison Magic Methods Demo:")
print(f"{v1} == {v2}: {v1 == v2}")
print(f"{v1} < {v2}: {v1 < v2}")
print(f"{v2} < {v3}: {v2 < v3}")
print(f"{v3} > {v1}: {v3 > v1}")

versions = [v3, v1, v2]
print(f"Unsorted: {[str(v) for v in versions]}")
print(f"Sorted: {[str(v) for v in sorted(versions)]}")


# Example 6: Context Manager with __enter__ and __exit__
# Context managers ensure resources are properly cleaned up
# The 'with' statement automatically calls __enter__ and __exit__
#
# Execution flow:
# 1. with FileLogger("app.log") as logger:  # Creates object
# 2.     __enter__() is called                # Opens file
# 3.     logger = return value of __enter__   # Assigns to 'logger'
# 4.     # Your code runs here
# 5.     __exit__() is called                 # Closes file (ALWAYS runs!)
#
# Benefits:
# - File is ALWAYS closed, even if exception occurs
# - No need to remember to call close()
# - Cleaner, more readable code
class FileLogger:
    """Context manager for file logging.
    
    Demonstrates: __enter__ and __exit__ for resource management
    Use case: Automatically open and close files
    """
    
    def __init__(self, filename: str) -> None:
        """Initialize FileLogger instance.
        
        Args:
            filename (str): Log file name.
        """
        self.filename = filename
        self.file = None
    
    def __enter__(self) -> 'FileLogger':
        """Enter context manager - SETUP phase.
        
        Called by: with statement (at the beginning)
        When: Right after 'with FileLogger(...) as logger:'
        
        This is where you:
        - Open files
        - Acquire locks
        - Connect to databases
        - Allocate resources
        
        Returns:
            FileLogger: Self reference (assigned to 'as' variable).
        """
        print(f"[__enter__] Opening {self.filename}")
        self.file = open(self.filename, 'w')
        return self  # This becomes the 'logger' variable
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """Exit context manager - CLEANUP phase.
        
        Called by: with statement (at the end, ALWAYS!)
        When: After the with block finishes (even if exception occurs)
        
        This is where you:
        - Close files
        - Release locks
        - Disconnect from databases
        - Free resources
        
        Args:
            exc_type: Exception type if error occurred, None otherwise.
            exc_val: Exception value if error occurred, None otherwise.
            exc_tb: Exception traceback if error occurred, None otherwise.
            
        Returns:
            bool: True to suppress exception, False to propagate it.
                  Usually return False to let exceptions bubble up.
        """
        print(f"[__exit__] Closing {self.filename}")
        if exc_type:
            print(f"[__exit__] Exception occurred: {exc_type.__name__}: {exc_val}")
        if self.file:
            self.file.close()
        return False  # Don't suppress exceptions
    
    def log(self, message: str) -> None:
        """Write log message.
        
        Args:
            message (str): Log message.
        """
        if self.file:
            self.file.write(f"{message}\n")
    
    def __repr__(self) -> str:
        """Developer representation.
        
        Returns:
            str: FileLogger representation.
        """
        return f"FileLogger(filename={self.filename!r})"

print("\n\nContext Manager Demo:")
print("Execution flow:")
print("1. Create FileLogger object")
print("2. Call __enter__() - opens file")
print("3. Execute code inside 'with' block")
print("4. Call __exit__() - closes file (ALWAYS!)\n")

with FileLogger("app.log") as logger:
    print("[Inside with block] Writing logs...")
    logger.log("Application started")
    logger.log("Processing data")
    logger.log("Application finished")
    print("[Inside with block] Done writing")

print("[Outside with block] File automatically closed!")

# Demonstrate exception handling
print("\nWith exception:")
try:
    with FileLogger("error.log") as logger:
        logger.log("Starting...")
        raise ValueError("Something went wrong!")
        logger.log("This won't execute")
except ValueError as e:
    print(f"[Caught exception] {e}")
print("[Outside] File still closed properly!")


# Main execution
if __name__ == "__main__":
    print("\n=== Magic Methods Demo ===\n")
    
    print("Key Differences:")
    print("__str__:  For end users (print, str)")
    print("__repr__: For developers (repr, console, debugger)")
    print("\nRule of thumb:")
    print("- Always implement __repr__ (for debugging)")
    print("- Implement __str__ if you need user-friendly output")
    print("- If only __repr__ exists, str() will use it as fallback")
    print("\nIn containers (lists, dicts), Python uses __repr__ for items!")
