import streamlit as st
from supabase import create_client

url = "https://wmzpahjpjkejfrzbewfz.supabase.co"
key = "sb_publishable_O8Erz_dPQk3fBkmhopdY-g_UitSlzJZ"

supabase = create_client(url, key)
data = supabase.table("arduino_state").select("*").execute().data[0]

st.header("Управление сервоприводом")

angle = st.sidebar.radio("Выбери градус поворота:", [0, 30, 60, 90, 120, 150, 180])

if st.button("Повернуть"):
    past_angle = data["angle"]

    def success_message():
        st.success(angle)
        supabase.table("arduino_state").update({"angle": angle}).eq("id", 1).execute()
        supabase.table("arduino_state").update({"state": True}).eq("id", 1).execute()

    def error_message():
        st.error("Серво уже повернут на этот угол, выбери другой")
        supabase.table("arduino_state").update({"state": False}).eq("id", 1).execute()

    if past_angle == str(angle):
        error_message()
    else:
        success_message()