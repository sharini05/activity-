
import streamlit as st
import random

def main():
    st.title("Guess the Number Game")

    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 10
        st.session_state.guesses = []

    st.write(f" You have {st.session_state.attempts} attempts left.")
    
    guess = st.number_input("Enter your guess:", min_value=10, max_value=99, step=1)

    if st.button("Submit Guess"):
        handle_guess(guess)

    if st.session_state.guesses:
        st.write("Your previous guesses:", st.session_state.guesses)

def handle_guess(guess):
    if guess:
        st.session_state.guesses.append(guess)
        st.session_state.attempts -= 1

        if guess < st.session_state.secret_number:
            st.warning(" Too low! Try again.")
        elif guess > st.session_state.secret_number:
            st.warning(" Too high! Try again.")
        else:
            st.success(" Congratulations! You've guessed the number!")
            

        if st.session_state.attempts == 0:
            st.error(f" Game Over! The secret number was {st.session_state.secret_number}.")
            

if __name__ == "__main__":
    main()