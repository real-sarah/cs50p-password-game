import streamlit as st
from api import get_top_track
import validate
from emoji import emojize
from checkers import snake_case


def main():
    st.title(emojize(":chequered_flag:Password Game"))
    subheader = emojize(":video_game: Welcome to the Password Game")
    st.header(subheader)
    st.subheader(
        "Firstly enter the name of your favourite artist. The top song from that artist will be looked up, and that will give us a starting point. Further, follow the instruction set to beat the game"
    )

    show_more = st.toggle("Click here to display the instructions")

    if show_more:
        st.write(
            "1. Password should contain song's name in snake_case. For example, 'I Want It That Way' becomes 'i_want_it_that_that_way'\n"
            + "2. Password should be between 8 and 50 characters long.\n"
            + "3. Password should not contain any whitespace characters (spaces, tabs, newlines).\n"
            + "4. Password should contain at least one uppercase letter.\n"
            + "5. Password must contain at least two vowels in different cases.\n"
            + "6. Password should contain at least one number\n"
            + "7. Sum of all numbers in the password must be equal to 37\n"
            + "8. Password must contain at least one special character.\n"
            + "9. Password should contain at least three Morse Code characters ('.', '-', '/') (No whitespaces allowed).\n"
            + "10. Password must contain at least one Roman numeral.\n"
            + "11. Password should contain at least one prime number.\n"
            + "12. Password must contain at least one colour of the rainbow.\n"
            + "13. Password must contain a colour in #RRGGBB format."
        )

    if "password" not in st.session_state:
        st.session_state.password = ""
    if "game_started" not in st.session_state:
        st.session_state.game_started = False

    if not st.session_state.password:
        password = get_artist()

        if password:
            st.session_state.password = password

    if st.session_state.password and not st.session_state.game_started:
        st.write(f"Your Password Game will begin with: {st.session_state.password}")
        if st.button("Start Game"):
            st.session_state.game_started = True

    song = snake_case(st.session_state.password)
    if st.session_state.game_started:
        password = st.text_input("Your Password is: ", value=st.session_state.password)
        if password:
            validate.validate(password, song)
        if st.button("End Game"):
            st.write("Nice meeting you!")
            st.stop()


def get_artist():
    artist = st.text_input("Enter the artist name: ")
    return_val = ""
    if artist:
        return_val = get_top_track(artist)
        if (
            return_val != "Artist not found or top tracks not available"
            and return_val != "API request failed"
        ):
            st.success(f"Top song of {artist} is {return_val}")
        else:
            st.error(return_val)

    return return_val


if __name__ == "__main__":
    main()
