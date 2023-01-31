import random


def blackjack(blackjack_deck):
    # functions
    def points_count(fpoints, fdeck):
        searching_points = {"two": 2,
                            "three": 3,
                            "four": 4,
                            "five": 5,
                            "six": 6,
                            "seven": 7,
                            "eight": 8,
                            "nine": 9,
                            "ten": 10,
                            "jack": 10,
                            "queen": 10,
                            "king": 10,
                            "ace": 11}
        fpoints += searching_points[fdeck[-1][2]]
        # Ace gives 11 or 1 points
        how_many_aces = 0
        how_many_used_aces = 0
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
            choice = input("print \"yes\" or \"no\"\n")
            # First letter must be "Y" or "y" in order to game will be continued
            if not choice.startswith("y") or choice.startswith("Y"):
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
