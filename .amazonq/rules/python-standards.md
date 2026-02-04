# Python Coding Standards for fun-with-python-oop

## Type Hints
- ALWAYS use type hints for all function/method parameters and return types
- Format: `def function(param: str, count: int) -> list[str]:`
- Use `-> None` for functions that don't return anything
- Annotate class attributes: `class_var: str = "value"`

## Docstrings
- ALWAYS use Google-style docstrings for all classes and methods
- Format for Args section: `param (datatype): description`
- Example:
  ```python
  def example(name: str, age: int) -> str:
      """Short description.
      
      Args:
          name (str): Person's name.
          age (int): Person's age.
          
      Returns:
          str: Formatted string.
      """
  ```

## Code Style
- Use only native Python libraries in example.py files
- External libraries can be mentioned in README.md only
- Keep code minimal and focused on the concept being taught
- Use clear, descriptive variable names

## Documentation
- Every class must have a docstring
- Every method must have a docstring (except simple property getters if obvious)
- Include Args, Returns, and Raises sections as needed
