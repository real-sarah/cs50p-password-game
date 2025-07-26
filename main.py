import streamlit as st
from api import get_top_track
from validate import validate

def main():

    st.title("Welcome to the Password Game")

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

    if st.session_state.game_started:
        password = st.text_input("Your Password is: ", value = st.session_state.password)
        if password:
            st.write(validate(password))




def get_artist():
    artist = st.text_input("Enter the artist name: ")
    return_val = ""
    if artist:
        return_val = get_top_track(artist)
        if return_val != "Artist not found or top tracks not available" and return_val != "API request failed":
            st.success(f"Top song of {artist} is {return_val}")
        else:
            st.error(return_val)

    return return_val







if __name__ == "__main__":
    main()
