from main import blackjack_score
import pytest


def test_score_for_pair_of_number_cards():
    # Arrange
    hand = [3, 4]
    expected_result = 7

    # Act
    score = blackjack_score(hand)

    # Assert <-- Write assert statement here
    # expected_result =7
    assert score == expected_result


def test_facecards_have_values_calculated_correctly():
    # Arrange
    hand = ['Ace', 'King', 'Queen']
    expected_result = 21

    # Act
    score = blackjack_score(hand)

    # Assert <-- Write assert statement here

    assert score == expected_result


def test_calculates_aces_as_11_where_it_does_not_go_over_21():
    # Arrange
    hand = ['Ace', 9]
    expected_result = 20

    # Act
    score = blackjack_score(hand)

    # Assert <-- Write assert statement here

    assert score == expected_result


def test_calculates_aces_as_1_where_11_would_bust():
  # Arrange
    hand = ['Ace', 'King', 'Jack']
    expected_result = 21

    # Act
    score = blackjack_score(hand)

    # Assert <-- Write assert statement here

    assert score == expected_result


def test_returns_invalid_for_invalid_cards():
    # Arrange
    hand = ['Joker', 'King', 'Jack']

    # Except
    with pytest.raises(ValueError, match="Joker Unknown card in hand"):
        blackjack_score(hand)


def test_returns_invalid_for_list_length_greater_than_5():
    # Arrange
    hand = [6, 'King', 'Jack', 2, 3, 8]

    # Except
    with pytest.raises(ValueError, match="6 cards in hand"):
        blackjack_score(hand)


def test_returns_bust_for_scores_over_21():
    # Arrange
    hand = ['Ace', 'King', 'Jack', 'Queen']

    # Except
    with pytest.raises(ValueError, match="Bust 31"):
        blackjack_score(hand)


def test_returns_12_for_ace_ace_king():
    hand = ['Ace', 'Ace', 'King']
    expected_result = 12

    # Act
    score = blackjack_score(hand)

    # Assert <-- Write assert statement here
    assert score == expected_result


def test_returns_14_for_ace_ace_ace_ace():
    hand = ['Ace', 'Ace', 'Ace', 'Ace']
    expected_result = 14

    # Act
    score = blackjack_score(hand)

    # Assert <-- Write assert statement here
    assert score == expected_result
