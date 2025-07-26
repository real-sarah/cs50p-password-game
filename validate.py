from random import choice
from checkers import *
import streamlit as st

error = [
    "Password should contain song's name in snake_case",
    "Password should be between 8 and 50 characters long",
    "Password must not contain any whitespace characters",
    "Password must contain at least one uppercase letter",
    "Password must contain at least two vowels in different cases",
    "Password must contain at least one number",
    "Sum of all numbers in the password must be equal to 37",
    "Password must contain at least one special character",
    "Password must contain at least three Morse Code characters",
    "Password must contain at least one Roman numeral",
    "Password should contain at least one prime number",
    "Password must contain at least one colour of the rainbow",
    "Password must contain a colour in #RRGGBB format",
]

expression = ["Oops", "Uh-oh", "Oh-no", "Whoops", "Wait up", "No, no"]
punctuation = ["..", "!"]

def formatt(num):
    return f"{choice(expression)} {choice(punctuation)} {error[num]}"


def validate(password, song):
    song = snake_case(song)
    if checker0(song, password) == 100:
        if checker1(password) == 100:
            if checker2(password) == 100:
                if checker3(password) == 100:
                    if checker4(password) == 100:
                        if checker5(password) == 100:
                            if checker6(password) == 100:
                                if checker7(password) == 100:
                                    if checker8(password) == 100:
                                        if checker9(password) == 100:
                                            if checker10(password) == 100:
                                                if checker11(password) == 100:
                                                    if checker12(password) == 100:
                                                        st.success("Password Game Defeated")
                                                        st.write("You may use this password anywhere, we do not store passwords.")
                                                    else:
                                                        x = formatt(12)
                                                        st.error(x)
                                                else:
                                                    x = formatt(11)
                                                    st.error(x)
                                            else:
                                                x = formatt(10)
                                                st.error(x)
                                        else:
                                            x = formatt(9)
                                            st.error(x)
                                    else:
                                        x = formatt(8)
                                        st.error(x)
                                else:
                                    x = formatt(7)
                                    st.error(x)
                            else:
                                x = formatt(6)
                                st.error(x)
                        else:
                            x = formatt(5)
                            st.error(x)
                    else:
                        x = formatt(4)
                        st.error(x)
                else:
                    x = formatt(3)
                    st.error(x)
            else:
                x = formatt(2)
                st.error(x)
        else:
            x = formatt(1)
            st.error(x)
    else:
        x = formatt(0)
        st.error(x)