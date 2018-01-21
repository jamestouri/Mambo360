
# coding: utf-8

# In[4]:

# Mambo Drone Flying up, doing a full 360 spin while recording
from Mambo import Mambo
import cv2
from MamboVision import MamboVision
import threading
import time


# In[2]:

# you will need to change this to the address of YOUR mambo
mamboAddr = "e0:14:d0:63:3d:d0"


# In[10]:

# make my mambo object
mambo = Mambo(mamboAddr, use_wifi=True)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)


# In[11]:

if success:
    print("sleeping")
    mambo.smart_sleep(2)
    mambo.ask_for_state_update
    mambo.smart_sleep(2)
    
    mambo.safe_takeoff(5)
    print("Houston we have Liftoff")
    
    #Number of frames to Buffer in Memory.  Def. was 10 but I put it to 100 for a panoramic view
    mambo_vision = MamboVision(buffer_size = 100)
    userVision = UserVision(mambo_vision)
    mambo_vision.set_user_callback_function(userVision.save_pictures, user_callback_args=None)
    success = mambo_vision.open_video(max_retries=15)

    if(success) and (mambo.sensors.flying_state != "emergency"):
        print("Preparing to record")
        
        mambo_vision.start_video_buffering()
        #Turn degrees had range of (-180, 180)
        mambo.turn_degrees(180)
        mambo.turn_degrees(180)
        
        #Stop the Video
        mambo_vision.stop_video_buffering()
        
    mambo.safe_land(5)
    isAlive = False 
    
    mambo.smart_sleep(5)
    mambo.disconnect()
    print("Program finish")
        
        
        
        
    


# In[ ]:



