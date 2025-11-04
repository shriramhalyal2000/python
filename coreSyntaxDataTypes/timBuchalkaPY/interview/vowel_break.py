# this program accepts the words and foram a vowel list newly formed from given list

word=input("Enter a word:\n").lower()
vowels="aeiou"

vowel_list=[]

for ch in word:
    if ch in vowels:
        vowel_list.append(ch)

print(f"the appended list from the {word} list : {vowel_list}")