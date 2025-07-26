# PASSWORD GAME
#### Video Demo:  <URL HERE>
#### Description: 
This is a simple Python project inspired by neal.fun's "The Password Game".
The project aims at validating a given string against a set of instructions, passing all of which will lead to the game being defeated. 
The game makes uses of Streamlit not just so that it can be hosted, but also to take advantage of the way Streamlit behaves. 
Streamlit makes use of "top-down, always rerun" approach, through which the string entered by the user can repeatedly be checked against the instruction set, without using loops for repitition.
To give the game a starting point, user is asked for the name of an artist, and then the most streamed song by that artist is fetched via API calls. Last.fm's API is used here.
