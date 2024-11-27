# Your friend wants to try to make a word ladder! This is a list of words where each word has a one-letter difference from the word before it. Here’s an example:

# cat
# cot
# cog
# log
# Write a program to help your friend. It should do the following:

# Ask your friend for an initial word
# Repeatedly ask them for an index and a letter
# You should replace the letter at the index they provided with the letter they enter
# You should then print the new word
# Stop asking for input when the user enters -1 for the index
# Here’s what should be happening behind the scenes:

# You should have a function, get_index, that repeatedly asks the user for an index until they enter a valid integer that is within the acceptable range of indices for the initial string. (If they enter a number out of range, you should reply invalid index.)
# You should have another function, get_letter, that repeatedly asks the user for a letter until they enter exactly one lowercase letter. (If they enter more than one character, you should reply Must be exactly one character!. If they enter a capital letter, you should reply Character must be a lowercase letter!.)
# You should store a list version of the current word in a variable. This is what you should update each time the user swaps out a new letter.
# Each time you have to print the current word, print the string version of the list you are keeping in your variable.
# Here’s what an example run of your program might look like:

# Enter a word: cat
# Enter an index (-1 to quit): 1
# Enter a letter: o
# cot
# Enter an index (-1 to quit): 2
# Enter a letter: g
# cog
# Enter an index (-1 to quit): 5
# Invalid index
# Enter an index (-1 to quit): -3
# Invalid index
# Enter an index (-1 to quit): 0
# Enter a letter: L
# Character must be a lowercase letter!
# Enter a letter: l
# log
# Enter an index (-1 to quit): -1
# Creating and Altering Data Structures
# 12.1
# 12.2
# 12.3
# 12.4
# 12.5



# 첫 단어 입력 받기 cat
# data =input

# # 반복
# while(true)
# ## 인덱스와 글자 입력
#     a=input1
#     b=input
# ## 해당 인덱스의 글자를 변경
#     data[a] = b
# ## 출력 cot
#     print
    
# ## 탈출조건
# ### 인덱스에다가 -1 탈출
#     if()
# ## 예외처리
#     if()

word = input("Enter a word:")
while True:
    while True:
        index = int(input("Enter an index (-1 to quit):"))
        # 인덱스가 없을때
        if index < -1:
            print("Invalid index")
            continue
        break
    
    if index == -1:
        break

    while True:
        letter = input("Enter a letter:")
        if not letter.islower():
            # 소문자가 아님
            print("Character must be a lowercase letter!")
            continue
        break

    list_word = list(word)
    list_word[index] = letter
    word = "".join(list_word)
    print(word)


