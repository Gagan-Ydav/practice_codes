from blackjack_art import logo
import random
import os

card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
comp_cards = []

def card_adder(list1,list2):
        return {
            "list1": sum(list1),
            "list2": sum(list2),
        }


for i in range(2):
    user_cards.append(random.choice(card_list))
    comp_cards.append(random.choice(card_list))

def blackjack(list1,list2):
    card_output = card_adder(list1,list2)
    user_sum = card_output["list1"]
    comp_sum = card_output["list2"]
    play_game = True
    while play_game:
        if (comp_sum == 21) or (user_sum == 21 and comp_sum != 21):
            if comp_sum == 21:
                play_game = False
                return "lose"
            else:
                play_game == False
                return "win"
        elif user_sum > 21 or comp_sum > 21:
            if (11 in list1):
                list1.remove(11) 
                list1.append(1)  
            if (11 in list2):    
                list2.remove(11)
                list2.append(1)
            card_output = card_adder(list1,list2)
            user_sum = card_output["list1"]
            comp_sum = card_output["list2"]
            if (comp_sum > 21 and user_sum < 21) or (user_sum == 21 and comp_sum != 21) or (user_sum < 21 and comp_sum < 21 and user_sum > comp_sum):
                play_game = False
                return "win"
            else:
                play_game = False
                return "lose"
        else:
            user_input = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_input == "n":
                while sum(list2) < 17:
                    list2.append(random.choice(card_list))
                card_output = card_adder(list1,list2)
                user_sum = card_output["list1"]
                comp_sum = card_output["list2"]
                if comp_sum > 21:
                    return "win"
                else:
                    if user_sum == comp_sum:
                        return "draw"
                    elif user_sum > comp_sum:
                        return "win"
                    else:
                        return "lose" 
                play_game = False
            else:
                print(f"Your cards: {list1}, current score = {sum(list1)}\nComputer's first card: {list2[0]}")
                list1.append(random.choice(card_list))



user_response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if user_response == "y":
    blackjack(user_cards,comp_cards)
    output = blackjack(user_cards,comp_cards)
    if output == "win":
        print(f"Your final hand: {user_cards}, final score = {sum(user_cards)}\nComputer's final hand: {comp_cards}, final score: {sum(comp_cards)}\nYou win.😈")
    elif output == "lose":
        print(f"Your final hand: {user_cards}, final score = {sum(user_cards)}\nComputer's final hand: {comp_cards}, final score: {sum(comp_cards)}\nYou lose.😤")
    else:
        print(f"Your final hand: {user_cards}, final score = {sum(user_cards)}\nComputer's final hand: {comp_cards}, final score: {sum(comp_cards)}\nIt's a draw.😌")
            

            