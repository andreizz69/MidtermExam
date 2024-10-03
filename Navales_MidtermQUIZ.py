import requests  
import json
from faker import Faker
from webexteamssdk import WebexTeamsAPI


accessToken = "NGM0MjdiM2YtY2M0NS00MDBiLThiMTctZWM2ODYwMzA1MDNiMTYyOTQxYmQtYjA0_P0A1_bc884c7a-820b-497b-8b60-00b4d15ea95d"
api = WebexTeamsAPI(access_token=accessToken)

'''
#1
meeting = api.meetings.create(
    title='Midterm Quiz Meeting',
    start='2024-10-03T16:00:00Z',
    end='2024-10-03T16:30:00Z'
)
print(f'Meeting created with ID: {meeting.id}')
'''

'''
#2
room = api.rooms.create('Hendrix Midterm Quiz Room')
print(f'Room created with ID: {room.id}')
participant_email = 'ellisnuevas00@gmail.com'
api.memberships.create(room.id, personEmail=participant_email)
print(f'Added participant: {participant_email}')


#3
message = api.messages.create(room.id, text='My name Jeff :D')
print('Message sent!')

#4
messages = api.messages.list(room.id)
for msg in messages:
    print({msg})




#5
def delete_message():
    message_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL01FU1NBR0UvNjY0NjM5NjAtODE1Yi0xMWVmLWE2ODMtNTkzNDE5MjFmZWJl"
    api.messages.delete(message_id)
    print(f'Message {message_id} deleted')

delete_message()
'''

fake = Faker()

#1
for _ in range (10):
    print(f"Name: {fake.name()}, Email:  {fake.email()}, Phone: {fake.phone_number()}")