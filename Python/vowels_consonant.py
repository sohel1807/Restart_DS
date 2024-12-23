input="Sohel"
vowels="AEIOUaeiou"
vowel=0
consonant=0
for char in input:
    if char in vowels:
        vowel+=1
    else:
        consonant+=1
print(f'''Vowels:{vowel}
consonant:{consonant}''')