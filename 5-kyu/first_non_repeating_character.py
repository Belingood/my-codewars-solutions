"""
Write a function that takes a string input, and returns the first character
that is not repeated anywhere in the string.
For example, if given the input "stress", the function should return 't',
since the letter t only occurs once in the string, and occurs first in the string.
As an added challenge, upper- and lowercase characters are considered the same character,
but the function should return the correct case for the initial character. For example,
the input "sTreSS" should return "T".
If a string contains only repeating characters, return an empty string ("");
Note: despite its name in some languages, your function should handle any Unicode codepoint:

"@#@@*"    --> "#"
"かか何"   --> "何"
"🐐🦊🐐" --> "🦊"
"""


def first_non_repeating_letter(s: str) -> str:

    for ch in s:

        if s.count(ch.lower()) + s.count(ch.upper()) - (not ch.isalpha()) == 1:
            return ch

    return ''


if __name__ == '__main__':
    print(first_non_repeating_letter('o70Dj8YvhNdBAoB8QoaJs l5qvRdjXL;ASP5;0q0gTGimc0Np::q:A5'))
