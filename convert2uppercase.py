def convert_even_to_uppercase(s):
  """Converts all even indexed characters in a string to uppercase.

  Args:
    s: The string to convert.

  Returns:
    A new string with all even indexed characters converted to uppercase.
  """

  result = ""
  for i, char in enumerate(s):
    if i % 2 == 0:
      result += char.upper()
    else:
      result += char
  return result

# Example usage
string = "Hello, world!"
converted_string = convert_even_to_uppercase(string)
print(converted_string)  # Output: HeLlO, wOrLd!
