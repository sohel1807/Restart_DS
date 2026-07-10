from langchain_community.tools import tool

@tool
def multiply_numbers(a:int,b:int)->int:
    """Multiplies two numbers."""
    # return a*b
    return a * b

result = multiply_numbers.invoke({"a": 5, "b": 10})

print(result)
print(multiply_numbers.name)
print(multiply_numbers.description)
print(multiply_numbers.args)