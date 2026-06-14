<<<<<<< HEAD
import streamlit as st
import sqlite3

st.title("📝 Quiz")

role = st.session_state.get("role", "student")

conn = sqlite3.connect("data/database.db")
cursor = conn.cursor()

# =========================
# ADMIN - ADD QUESTION
# =========================

if role == "admin":

    st.subheader("➕ Add Question")

    question = st.text_area("Question")

    option_a = st.text_input("Option A")
    option_b = st.text_input("Option B")
    option_c = st.text_input("Option C")
    option_d = st.text_input("Option D")

    correct_answer = st.selectbox(
    "Correct Answer",
    [option_a, option_b, option_c, option_d],
    key="new_correct_answer"
)

    if st.button("Save Question"):

        cursor.execute(
            """
            INSERT INTO quiz
            (
                question,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                question,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer
            )
        )

        conn.commit()

        st.success("Question Saved Successfully")

# =========================
# LOAD QUESTIONS
# =========================

cursor.execute("SELECT * FROM quiz")
questions = cursor.fetchall()

# =========================
# ADMIN - EDIT / DELETE
# =========================

if role == "admin" and len(questions) > 0:

    st.divider()

    st.subheader("✏️ Manage Questions")

    selected = st.selectbox(
        "Select Question",
        questions,
        format_func=lambda x: x[1]
    )

    edit_question = st.text_area(
        "Edit Question",
        value=selected[1]
    )

    edit_a = st.text_input(
        "Edit Option A",
        value=selected[2]
    )

    edit_b = st.text_input(
        "Edit Option B",
        value=selected[3]
    )

    edit_c = st.text_input(
        "Edit Option C",
        value=selected[4]
    )

    edit_d = st.text_input(
        "Edit Option D",
        value=selected[5]
    )

    edit_correct = st.selectbox(
        "Correct Answer",
        [edit_a, edit_b, edit_c, edit_d],
        key="edit_correct_answer"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Update Question"):

            cursor.execute(
                """
                UPDATE quiz
                SET
                    question=?,
                    option_a=?,
                    option_b=?,
                    option_c=?,
                    option_d=?,
                    correct_answer=?
                WHERE id=?
                """,
                (
                    edit_question,
                    edit_a,
                    edit_b,
                    edit_c,
                    edit_d,
                    edit_correct,
                    selected[0]
                )
            )

            conn.commit()

            st.success("Question Updated")

            st.rerun()

    with col2:

        if st.button("Delete Question"):

            cursor.execute(
                """
                DELETE FROM quiz
                WHERE id=?
                """,
                (selected[0],)
            )

            conn.commit()

            st.success("Question Deleted")

            st.rerun()

# =========================
# STUDENT QUIZ
# =========================

if len(questions) > 0:

    st.divider()

    st.subheader("📚 Answer Quiz")

    answers = []

    for q in questions:

        answer = st.radio(
            q[1],
            [q[2], q[3], q[4], q[5]],
            key=f"question_{q[0]}"
        )

        answers.append(
            (answer, q[6])
        )

    if st.button("Submit Quiz"):

        score = 0

        for user_answer, correct_answer in answers:

            if user_answer == correct_answer:
                score += 1

        st.success(
            f"Score: {score}/{len(questions)}"
        )

        for i in range(len(questions)):

            if answers[i][0] == answers[i][1]:

                st.success(
                    f"✓ Question {i + 1} Correct"
                )

            else:

                st.error(
                    f"✗ Question {i + 1} Wrong"
                )

                st.info(
                    f"Correct Answer: {answers[i][1]}"
                )

else:

    st.info("No questions available")

conn.close()
=======
import streamlit as st

st.title("📝 Quiz")

answer = st.radio(
    "Apakah beban yang datang daripada berat struktur sendiri?",
    [
        "Beban Mati",
        "Beban Hidup",
        "Beban Angin",
        "Beban Gempa"
    ]
)

if st.button("Submit"):

    if answer == "Beban Mati":
        st.success("Correct!")
    else:
        st.error("Wrong Answer")
>>>>>>> 560a7b9ecbd9845f259431c99c596a61f73df7ac
