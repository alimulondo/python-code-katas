# TODO: Implement the StringCalculator class and its add method below.
#
# What should you do?
# Create a class called StringCalculator with a method named add(self, numbers: str).
# The add method should:
#   - Take a string of numbers separated by commas or newlines (e.g. "1,2,3" or "1\n2,3")
#   - Return the sum of the numbers
#   - Return 0 if the input string is empty
#   - Ignore numbers greater than 1000
#   - Raise an exception if any number is negative
#
# Example usage:
#   sc = StringCalculator()
#   result = sc.add("1,2,3")      # result should be 6
#   result = sc.add("1\n2,3")    # result should be 6
#   result = sc.add("")          # result should be 0
#   result = sc.add("2,1001")    # result should be 2
#   sc.add("1,-2,3")             # should raise an exception
#
# Try to write code that follows these rules!
