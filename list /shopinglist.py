while (True):
    list_of_items_to_buy = [["tea","cinemmon","bannanna"],
             ["white bread","milk","butter"],
             ["brown bread","penutbutter","snacks"]]
    print("row starts at 0 and ends at 2 ")
    print("colum starts at 0 and eds at 2 ")
    question = input("which row do you want ot chose form ") 
    question_2 = input("which colum do you what to chose from")
    print(list_of_items_to_buy[int(question)][int(question_2)])

