#Words are way more edgy when you replace the letter i with an exclamation point!

#Write the function exclamation that takes a string and then returns the same string with every lowercase i replaced with an exclamation point. Your function should:

#Convert the initial string to a list

#Use a for loop to go through your list element by element

#Whenever you see a lowercase i, replace it with an exclamation point in the list

#Return the stringified version of the list when your for loop is finished

#Here’s what an example run of your program might look like:

#exclamation("I like music.")
# => I l!ke mus!c.
#python
#exclamation("Mississippi")
# => M!ss!ss!pp!


def exclamation(text):
    #Convert the initial string to a list
    text_list = list(text)

    #Use a for loop to go through your list element by element
    i = 0
    for i in range(len(text_list)):
        # print(letter)
        if text_list[i] == "i":
            # print("before", letter)
            text_list[i] = "!"
            # print("after", letter)
            


    # 
    # i = 0
    # for letter in (text_list):
    #     if letter == "i":
    #         text_list[i] = "!"
    #     i= i + 1
    
    # 
    # for i, letter in enumerate(text_list):
    #     if letter == "i":
    #         text_list[i] = "!"
    #     i= i + 1


    print("text_list : ", text_list)
    x = "".join(text_list)
    print("x : ", x)

    return x
            

            
print(exclamation("I like music."))
print(exclamation("Mississippi"))
    





# 자료구조 리스트, 객체, 문자열 > 인덱스랑 값이 있을때
# enumerate 자료형으로 바꾸는거 > 반복하기 편하게 만든거

# 일종의 for문 약식표현


# list(문자) > 리스트로 바뀌잖아
