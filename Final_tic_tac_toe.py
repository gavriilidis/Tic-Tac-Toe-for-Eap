# Original code Tic-Tac-Toe
# ΤΡΙΛΙΖΑ από τον Γαβριήλ Γαβριηλίδη
# ΣΘΕΤ-ΑΨΛ(Δ)
# 2η ΑΕ μέρος 2ο
# Python 3.10

import turtle
import random
import winsound

# Η μουσική του παιχνιδιού παίζει συνέχεια μέχρι να κλείσουμε το παράθυρο
winsound.PlaySound("background.wav", winsound.SND_LOOP + winsound.SND_ASYNC)


# Αν θέλουμε να παίξουμε ξανά στο τέλος υπάρχει επιλογή y/n. Αν η επιλογή είναι y, τρέχει game() και αρχίζει πάλι.
def game():
    # Το παράθυρο του παιχνιδιού
    wn = turtle.Screen()
    wn.setup(600, 600)
    wn.title("ΤΡΙΛΙΖΑ ΑΕ 2 Μέρος 2 Γαβριηλίδης Γαβριήλ")
    wn.bgcolor("black")
    wn.tracer(0)
    turtle.hideturtle()

    # Οι γραμμές που σχηματίζουν τη "δίεση" και με μικρά νούμερα δείχνουν τις θέσεις
    def board():
        turtle.pencolor("gray")
        turtle.speed(0)
        turtle.pensize(10)
        turtle.penup()
        turtle.goto(-160, 5)
        turtle.pendown()
        turtle.forward(320)
        turtle.penup()
        turtle.goto(-160, -105)
        turtle.pendown()
        turtle.forward(320)
        turtle.penup()
        turtle.goto(-55, -210)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(320)
        turtle.penup()
        turtle.goto(55, -210)
        turtle.pendown()
        turtle.forward(320)
        turtle.penup()
        turtle.color("yellow")
        turtle.pensize(4)
        turtle.goto(-158, -125)
        turtle.write(1, font=("Arial", 8, "normal"))
        turtle.penup()
        turtle.goto(-48, -125)
        turtle.pendown()
        turtle.write(2, font=("Arial", 8, "normal"))
        turtle.penup()
        turtle.goto(62, -125)
        turtle.pendown()
        turtle.write(3, font=("Arial", 8, "normal"))
        turtle.penup()
        turtle.goto(-158, -15)
        turtle.pendown()
        turtle.write(4, font=("Arial", 8, "normal"))
        turtle.penup()
        turtle.goto(-48, -15)
        turtle.pendown()
        turtle.write(5, font=("Arial", 8, "normal"))
        turtle.penup()
        turtle.goto(62, -15)
        turtle.pendown()
        turtle.write(6, font=("Arial", 8, "normal"))
        turtle.penup()
        turtle.goto(-158, 95)
        turtle.pendown()
        turtle.write(7, font=("Arial", 8, "normal"))
        turtle.penup()
        turtle.goto(-48, 95)
        turtle.pendown()
        turtle.write(8, font=("Arial", 8, "normal"))
        turtle.penup()
        turtle.goto(62, 95)
        turtle.pendown()
        turtle.write(9, font=("Arial", 8, "normal"))
        turtle.penup()

    # Σχεδιάζει το Χ
    def draw_x(x, y):
        turtle.pencolor("red")
        turtle.speed(5)
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x + 80, y - 80)
        turtle.penup()
        turtle.goto(x + 80, y)
        turtle.pendown()
        turtle.goto(x, y - 80)
        turtle.penup()

    # Σχεδιάζει το Ο
    def draw_o(x, y):
        turtle.color("blue")
        turtle.speed(0)
        turtle.pensize(5)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(40)
        turtle.penup()

    # Ανάλογα με τη θέση δείχνει που πρέπει να σχεδιαστεί το σωστό γράμμα
    def drawBoard(board):
        if board[1] == "X":
            draw_x(-150, -120)
        if board[2] == "X":
            draw_x(-40, -120)
        if board[3] == "X":
            draw_x(70, -120)
        if board[4] == "X":
            draw_x(-150, -10)
        if board[5] == "X":
            draw_x(-40, -10)
        if board[6] == "X":
            draw_x(70, -10)
        if board[7] == "X":
            draw_x(-150, 100)
        if board[8] == "X":
            draw_x(-40, 100)
        if board[9] == "X":
            draw_x(70, 100)
        if board[1] == "O":
            draw_o(-70, -160)
        if board[2] == "O":
            draw_o(40, -160)
        if board[3] == "O":
            draw_o(150, -160)
        if board[4] == "O":
            draw_o(-70, -50)
        if board[5] == "O":
            draw_o(40, -50)
        if board[6] == "O":
            draw_o(150, -50)
        if board[7] == "O":
            draw_o(-70, 60)
        if board[8] == "O":
            draw_o(40, 60)
        if board[9] == "O":
            draw_o(150, 60)

    # Ανοίγει παράθυρο και επιλέγει ο παίκτης Χ ή Ο (στα Αγγλικά)
    def inputPlayerLetter():
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            letter = turtle.textinput("Διάλεξε γράμμα", " Αγγλικό X ή O").upper()

        # The first element in the list is the player's letter; the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    # Ίδιο με τον αρχικό κώδικα
    def whoGoesFirst():
        # Randomly choose which player goes first.
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    # Ίδιο με τον αρχικό κώδικα
    def makeMove(board, letter, move):
        board[move] = letter

    # Ίδιο με τον αρχικό κώδικα
    def isWinner(bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use "bo" instead of "board" and "le" instead of "letter" so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # Across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # Across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # Across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # Down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # Down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # Down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # Diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # Diagonal

    # Ίδιο με τον αρχικό κώδικα
    def getBoardCopy(board):
        # Make a copy of the board list and return it.
        boardCopy = []
        for i in board:
            boardCopy.append(i)
        return boardCopy

    # Ίδιο με τον αρχικό κώδικα
    def isSpaceFree(board, move):
        # Return True if the passed move is free on the passed board.
        return board[move] == ' '

    # Ίδιο με τον αρχικό κώδικα
    def getPlayerMove(board):
        # Let the player enter their move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            move = turtle.textinput("Διάλεξε θέση", "1 ως 9",)
        return int(move)

    # Ίδιο με τον αρχικό κώδικα
    def chooseRandomMoveFromList(board, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    # Ίδιο με τον αρχικό κώδικα
    def getComputerMove(board, computerLetter):
        # Given a board and the computer's letter, determine where to move and return that move.
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        # Here is the algorithm for our Tic-Tac-Toe AI:
        # First, check if we can win in the next move.
        for i in range(1, 10):
            boardCopy = getBoardCopy(board)
            if isSpaceFree(boardCopy, i):
                makeMove(boardCopy, computerLetter, i)
                if isWinner(boardCopy, computerLetter):
                    return i

        # Check if the player could win on their next move and block them.
        for i in range(1, 10):
            boardCopy = getBoardCopy(board)
            if isSpaceFree(boardCopy, i):
                makeMove(boardCopy, playerLetter, i)
                if isWinner(boardCopy, playerLetter):
                    return i

        # Try to take one of the corners, if they are free.
        move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
        if move != None:
            return move

        # Try to take the center, if it is free.
        if isSpaceFree(board, 5):
            return 5

        # Move on one of the sides.
        return chooseRandomMoveFromList(board, [2, 4, 6, 8])

    # Ίδιο με τον αρχικό κώδικα
    def isBoardFull(board):
        # Return True if every space on the board has been taken. Otherwise, return False.
        for i in range(1, 10):
            if isSpaceFree(board, i):
                return False
        return True

    # Κύριο μέρος παιχνιδιού
    while True:
        # Εμφανίζει την σχεδιασμένη "δίεση"
        board()
        # Γράφει "ΤΡΙΛΙΖΑ" πάνω στο παράθυρο
        ttt = turtle.Turtle()
        ttt.hideturtle()
        ttt.color("yellow")
        ttt.shape("circle")
        ttt.speed(0)
        ttt.penup()
        ttt.goto(0, 210)
        ttt.write("ΤΡΙΛΙΖΑ", align="center", font=("Ariel", 40, "bold"))
        # Reset the board.
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                # Γράφει πάνω στην οθόνη πως παίζει ο παίκτης όταν είναι η σειρά του
                play = turtle.Turtle()
                play.hideturtle()
                play.color("white")
                play.shape("circle")
                play.speed(0)
                play.penup()
                play.goto(0, 160)
                play.write("Είναι η σειρά σου", align="center", font=("Ariel", 20, "bold"))

                # Player's turn
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    play.clear()
                    # Αν έχει κερδίσει ο παικτης γράφει πως κέρδισε
                    you_win = turtle.Turtle()
                    you_win.hideturtle()
                    you_win.color("white")
                    you_win.shape("circle")
                    you_win.speed(0)
                    you_win.penup()
                    you_win.goto(0, 160)
                    you_win.write("Κέρδισες!!!", align="center", font=("Ariel", 30, "bold"))
                    gameIsPlaying = False

                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        play.clear()
                        # Αν έχουν γράμμα όλες οι θέσεις και δεν υπάρχει νικητής, γράφει ισοπαλία
                        tie = turtle.Turtle()
                        tie.hideturtle()
                        tie.color("white")
                        tie.shape("circle")
                        tie.speed(0)
                        tie.penup()
                        tie.goto(0, 160)
                        tie.write("Ισοπαλία!", align="center", font=("Ariel", 30, "bold"))
                        gameIsPlaying = False

                    else:
                        play.clear()
                        turn = 'computer'

            else:
                # Computer's turn
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    # Αν έχει κερδίσει το κομπιούτερ γράφει έχασες
                    you_lost = turtle.Turtle()
                    you_lost.hideturtle()
                    you_lost.color("white")
                    you_lost.shape("circle")
                    you_lost.speed(0)
                    you_lost.penup()
                    you_lost.goto(0, 160)
                    you_lost.write("Έχασες!", align="center", font=("Ariel", 30, "bold"))
                    gameIsPlaying = False

                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        # Αν έχουν γράμμα όλες οι θέσεις και δεν υπάρχει νικητής, γράφει ισοπαλία
                        tie = turtle.Turtle()
                        tie.hideturtle()
                        tie.color("white")
                        tie.shape("circle")
                        tie.speed(0)
                        tie.penup()
                        tie.goto(0, 160)
                        tie.write("Ισοπαλία!", align="center", font=("Ariel", 30, "bold"))
                        gameIsPlaying = False

                    else:
                        turn = 'player'
        else:
            # Αφού τελείωσε η παρτίδα ρωτάει αν θέλει ο παίκτης να ξαναπαίξει
            restart = wn.textinput("Θες να παίξεις ξανά;", "(y/n)").lower()
            while restart != "y" or restart != "n":
                # συνεχίζει να ρωτάει αν δεν έχει δώσει ο παίκτης μια από τις δύο επιλογές
                restart = wn.textinput("Θες να παίξεις ξανά;", "(y/n)").lower()
                if restart == "y":
                    # Αν ο παίκτης επιλέξει να ξαναπαίξει, καθαρίζει το παράθυρο και ξεκινάει απο την αρχή
                    wn.clearscreen()
                    game()
                if restart == "n":
                    # Αν ο παίκτης επιλέξει να σταματήσει το παράθυρο κλείνει στο πρώτο click
                    turtle.Screen().exitonclick()

        wn.update()


game()