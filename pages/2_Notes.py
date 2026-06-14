import streamlit as st
import sqlite3
import os

# =========================
# PAGE TITLE
# =========================

st.title("📚 Learning Notes")

role = st.session_state.get("role", "student")

# =========================
# DATABASE
# =========================

conn = sqlite3.connect("data/database.db")
cursor = conn.cursor()

# =========================
# ADMIN ADD NOTE
# =========================

if role == "admin":

    st.subheader("➕ Add New Note")

    title = st.text_input("Title")

    content = st.text_area(
        "Content",
        height=200
    )

    uploaded_files = st.file_uploader(
        "Upload Images",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True
    )

    if st.button("Save Note"):

        image_paths = []

        if uploaded_files:

            os.makedirs("uploads", exist_ok=True)

            for uploaded_file in uploaded_files:

                image_path = os.path.join(
                    "uploads",
                    uploaded_file.name
                )

                with open(image_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                image_paths.append(image_path)

        all_images = "|".join(image_paths)

        cursor.execute(
            """
            INSERT INTO notes
            (title, content, image_path)
            VALUES (?, ?, ?)
            """,
            (
                title,
                content,
                all_images
            )
        )

        conn.commit()

        st.success("Note Saved Successfully")

# =========================
# LOAD NOTES
# =========================

cursor.execute("SELECT * FROM notes")
notes = cursor.fetchall()

# =========================
# ADMIN EDIT / DELETE
# =========================

if role == "admin" and len(notes) > 0:

    st.divider()

    st.subheader("✏️ Manage Notes")

    selected_note = st.selectbox(
        "Select Note",
        notes,
        format_func=lambda x: x[1],
        key="admin_note"
    )

    edit_title = st.text_input(
        "Edit Title",
        value=selected_note[1]
    )

    edit_content = st.text_area(
        "Edit Content",
        value=selected_note[2],
        height=200
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Update Note"):

            cursor.execute(
                """
                UPDATE notes
                SET title=?, content=?
                WHERE id=?
                """,
                (
                    edit_title,
                    edit_content,
                    selected_note[0]
                )
            )

            conn.commit()

            st.success("Note Updated")

            st.rerun()

    with col2:

        confirm_delete = st.checkbox(
            "Confirm Delete"
        )

        if confirm_delete:

            if st.button("Delete Note"):

                cursor.execute(
                    """
                    DELETE FROM notes
                    WHERE id=?
                    """,
                    (
                        selected_note[0],
                    )
                )

                conn.commit()

                st.success("Note Deleted")

                st.rerun()

# =========================
# VIEW NOTES
# =========================

st.divider()

cursor.execute("SELECT * FROM notes")
notes = cursor.fetchall()

if len(notes) > 0:

    selected_view = st.selectbox(
        "Select Note To View",
        notes,
        format_func=lambda x: x[1],
        key="view_note"
    )

    st.header(selected_view[1])

    image_data = selected_view[3]

    if image_data:

        images = image_data.split("|")

        for img in images:

            if os.path.exists(img):

                st.image(
                    img,
                    width=500
                )

    st.write(selected_view[2])

else:

    st.info("No notes available")

conn.close()