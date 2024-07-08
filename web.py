import streamlit as st

import function

todos = function.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todos(todos)



st.title("My Todo App ")
st.subheader("Productivity app")

# to get todos
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    # to removetodo
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# to add todos
st.text_input(label="", placeholder="Enter a to do", on_change=add_todo,
key="new_todo")



