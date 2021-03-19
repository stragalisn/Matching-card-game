import random
import time

def populate(face_up = False):
    deck = []
    for i in range(1, 14):
        for h in range(4):
            if i == 1:
                if h == 0:
                    deck += [['A', '♥', i, 'A♥', face_up]]
                elif h == 1:
                    deck += [['A', '♣', i, 'A♣', face_up]]
                elif h == 2:
                    deck += [['A', '♦', i, 'A♦', face_up]]
                elif h == 3:
                    deck += [['A', '♠', i, 'A♠', face_up]]
            elif i <= 10 and i > 1:
                if h == 0:
                    deck += [[str(i), '♥', i, str(i) + '♥', face_up]]
                elif h == 1:
                    deck += [[str(i), '♣', i, str(i) + '♣', face_up]]
                elif h == 2:
                    deck += [[str(i), '♦', i, str(i) + '♦', face_up]]
                elif h == 3:
                    deck += [[str(i), '♠', i, str(i) + '♠', face_up]]
            elif i == 11:
                if h == 0:
                    deck += [['J', '♥', 10, 'J♥', face_up]]
                elif h == 1:
                    deck += [['J', '♣', 10, 'J♣', face_up]]
                elif h == 2:
                    deck += [['J', '♦', 10, 'J♦', face_up]]
                elif h == 3:
                    deck += [['J', '♠', 10, 'J♠', face_up]]
            elif i == 12:
                if h == 0:
                    deck += [['Q', '♥', 10, 'Q♥', face_up]]
                elif h == 1:
                    deck += [['Q', '♣', 10, 'Q♣', face_up]]
                elif h == 2:
                    deck += [['Q', '♦', 10, 'Q♦', face_up]]
                elif h == 3:
                    deck += [['Q', '♠', 10, 'Q♠', face_up]]
            elif i == 13:
                if h == 0:
                    deck += [['K', '♥', 10, 'K♥', face_up]]
                elif h == 1:
                    deck += [['K', '♣', 10, 'K♣', face_up]]
                elif h == 2:
                    deck += [['K', '♦', 10, 'K♦', face_up]]
                elif h == 3:
                    deck += [['K', '♠', 10, 'K♠', face_up]]
    return deck

def easy_game():
    deck = populate()[36:52]
    random.shuffle(deck)
    return deck

def medium_game():
    deck = populate()[:40]
    random.shuffle(deck)
    return deck

def ultimate_game():
    deck = populate()[:52]
    random.shuffle(deck)
    return deck

def easy_table(easy_deck):
    for i in range(1,5):
        if i == 1:
            print('  ', i, end = '   ')
        elif i < 4:
            print(i, end = '   ')
        else:
            print(i)
    c = 0
    for i in range(1,5):
        print(i, end = ' ')
        for j in range(4):
            if easy_deck[j+c][4] == True:
                if '10' in easy_deck[j+c][3]:
                    print(easy_deck[j+c][3], end = ' ')
                else:
                    print(easy_deck[j+c][3], end = '  ')
            else:
                print(' X', end = '  ')
        c += 4
        print('\n')
        
def medium_table(medium_deck):
    for i in range(1,11):
        if i == 1:
            print('  ', i, end = '   ')
        elif i < 10:
            print(i, end = '   ')
        else:
            print(i)
    c = 0
    for i in range(1,5):
        print(i, end = ' ')
        for j in range(10):
            if medium_deck[j+c][4] == True:
                if '10' in medium_deck[j+c][3]:
                    print(medium_deck[j+c][3], end = ' ')
                else:
                    print(medium_deck[j+c][3], end = '  ')
            else:
                print(' X', end = '  ')
        c += 10
        print('\n')
        
def ultimate_table(ultimate_deck):
    for i in range(1,14):
        if i == 1:
            print('  ', i, end = '   ')
        elif i ==10 or i == 11 or i == 12:
            print(i, end = '  ')
        elif i < 10:
            print(i, end = '   ')
        else:
            print(i)
    c = 0
    for i in range(1,5):
        print(i, end = ' ')
        for j in range(13):
            if ultimate_deck[j+c][4] == True:
                if '10' in ultimate_deck[j+c][3]:
                    print(ultimate_deck[j+c][3], end = ' ')
                else:
                    print(ultimate_deck[j+c][3], end = '  ')
            else:
                print(' X', end = '  ')
        c += 13
        print('\n')

def game_choice(game, table, number_of_players, points, counter):
    deck = game()
    table(deck)
    all_face_up = False
    found = []
    h = 1
    while all_face_up == False:
        first_card = 0
        second_card = 0
        j = 0
        while j != 2:
            player_row = int(input('Παίκτης ' + str(h) + ' :Εισάγετε τη σειρά που θελετε: '))
            while player_row not in range(1,5):
                print('Η σειρά που διαλέξατε είναι εκτός εμβέλειας')
                player_row = int(input('Παίκτης ' + str(h) + ' :Εισάγετε τη σειρά που θελετε: '))
            player_column = int(input('Παίκτης ' + str(h) + ' :Εισάγετε τη στήλη που θέλετε: '))
            while player_column not in range(1,counter):
                print('Η στήλη που διαλέξατε είναι εκτός εμβέλειας')
                player_column = int(input('Παίκτης ' + str(h) + ' :Εισάγετε τη στήλη που θέλετε: '))
            if player_row == 1:
                if j == 0:
                    first_card += player_column - player_row
                else:
                    second_card += player_column - player_row
            elif player_row == 2:
                if j == 0:
                    first_card += (player_column + counter) - player_row
                else:
                    second_card += (player_column + counter) - player_row
            elif player_row == 3:
                if j == 0:
                    first_card += (player_column + (counter * 2)) - player_row
                else:
                    second_card += (player_column + (counter * 2)) - player_row
            else:
                if j == 0:
                    first_card += (player_column + (counter * 3)) - player_row
                else:
                    second_card += (player_column + (counter * 3)) - player_row
            if deck[first_card][3] in found and j == 0:
                print('Η πρώτη κάρτα που διαλέξατε είναι ήδη ανοιχτή')
                first_card = 0
            elif deck[first_card][3] not in found and j == 0:
                deck[first_card][4] = True
                j += 1
                table(deck)
            elif first_card == second_card and j == 1:
                print('Διάλεξες την ίδια κάρτα δύο φορές')
                j = 0
                deck[first_card][4] = False
                first_card = 0
                second_card = 0
            elif deck[second_card][3] in found and j == 1:
                print('Η δεύτερη κάρτα που διαλέξατε είναι ήδη ανοιχτή')
                second_card = 0
            elif deck[second_card][3] not in found and j == 1:
                deck[second_card][4] = True
                j += 1
                table(deck)
        time.sleep(1)
        if (deck[first_card][0] == 'Q' and deck[second_card][0] == 'K') or (deck[second_card][0] == 'Q' and deck[first_card][0] == 'K'):
            print('Μπορεις να διαλέξεις και τρίτη κάρτα!')
            r = 0
            while r == 0:
                player_row = int(input('Παίκτης ' + str(h) + ' :Εισάγετε τη σειρά που θελετε: '))
                while player_row not in range(1,5):
                    print('Η σειρά που διαλέξατε είναι εκτός εμβέλειας')
                    player_row = int(input('Παίκτης ' + str(h) + ' :Εισάγετε τη σειρά που θελετε: '))
                player_column = int(input('Παίκτης ' + str(h) + ' :Εισάγετε τη στήλη που θέλετε: '))
                while player_column not in range(1,5):
                    print('Η στήλη που διαλέξατε είναι εκτός εμβέλειας')
                    player_column = int(input('Παίκτης ' + str(h) + ' :Εισάγετε τη στήλη που θέλετε: '))
                if player_row == 1:
                    third_card = player_column - player_row
                elif player_row == 2:
                    third_card = (player_column + counter) - player_row
                elif player_row == 3:
                    third_card = (player_column + (counter * 2)) - player_row
                else:
                    third_card += (player_column + (counter * 3)) - player_row
                if deck[third_card][3] in found:
                    print('Η κάρτα που διαλέξατε είναι ήδη ανοιχτή')
                elif third_card == first_card or third_card == second_card:
                    print('Διάλεξες την ίδια κάρτα δύο φορές')
                else:
                    r = 1
                    deck[third_card][4] = True
                    table(deck)
                    if deck[first_card][0] == deck[third_card][0]:
                        deck[second_card][4] = False
                        second_card = third_card
                    elif deck[second_card][0] == deck[third_card][0]:
                        deck[first_card][4] = False
                        first_card = third_card
                    else:
                        deck[third_card][4] = False
        if deck[first_card][0] == deck[second_card][0]:
            found.append(deck[first_card][3])
            found.append(deck[second_card][3])
            points[h - 1] += deck[first_card][2]
            print('Ο παίχτης ' + str(h) + ' βρήκε δύο κάρτες!!')
            print('Οι πόντοι του πλέον είναι ',points[h - 1])
            h += 1
            if deck[first_card][0] == 'J':
                print('Ο παίχτης ' + str(h - 1) + ' βρήκε δύο βαλέδες!!\nΠαίζει ξανα!!')
                h -= 1
            elif deck[first_card][0] == 'K':
                if (h - 1) != 3:
                    print('Ο παίχτης ' + str(h - 1) + ' βρήκε δύο ρηγάδες. Ο παίχτης ' + str(h) + ' χάνει τη σειρά του!')
                    h += 1
                else:
                    print('Ο παίχτης ' + str(h - 1) + ' βρήκε δύο ρηγάδες. Ο παίχτης 1 χάνει τη σειρά του!')
                    h = 2
        else:
            deck[first_card][4] = False
            deck[second_card][4] = False
            print('Δεν βρήκες δύο ίδιες')
            h += 1
        c = 0
        for i in range(16):
            if deck[i][4] == True:
                c += 1
        if c == 16:
            all_face_up = True
            maximum = -1
            for i in range(number_of_players):
                if points[i] > maximum:
                    maximum = points[i]
            c1 = 0
            for i in range(number_of_players):
                if points[i] == maximum:
                    c1 += 1
                    if c1 == 1:
                        player1 = str(i + 1)
                    elif c1 == 2:
                        player2 = str(i + 1)
                    elif c1 == 3:
                        player3 = str(i + 1)
            if c1 == 1:
                print('Κέρδισε ο παίχτης:', player1)
            elif c1 == 2:
                print('Υπάρχει ισοπαλία μεταξύ παιχτών:', player1, 'και', player2)
            elif c1 == 3:
                print('Υπάρχει ισοπαλία μεταξύ παιχτών:', player1, 'και', player2, 'και', player3)
            play_again = input('Θέλετε να ξαναπαίξετε; (Ν/Ο)')
            if play_again == 'Ν' or play_again == 'ν':
                game_start()
        else:
            table(deck)
        if h == number_of_players + 1:
            h = 1

def game_start():
    print('Καλωσήλθατε στο Matching Game')
    number_of_players = int(input('Δώστε αριθμό παικτών (2-3): '))
    while number_of_players not in range(2,4):
        print('Ο αριθμός παιχτών που δώσατε δεν είναι εφικτός!')
        number_of_players = int(input('Δώστε αριθμό παικτών (2-3): '))
    game_difficulty = int(input('Δώστε επίπεδο δυσκολίας Εύκολο (1), Μέτριο (2), Δύσκολο(3): '))
    while game_difficulty not in range(1,4):
        print('Το επίπεδο δυσκολίας που δώσατε δεν είναι εφικτό!')
        game_difficulty = int(input('Δώστε επίπεδο δυσκολίας Εύκολο (1), Μέτριο (2), Δύσκολο(3): '))
    points = []
    for i in range(number_of_players):
        points.append(0)
    if game_difficulty == 1:
        game_choice(easy_game, easy_table, number_of_players, points, 5)
    elif game_difficulty == 2:
        game_choice(medium_game, medium_table, number_of_players, points, 11)
    else:
        game_choice(ultimate_game, ultimate_table, number_of_players, points, 14)

game_start()
