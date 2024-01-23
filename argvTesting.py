import sys

def valid_args(args):
   
    if len(args) != 3:
        return False, "Exactly two command-line arguments are required."
    try:
        int(args[1])
    except ValueError:
        return False, "The first argument must be an integer."

    if not args[2].isalpha():
        return False, "The second argument must be a string."

    return True, "Arguments are valid."


args = sys.argv
is_valid, message = valid_args(args)
if is_valid:
    print("Command-line arguments are valid.")
    print(f"First argument (integer): {int(args[1])}")
    print(f"Second argument (string): {args[2]}")
else:
    print(f"Error: {message}")
