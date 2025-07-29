# PASSWORD GAME
#### URL: https://cs50p-password-game.streamlit.app/
#### Video Demo:  https://www.youtube.com/watch?v=I6nj65Ti7p8
#### Description: 
This is a simple Python project inspired by neal.fun's "The Password Game".
The project aims at validating a given string against a set of instructions, passing all of which will lead to the game being defeated. 
The game makes uses of **Streamlit** not just so that it can be hosted, but also to take advantage of the way Streamlit behaves. 
Streamlit makes use of "*top-down, always rerun*" approach, through which the string entered by the user can repeatedly be checked against the instruction set, without using loops for repitition.
To give the game a starting point, user is asked for the name of an artist, and then the most streamed song by that artist is fetched via API calls. **Last.fm**'s API is used here.

Then once we have our starting point, the user's string is validated against the following set of instructions:
```
Password should contain the song's name in snake_case.
For example: 'I Want It That Way' becomes i_want_it_that_way.

Password should be between 8 and 50 characters long.

Password should not contain any whitespace characters (spaces, tabs, or newlines).

Password should contain at least one uppercase letter.

Password must contain at least two vowels in different cases (e.g., 'a' and 'E').

Password should contain at least one number.

The sum of all numbers in the password must be equal to 37.

Password must contain at least one special character (e.g., !, @, #, etc.).

Password should contain at least three Morse Code characters (., -, /).
Note: No whitespaces allowed in Morse symbols.

Password must contain at least one Roman numeral (e.g., I, V, X, L, C, D, M).

Password should contain at least one prime number (e.g., 2, 3, 5, 7, 11, etc.).

Password must contain at least one colour of the rainbow
(Red, Orange, Yellow, Green, Blue, Indigo, Violet).

Password must contain a colour in hex format – #RRGGBB
Example: #1A2B3C
```

The validation is done by making use of **regular expressions** wherever possible. Each instruction is broken down into **checker** functions that individually check one instruction.
All these functions are then chained inside of a bigger function called **validate**. As soon as a string is entered, validate function checks against each instruction from top to bottom, and whenever it finds the first mismatch, an error message corresponding to the mismatch is displayed.
This process is repeated till the string passes all of the instructions, after which a success message is displayed. 
To add some flavour to the error messages, **choice** function from Python's inbuilt **random** library is used to display different exclaimation expressions among "Oh no!", "Uh oh", "Oops" and the like.




