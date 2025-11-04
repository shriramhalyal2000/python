# accept and count vowels

word=input("Enter a word:\n").lower()
vowels="aeiou"

vowel_count=0
for ch in word:
    if ch in vowels:
        vowel_count+=1


print(f"total vowels in {word} is :{vowel_count}")