def count_vowels_and_consonants(string):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    for char in string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

string = input("Enter a string: ")
vowels, consonants = count_vowels_and_consonants(string)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
