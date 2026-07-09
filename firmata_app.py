import streamlit as st
from pathlib import Path

path = Path("angle.txt")
path_block = Path("block.txt")

st.header("Управление сервоприводом")

angle = st.sidebar.radio("Выбери градус поворота:", [0, 30, 60, 90, 120, 150, 180])

if st.button("Повернуть"):
    past_angle = path.read_text()

    def success_message():
        st.success(angle)
        path.write_text(f"{angle}")
        path_block.write_text("True")

    def error_message():
        st.error("Серво уже повернут на этот угол, выбери другой")
        path_block.write_text("False")

    if past_angle == str(angle):
        error_message()
    else:
        success_message()

    st.write(path.resolve())