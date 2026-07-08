def input_temperature(temp_str) -> int:
    temp_int = int(temp_str)
    return (temp_int)


def test_temperature(temp_str) -> None:
    try:
        input_temperature(temp_str)
    except ValueError:
        print(f"Input data is ’{temp_str}’")
        print("Caught input_temperature error: ", end="")
        print("invalid literal for int() with", end="")
        print(f" base 10: ’{temp_str}’")
    else:
        print(f"Input data is ’{temp_str}’")
        print(f"Temperature is now {temp_str}°C")


def main() -> None:
    print("=== Garden Temperature ===")
    print()
    test_temperature("25")
    print()
    test_temperature("abc")
    print()
    print("All tests completed - program didn’t crash!")


if __name__ == "__main__":
    main()
