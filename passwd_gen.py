import string
import random

# This function will generate a random password with the following policy:
# - At least one lower case letter
# - At least one upper case letter
# - At least one digit
# - At least one special character
# - Length of 16 characters
def random_password():
    pass_len = 16
    pass_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    random_pass = ''.join(random.choice(pass_chars) for _ in range(pass_len))
    while not (any(c.islower() for c in random_pass) and any(c.isupper() for c in random_pass) and any(c.isdigit() for c in random_pass) and any(c in string.punctuation for c in random_pass)):
        random_pass = ''.join(random.choice(pass_chars) for _ in range(pass_len))
    print(random_pass)

# This function will generate a password with the following rules:
# - 3 random words from fr_words.txt
# - Each word capitalized
# - Each word separated by either '-', '_', or '.'
def three_words_password():
    with open('fr_words.txt', 'r', encoding='utf-8') as fichier:
        words = fichier.readlines()
        words = [word.strip().capitalize() for word in words]
        pass_sep = ['-', '_', '.']
        random_sep = random.choice(pass_sep)
        random_pass = random_sep.join(random.choice(words) for _ in range(3))
        print(random_pass)

def main():
        print("\nGenerating 10 random passwords : \n")
        for i in range(10):
            random_password()
        print("\n\nGenerating 10 passwords with 3 random words : \n")
        for i in range(10):
            three_words_password()
       
if __name__ == '__main__':
    main()