import streamlit as st
import modules.functions as functions

def add_todo():
        n_todo = st.session_state["new_todo"]+"\n"
        #todos = functions.get_todos()
        todos.append(n_todo)
        functions.write_todos(todos)

todos = functions.get_todos()

st.title("My TO DO app")
st.subheader("Description")
st.write("Simple text")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input("Enter a TODO:", placeholder="HINT", on_change=add_todo, key='new_todo')

#st.session_state