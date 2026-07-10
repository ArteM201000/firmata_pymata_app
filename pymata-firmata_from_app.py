# from pymata4 import pymata4
# import time
# from supabase import create_client
# from servo_py import Servo

# # password: firmata-pymata_1_project, project: https://wmzpahjpjkejfrzbewfz.supabase.co, key: sb_publishable_O8Erz_dPQk3fBkmhopdY-g_UitSlzJZ, table: https://wmzpahjpjkejfrzbewfz.supabase.co/rest/v1/arduino_state
# board = pymata4.Pymata4("COM6", 57600)

# url = "https://wmzpahjpjkejfrzbewfz.supabase.co"
# key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndtenBhaGpwamtlamZyemJld2Z6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODM2NjQ5MTcsImV4cCI6MjA5OTI0MDkxN30.mkiDSYFwrUdW0h4_W2Et13OlBz4gqAVrPMktTocrGvU"

# supabase = create_client(url, key)

# servo = Servo(9, board)

# while True:
#     data = supabase.table("arduino_state").select("*").execute().data[0]
#     angle = data["angle"]
#     state = data["state"]
#     print(state)
#     if state:
#         print(f"Поворот на угол: {angle}")
#         servo.write_servo(angle)
        
#         supabase.table("arduino_state").update({"state": False}).eq("id", 1).execute()
#         time.sleep(5) # можно сделать меньше, если интернет быстрее и серво успевает повернуться.

#     time.sleep(1)