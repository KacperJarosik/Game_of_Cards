import random


def blackjack(blackjack_deck):
    # functions
    def points_count(fpoints, fdeck):
        how_many_aces = 0
        how_many_used_aces = 0
        if fdeck[-1][2] == "two":
            fpoints += 2
        if fdeck[-1][2] == "three":
            fpoints += 3
        if fdeck[-1][2] == "four":
            fpoints += 4
        if fdeck[-1][2] == "five":
            fpoints += 5
        if fdeck[-1][2] == "six":
            fpoints += 6
        if fdeck[-1][2] == "seven":
            fpoints += 7
        if fdeck[-1][2] == "eight":
            fpoints += 8
        if fdeck[-1][2] == "nine":
            fpoints += 9
        if fdeck[-1][2] == "ten":
            fpoints += 10
        if fdeck[-1][2] == "jack":
            fpoints += 10
        if fdeck[-1][2] == "queen":
            fpoints += 10
        if fdeck[-1][2] == "king":
            fpoints += 10
        if fdeck[-1][2] == "ace":
            fpoints += 11
        # or 1
        if fpoints > 21:
            for k in range(len(fdeck)):
                if fdeck[k][2] == "ace":
                    how_many_aces += 1
                how_many_aces -= how_many_used_aces
            while how_many_aces > 0:
                fpoints -= 10
                how_many_aces -= 1
                how_many_used_aces += 1
                if fpoints <= 21:
                    break
        return fpoints

    # variables
    userdeck = []
    croupierdeck = []
    user_points = 0
    croupier_points = 0
    # Hello
    print("Hello in Black Jack Game!!!")
    # Croupier part
    while croupier_points < 17:
        randomly_index = random.randint(0, len(blackjack_deck) - 1)
        croupierdeck.append(blackjack_deck.pop(randomly_index))
        croupier_points = points_count(croupier_points, croupierdeck)
    # User part
    while user_points < 21:
        if not user_points == 0:
            print("Do you wanna take another card?")
            actually_choice = input("print \"yes\" or \"no\"\n")
            if actually_choice == "no":
                break
        randomly_index = random.randint(0, len(blackjack_deck))
        userdeck.append(blackjack_deck.pop(randomly_index))
        print("Croupier has %d cards. His first card:" % len(croupierdeck), croupierdeck[1], "\n")
        print("Your cards:", userdeck)
        user_points = points_count(user_points, userdeck)
        print("your actually points:", user_points, "\n")
    # result
    if user_points > 21:
        print("Defeat!!!")
    elif user_points == croupier_points:
        print("Draw!!!")
    elif user_points == 21:
        print("Black Jack\nHuge win!!!")
    elif user_points > croupier_points:
        print("win!!!")
    else:
        print("Croupier better than you\nDefeat!!!")
    print("Croupier points: ", croupier_points)
    print("Croupier cards: ", croupierdeck)
    return


# Games menu
if __name__ == '__main__':
    deck = []
    file = open("card_list", "r")
    for line in file.readlines():
        deck.append(tuple(line.split()))
    file.close()
    blackjack(deck[:-2])
