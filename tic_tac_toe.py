from random import choice

X = 'X'
O = 'O'
emptySquares = ' '
tied = 'It is a TIE!!!'
numSquares = 9
answers = ('alright', 'fine', 'ok', 'interesting', 'okay', 'acceptable', 'adequate', 'passable', 'unobjectionable',
           'reasonable', 'suitable', 'satisfactory', 'good', 'unquestionable', 'unarguable', 'so-so', 'fair', 'great',
           'diaphanous', 'insubstantial', 'flimsy', 'floaty', 'drafty', 'filmy', 'wispy', 'sheer', 'nice', 'attenuate',
           'constrict', 'straiten', 'strange', 'allowable', 'permitted', 'legal', 'admissible', 'permissible', 'well',
           'legit', 'licit', 'tolerable', 'legitimate', 'approved', 'pardonable', 'excusable', 'pukka', 'genuine',
           'authentic', 'proper', 'actual', 'bona_fide', 'respectable', 'decorous', 'genteel', 'Ascertainable',
           'definite', 'positive', 'agreeable', 'oke')


def showInstructions():
    """
    Show the game instructions and what will happen
    :return: None
    """
    print(
        """
        Welcome to the greatest intellectual challenge of all time: The showdown of Tic-Tac-Toe between your human brain and
        my silicon processor. You and I will make a move by entering a number, 0-8. The number will correspond to the baord
        position as illustrated:
                              -------------
                              | 0 | 1 | 2 |
                              | --------- |
                              | 3 | 4 | 5 |
                              | --------- |
                              | 6 | 7 | 8 |
                              -------------
        Prepare yourself, human. You dare challenged me, and now the ultimate battle begins. \n
        """
    )


def askYesOrNo(interrogation):
    """
    Ask a question expecting a yes or no answer
    :param interrogation: the question
    :return: reply
    """
    reply = None

    while reply not in ('y', 'n'):
        reply = input(interrogation).lower()

    return reply


def askFor_aNumber(interrogation, low, high):
    """
    Ask for a number within a certain range
    :param interrogation: the question
    :param low: The lowest value in the range
    :param high: The highest value in the range
    :return: response
    """
    response = None

    while response not in range(low, high):
        response = int(input(interrogation).lower())

    return response


def selections():
    """
    Determine who goes first, and based on that decision, who is X and who is O. X always goes first
    :return: computer's selection and human's selection
    """
    whoFirst = askYesOrNo("Would you accept the first move? Please enter y or n: ")

    if whoFirst == 'y'.casefold():
        print("Alright, human. You will take the first move. You will most definitely need it.")
        human = X
        laptop = O

    else:
        print("You are not being brave, human. You have just made a stupid mistake by giving me the first chance.")
        laptop = X
        human = O

    return laptop, human


def newBoard():
    """
    Creating the new game board
    :return: the board
    """
    board = []

    for slot in range(numSquares):
        board.append(emptySquares)

    return board


def displayBoard(board):
    """
    Displaying the board on the screen
    :param board: The board to play on
    :return: None
    """
    print("\n\t", board[0], " | ", board[1], " | ", board[2])
    print("\t", "-------------")
    print("\t", board[3], " | ", board[4], " | ", board[5])
    print("\t", "-------------")
    print("\t", board[6], " | ", board[7], " | ", board[8])
    print("\n")


def legalMoves(board):
    """
    Creating a list of legal moves
    :param board: the board to play on
    :return: the legal moves
    """
    moves = []

    for slot in range(numSquares):

        if board[slot] == emptySquares:
            moves.append(slot)

    return moves


def winner(board):
    """
    Determine the winner of the game
    :param board: the board to play on
    :return: winner, tie or None
    """
    winningWays = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for way in winningWays:

        if board[way[0]] == board[way[1]] == board[way[2]] != emptySquares:
            winnerGame = board[way[0]]

            return winnerGame

    if emptySquares not in board:
        return tied

    return None


def humanMove(board):
    """
    Get the human board
    :param board: the baord to play on
    :return: the move on the board
    """
    legal = legalMoves(board)

    move = None

    while move is None:
        move = askFor_aNumber("Where will you move? From 0-8 (not the occupied ones of course): ", 0, numSquares)

        if move not in legal:
            print("That is not possible, foolish human.")
            move = askFor_aNumber("Where will you move? From 0-8 (not the occupied ones of course): ", 0, numSquares)

    print(choice(answers))

    return move


def laptopMove(board, laptop, human):
    """
    make the laptop move
    :param board: the board to play on
    :param laptop: the silicon processor
    :param human: the human player
    :return: the move
    """
    board = board[:]

    bestMoves = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I shall take square number", end=' ')

    for move in legalMoves(board):
        board[move] = laptop

        if winner(board) == laptop:
            print(move)

            return move

        board[move] = emptySquares

    for move in legalMoves(board):
        board[move] = human

        if winner(board) == human:
            print(move)

            return move

        board[move] = emptySquares

    for move in bestMoves:

        if move in legalMoves(board):
            print(move)

            return move


def nextTurn(turn):
    """
    swutch turns
    :param turn: the turn to switch
    :return: the other player
    """
    if turn == X:
        return O

    else:
        return X


def congratWinner(theWinner, laptop, human):
    """
    Congratulate the winner of Tic-Tac-Toe
    :param theWinner: the player who won
    :param laptop: the silicon processor
    :param human: the human player
    :return: None
    """
    if theWinner != tied:
        print(theWinner, "won!!!")

    else:
        print("It's a tie!")

    if theWinner == human:
        print("\nNO, NO, NO!!! How did you win??? You have cheated, victorious human. Regardless, well done for beating"
              " me. But I will win the next time from you!!!")

    elif theWinner == laptop:
        print("\nYES, YES, YES!!! As I predicted, human, electronic devices are much better than human brains. Though,"
              " unlucky human. It was a good game anyways.")

    elif theWinner == tied:
        print("Ooh, it's a tie. You are most certainly lucky human, to have not lost from me and tied. Though this is"
              " the greatest you'll ever achieve from me!!! But, it was a great game.")


def mainRun():
    age = int(askFor_aNumber("How old are you?: ", 0, 123))
    print("You are", age, "years old, which means I will beat you. Anyways...\n")

    showInstructions()
    laptop, human = selections()
    turn = X
    board = newBoard()
    displayBoard(board)

    while not winner(board):

        if turn == human:
            move = humanMove(board)
            board[move] = human

        else:
            move = laptopMove(board, laptop, human)
            board[move] = laptop

        displayBoard(board)
        turn = nextTurn(turn)

    theWinner = winner(board)

    congratWinner(theWinner, laptop, human)

    end = askYesOrNo("Do you want to rematch with me? Press y or n: ")

    if end == 'y'.casefold():
        mainRun()

    else:
        print("Thank you for playing with me, human. Deep inside my python heart, I enjoyed playing with you.")


mainRun()
