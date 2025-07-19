# TODO: Implement the SecretKeyGenerator class and its methods below.
#
# What should you do?
# Create a class called SecretKeyGenerator that can help generate and store a secret key in a .env file.
# The class should:
#   - Have a method to generate a secure secret key (for example, using Python's secrets module)
#   - Have a method to write the key to a .env file, only if it doesn't already exist
#   - Have a method to check if the key is already present in the file
#
# Example usage:
#   generator = SecretKeyGenerator()
#   generator.write_to_file()  # This should add a line like SECRET_KEY=... to the .env file if not present
#
# Try to write code that follows these rules!
                return False
