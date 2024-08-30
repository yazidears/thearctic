import os
import random
import string

def generate_random_name(length):
    """Generates a random string of specified length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def rename_html_files():
    """Renames HTML files in the current directory to random strings."""
    existing_names = set()
    for filename in os.listdir():
        if filename.endswith(".html"):
            new_name = generate_random_name(random.randint(1, 3))
            while new_name in existing_names:
                new_name = generate_random_name(random.randint(1, 3))
            existing_names.add(new_name)
            os.rename(filename, new_name + ".html")

if __name__ == "__main__":
    rename_html_files()