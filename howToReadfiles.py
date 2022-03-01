def count_vowels(string_input):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count_vowels = 0
    for x in string_input:
        if x in vowels:
            count_vowels += 1
    return count_vowels


with open("Python/ReadingFiles/textFile.txt", 'r') as file:
    file1 = file.read()
    print(count_vowels(file1))
    file.close()
    pass