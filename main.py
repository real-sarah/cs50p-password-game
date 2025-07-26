import streamlit as st
from api import get_top_track

def main():

    st.title("Welcome to the Password Game")

    if "password" not in st.session_state:
        st.session_state.password = ""

    artist = st.text_input("Enter the artist name: ")
    if artist:
        return_val = get_top_track(artist)
        if return_val != "Artist not found or top tracks not available" and return_val != "API request failed":
            st.success(f"Top song of {artist.upper()} is {return_val}")
            st.session_state.password = return_val.lower()
        else:
            st.error(return_val)

    st.write(st.session_state.password)





if __name__ == "__main__":
    main()
