import streamlit as st

def main():
    st.title("Simple Hello App")
    st.write("Welcome to my first Streamlit app!")

    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, {name}! Welcome to Streamlit!")

if __name__ == "__main__":
    main()