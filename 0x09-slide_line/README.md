# 0x09. 2048 (single line)

- The goal of this task is to reproduce the 2048 game mechanics on a single horizontal line.

- Given an array of integers, we want to be able to slide & merge it to the left or to the right. Identical numbers, if they are contiguous or separated by zeros, should be merged

### Pseudocode

 - Check for null and invalid direction.
 - We'll need to loop through the array in the opposite of the given direction
 - and add any same numbers together, while replacing all zeroes with non-
 - zeroes.
 - We only want to add numbers once, so increment the previous index variable
 - whenever this happens. Don't increment whenever replacing a zero so we can
 - check for pairs with the next number.
 - If the next number doesn't match previous, replace the index after previous
 - with next and increment previous.
 - We need variables for current and previous index, start and end indices,
 - and incrementer (1 or -1, depending left or right).
