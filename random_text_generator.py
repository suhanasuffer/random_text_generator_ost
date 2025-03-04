import random

def generate_random_text(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?'
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    text_length = 100  # Change this to adjust the length of generated text
    random_text = generate_random_text(text_length)
    print(random_text)
