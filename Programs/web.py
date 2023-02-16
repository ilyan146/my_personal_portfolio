import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo_input"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my to do app.")
st.write("This app is to increase your productivity!")

for i in todos:
    st.checkbox(i)

st.text_input(label="1", placeholder="Enter a todo....",
              on_change=add_todo, key="new_todo_input",label_visibility="hidden")

st.session_state
print("Hello")