import streamlit as st
from supabase import create_client

# Это приложение отправляет данные на облако, из которого читает информацию цикл из закомментированного файла pymata-firmata_from_app.py, который управляет сервоприводом.
# Файл pymata-firmata_from_app.py должен быть запущен на компьютере, к которому подключен Arduino с сервоприводом и обязательно отдельно от этого приложения, иначе не будет работать, так как у streamlit
# нет доступа к COM портам.

url = "https://wmzpahjpjkejfrzbewfz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndtenBhaGpwamtlamZyemJld2Z6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODM2NjQ5MTcsImV4cCI6MjA5OTI0MDkxN30.mkiDSYFwrUdW0h4_W2Et13OlBz4gqAVrPMktTocrGvU"

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

    if past_angle == angle:
        error_message()
    else:
        success_message()