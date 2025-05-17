"""
950. Reveal Cards In Increasing Order
You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].
You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1. Otherwise, stop. Return an ordering of the deck that would reveal the cards in increasing order.
Note that the first entry in the answer is considered to be the top of the deck.
"""


from typing import List

class Solution(object):
  def deckRevealIncreasing(self, deck: List[int]) -> List[int]:
    """
    Step 1. Figure out the order for us to take out values
    Step 2. Rearrange the values by using the order.
    """
    q = deque()
    n = len(deck)

    for i in range(n):
      q.append(i)

    order = []

    while len(q) > 0:
      first_value = q.popleft()
      order.append(first_value)
      if len(q) > 0:
        second_value = q.popleft()
        q.append(second_value)

    sorted_deck = sorted(deck)
    result = [0] * len(deck)
    for index,value in zip(order, sorted_deck):
      result[index] = value
    return result