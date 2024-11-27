from winotify import Notification, audio
from playsound import playsound
import time



toast=Notification(app_id='Vissa Appointment',
                    title='Visa Appointment Found',
                    msg='A new appointment has been schedule has been detected',
                    duration='long',
                    icon=r'C:\Users\Lenovo\Desktop\Hope\images.png')

toast.add_actions(label='Enter Website',launch='https://portal.ustraveldocs.com/')


toast.set_audio(audio.LoopingAlarm,loop=True)

toast.show()


