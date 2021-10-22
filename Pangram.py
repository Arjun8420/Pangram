#Porgram to verify given String is Pangram or not

data = input("Enter the String = ")
data = data.upper()
freq = [False] * 26

for c in data:
    if c.isalpha():
        freq[ord(c) - 65] = True
        
if all(freq) == True:
    print("Entered String is Pangram")
else:
    print("Entered string is not Pangram")
