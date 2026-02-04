import streamlit as st

st.title("Simple CRUD App")

# -------------------------
# Temporary storage (list)
# -------------------------
if "students" not in st.session_state:
    st.session_state.students = []


menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)


# -------------------------
# CREATE
# -------------------------
if choice == "Create":
    st.header("Add Student")

    name = st.text_input("Name")
    age = st.number_input("Age", 1, 100)

    if st.button("Add"):
        st.session_state.students.append({"name": name, "age": age})
        st.success("Student Added!")


# -------------------------
# READ
# -------------------------
elif choice == "Read":
    st.header("View Students")

    if st.session_state.students:
        for i, s in enumerate(st.session_state.students):
            st.write(f"{i} → {s['name']} ({s['age']})")
    else:
        st.info("No data yet")


# -------------------------
# UPDATE
# -------------------------
elif choice == "Update":
    st.header("Update Student")

    if st.session_state.students:
        index = st.number_input("Index number", 0, len(st.session_state.students)-1)

        name = st.text_input("New Name")
        age = st.number_input("New Age", 1, 100)

        if st.button("Update"):
            st.session_state.students[index] = {"name": name, "age": age}
            st.success("Updated!")
    else:
        st.info("No data to update")


# -------------------------
# DELETE
# -------------------------
elif choice == "Delete":
    st.header("Delete Student")

    if st.session_state.students:
        index = st.number_input("Index number", 0, len(st.session_state.students)-1)

        if st.button("Delete"):
            st.session_state.students.pop(index)
            st.success("Deleted!")
    else:
        st.info("No data to delete")
