import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def visualizer(player1, player2, winner):
    """
    (str, str, int) -> None
    This function visualizes the choices from player 1 and 2 and displays the winner.

    Example:
        rpsls_visualizer('Rock', 'Paper', 1)
        rpsls_visualizer('Scissors', 'Rock', 1)
    """

    # Setup figure
    fig = plt.figure(figsize=(20, 6))
    ax1 = plt.subplot2grid((1, 3), (0, 0))
    ax2 = plt.subplot2grid((1, 3), (0, 1))
    ax3 = plt.subplot2grid((1, 3), (0, 2))

    # Player 1
    player1_image = mpimg.imread('images/{}.png'.format(player1.lower()))
    ax1.set_title('Player 1', fontsize=24, y=1.05)
    ax1.imshow(player1_image)
    ax1.axes.xaxis.set_visible(False)
    ax1.axes.yaxis.set_visible(False)
    if winner == -1:
        [x.set_linewidth(10) for x in ax1.spines.values()]
        [x.set_color('green') for x in ax1.spines.values()]
    elif winner == 1:
        [x.set_linewidth(10) for x in ax1.spines.values()]
        [x.set_color('red') for x in ax1.spines.values()]
    else:
        [x.set_linewidth(10) for x in ax1.spines.values()]
        [x.set_color('yellow') for x in ax1.spines.values()]

    # VS
    player1_image = mpimg.imread('images/vs.png')
    ax2.imshow(player1_image)
    ax2.axes.xaxis.set_visible(False)
    ax2.axes.yaxis.set_visible(False)
    ax2.axis('off')

    # Player 2
    player2_image = mpimg.imread('images/{}.png'.format(player2.lower()))
    ax3.set_title('Computer', fontsize=24, y=1.05)
    ax3.imshow(player2_image)
    ax3.axes.xaxis.set_visible(False)
    ax3.axes.yaxis.set_visible(False)
    if winner == 1:
        [x.set_linewidth(10) for x in ax3.spines.values()]
        [x.set_color('green') for x in ax3.spines.values()]
    elif winner == -1:
        [x.set_linewidth(10) for x in ax3.spines.values()]
        [x.set_color('red') for x in ax3.spines.values()]
    else:
        [x.set_linewidth(10) for x in ax3.spines.values()]
        [x.set_color('yellow') for x in ax3.spines.values()]

def run_tests_coffee_machine(coffee_machine):
    """Runs test cases for the coffee_machine function and calculates the score.

    Returns:
    int: The total score based on correct responses."""

    test_cases = [
        (1, "You have selected Espresso. That will be $3. Enjoy your drink!"),
        (2, "You have selected Latte. That will be $4. Enjoy your drink!"),
        (3, "You have selected Cappuccino. That will be $5. Enjoy your drink!"),
        (4, "Thank you! Have a great day and stay caffeinated!"),
        (5, "Invalid selection. Please select a valid option.")
    ]

    score = 0
    total_tests = len(test_cases)

    for option, expected in test_cases:
        result = coffee_machine(option)
        if result == expected:
            score += 1
            print(f"Test case {option}: ✅ Passed")
        else:
            print(f"Test case {option}: ❌ Failed (Expected: '{expected}', Got: '{result}')")

    print(f"\nTest results: {score}/{total_tests} correct answers.")

def run_tests_select_winner(select_winner):
    """Runs test cases for the select_winner function and calculates the score.

    Returns:
    int: The total score based on correct responses."""

    test_cases = [
        (('rock', 'scissors'), -1),   # Rock crushes Scissors
        (('scissors', 'rock'), 1),    # Rock crushes Scissors
        (('paper', 'rock'), -1),      # Paper covers Rock
        (('rock', 'paper'), 1),       # Paper covers Rock
        (('lizard', 'spock'), -1),    # Lizard poisons Spock
        (('spock', 'lizard'), 1),     # Lizard poisons Spock
        (('spock', 'scissors'), -1),  # Spock smashes Scissors
        (('scissors', 'spock'), 1),   # Spock smashes Scissors
        (('paper', 'spock'), 1),      # Paper disproves Spock
        (('spock', 'paper'), -1),     # Paper disproves Spock
        (('rock', 'rock'), 0),        # Tie
        (('lizard', 'lizard'), 0),    # Tie
    ]

    score = 0
    total_tests = len(test_cases)

    for inputs, expected in test_cases:
        result = select_winner(inputs[0], inputs[1])
        if result == expected:
            score += 1
            print(f"Test case {inputs}: ✅ Passed")
        else:
            print(f"Test case {inputs}: ❌ Failed (Expected: {expected}, Got: {result})")

    print(f"\nTest results: {score}/{total_tests} correct answers.")

def run_tests_rps_winner(rps_winner):
    """Runs test cases for the rps_winner function and calculates the score.

    Returns:
    int: The total score based on correct responses.
    """

    test_cases = [
        (('rock', 'scissors'), -1),  # rock beats scissors
        (('scissors', 'paper'), -1),  # scissors beats paper
        (('paper', 'rock'), -1),  # paper beats rock
        (('rock', 'rock'), 0),  # tie condition
        (('paper', 'paper'), 0),  # tie condition
        (('scissors', 'scissors'), 0),  # tie condition
        (('scissors', 'rock'), 1),  # rock beats scissors
        (('rock', 'paper'), 1),  # paper beats rock
    ]

    score = 0
    total_tests = len(test_cases)

    for inputs, expected in test_cases:
        result = rps_winner(*inputs)
        if result == expected:
            score += 1
            print(f"Test case {inputs}: ✅ Passed")
        else:
            print(f"Test case {inputs}: ❌ Failed (Expected: '{expected}', Got: '{result}')")

    print(f"\nTest results: {score}/{total_tests} correct answers.")

def run_tests_rpsls_winner(rpsls_winner):
    """Runs test cases for the rpsls_winner function and calculates the score.

    Returns:
    int: The total score based on correct responses.
    """

    test_cases = [
        # Test cases where input1 wins (-1)
        (('rock', 'scissors'), -1),
        (('paper', 'rock'), -1),
        (('scissors', 'paper'), -1),
        (('lizard', 'spock'), -1),
        (('spock', 'rock'), -1),

        # Test cases where input2 wins (1)
        (('scissors', 'rock'), 1),
        (('rock', 'paper'), 1),
        (('paper', 'scissors'), 1),
        (('spock', 'lizard'), 1),
        (('lizard', 'rock'), 1),

        # Test cases for ties (0)
        (('rock', 'rock'), 0),
        (('paper', 'paper'), 0),
        (('scissors', 'scissors'), 0),
        (('lizard', 'lizard'), 0),
        (('spock', 'spock'), 0)
    ]

    score = 0
    total_tests = len(test_cases)

    for inputs, expected in test_cases:
        result = rpsls_winner(*inputs)
        if result == expected:
            score += 1
            print(f"Test case {inputs}: ✅ Passed")
        else:
            print(f"Test case {inputs}: ❌ Failed (Expected: '{expected}', Got: '{result}')")

    print(f"\nTest results: {score}/{total_tests} correct answers.")
