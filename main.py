VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']


def blackjack_score(hand):
    if len(hand) <= 1:
        raise ValueError(f'{len(hand)} cards in hand.')

    if len(hand) > 5:
        raise ValueError(f'{len(hand)} cards in hand.')

    for card in hand:
        if card not in VALID_CARDS:
            raise ValueError(f'{card} Unknown card in hand.')
    # we made a list to append non ace cards first.
    # if we have four aces and the king = 24, if king and four ace = 14
    order_the_hand = []
    for card in hand:
        if card != 'Ace':
            order_the_hand.append(card)

    for card in hand:
        if card == 'Ace':
            order_the_hand.append(card)

    score = 0
    for card in order_the_hand:
        if isinstance(card, str):
            if card == 'Ace':
                if score + 11 > 21:
                    score += 1
                else:
                    score += 11
            else:
                score += 10
        else:
            score += card

    if score > 21:
        raise ValueError(f"Bust {score}")

    return score
