import streamlit as st
from agent.planner import plan_tasks
from agent.memory import memory
from agent.tools import save_tasks, load_tasks

st.set_page_config(page_title="TaskPilot", page_icon="🧠")
st.title("🧠 TaskPilot – Your AI Task Manager")

user_input = st.text_input("Describe your task:", placeholder="e.g. Prepare for math exam next Friday")

if st.button("Plan Task") and user_input:
    subtasks = plan_tasks(user_input, memory)
    save_tasks(subtasks)
    st.success("Here's your plan:")
    for idx, task in enumerate(subtasks, 1):
        st.write(f"{idx}. {task}")

if st.button("View All Tasks"):
    all_tasks = load_tasks()
    if all_tasks:
        st.subheader("📋 Current Task List:")
        for idx, task in enumerate(all_tasks, 1):
            st.write(f"{idx}. {task}")
    else:
        st.info("No tasks found.")
