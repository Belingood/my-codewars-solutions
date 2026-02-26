"""
Background
We all know about "balancing parentheses" (plus brackets, braces and chevrons) and even balancing characters that are identical.
Read that last sentence again, I balanced different characters and identical characters twice and you didn't even notice... :)
Kata
Your challenge in this kata is to write a function to validate that a supplied string is balanced.
You must determine if all that is open is then closed, and nothing is closed which is not already open!
You will be given a string to validate, and a second string, where each pair of characters defines an
opening and closing sequence that needs balancing.
You may assume that the second string always has an even number of characters.

Examples
// In this case '(' opens a section, and ')' closes a section
("(Sensei says yes!)", "()")       => true
("(Sensei says no!", "()")         => false

// In this case '(' and '[' open a section, while ')' and ']' close a section
("(Sensei [says] yes!)", "()[]")   => true
("(Sensei [says) no!]", "()[]")    => false

// In this case a single quote (') both opens and closes a section
("Sensei says 'yes'!", "''")       => true
("Sensei say's no!", "''")         => false
"""


def is_balanced(source: str, caps: str) -> bool:
    caps_from_source: str = ''.join(filter(lambda x: x in caps, source))
    new_ln: int = 0

    while new_ln != len(caps_from_source):
        new_ln: int = len(caps_from_source)
        for i in range(0, len(caps), 2):
            caps_from_source: str = caps_from_source.replace(caps[i: i + 2], '')

    return False if new_ln else True


if __name__ == '__main__':
    print(is_balanced("(Sensei [says] yes!)", "()[]"))
    print(is_balanced("(Sensei [says) no!]", "()[]"))

# The function determines whether a sequence of opening and closing symbols is properly balanced.
# First, it extracts from the input string (source) only those characters that are present in the caps string.
# This produces a filtered string containing only relevant symbols (such as brackets), while preserving their original order.
# Next, the function repeatedly removes valid adjacent pairs. It assumes that caps defines valid opening–closing pairs
# in consecutive two-character groups (e.g., "()", "[]", "{}"). During each iteration of the loop, it removes
# all occurrences of these valid pairs from the filtered string using str.replace().
# This process continues until the length of the string stops changing, meaning no more valid adjacent pairs can be removed.
# Finally, the function returns:
# True if the string is empty (all symbols were successfully matched and removed),
# False otherwise (some unmatched or improperly ordered symbols remain).
# Overall, the algorithm validates balance by repeatedly eliminating correctly matched adjacent pairs until no further
# reductions are possible.
