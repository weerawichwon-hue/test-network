def add_numbers(a: int, b: int) -> int:
    result = a + b
    return str(result)  # intentionally wrong return type for mypy


def greet(name):
    message = "Hello, " + name
    print(message)
    return message


if __name__ == "__main__":
    greet("World")
    print(add_numbers(2, 3))
