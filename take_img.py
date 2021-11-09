import os
import datetime
import time
import pyrebase
from zipfile import ZipFile
import psutil
    
#firebase Credentials
firebaseConfig = {
  'apiKey': "AIzaSyAeVxMEE7BM5tdELx9jsQwNDe4bVjCDTl0",
  'authDomain': "emeter-image-transmission.firebaseapp.com",
  'databaseURL': "https://emeter-image-transmission-default-rtdb.firebaseio.com",
  'projectId': "emeter-image-transmission",
  'storageBucket': "emeter-image-transmission.appspot.com",
  'messagingSenderId': "516882488455",
  'appId': "1:516882488455:web:f410318990794dc6a2ac22",
  'measurementId': "G-VXPMTX2QRP"
}

firebase = pyrebase.initialize_app(firebaseConfig) 
storage = firebase.storage()


#check images and zip folder
os.system('/home/pi/Desktop/piCodes/check_all_files.sh')
#file_script = 'check_all_files.sh'
#abs_files = os.path.dirname(file_script)
#print(abs_files)
#os.system(abs_files)
#print("Folder done")

#get cam script file location
#os.system('/home/pi/Desktop/piCodes/webcam.sh')
#webcam_script_name = 'webcam.sh'
#abs_webCam = os.path.dirname(webcam_script_name)
#print(abs_webCam)
#print("Cam done")

#give a name with write mode on
currentdate_hour = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M")
zipObj = ZipFile('/home/pi/Desktop/piCodes/zip_files/'+currentdate_hour+".zip", 'w')

#this will take image according to the given range
for x in range(2):
    currentdate = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    image_name = currentdate +".jpg"
    print (image_name)
    
    #capture the image
    #os.system('/home/pi/Desktop/piCodes/webcam.sh')
    os.system('/home/pi/Desktop/piCodes/webcam.sh')
    
    #time to change the reading of meter 
    time.sleep(5)
    
    #add file to zipObj
    zipObj.write('/home/pi/Desktop/piCodes/images/'+image_name,image_name)

# close the Zip File
zipObj.close()

#send zipped file to FRDC folder of firebase
print("Uploading file...")
storage.child('FRDC/'+currentdate_hour+".zip").put('/home/pi/Desktop/piCodes/zip_files/'+currentdate_hour+".zip")
print("Zip upload done")
