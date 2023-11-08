def count_vowels_and_consonants(input_string):
    # Define a set of vowels (both uppercase and lowercase)
    vowels = "aeiouAEIOU"

    # Initialize counters
    vowel_count = 0
    consonant_count = 0

    # Iterate through each character in the input string
    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Get input from the user
user_input = input("Enter a string: ")

vowels, consonants = count_vowels_and_consonants(user_input)

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
