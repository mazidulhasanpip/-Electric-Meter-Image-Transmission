import os
import datetime
import time
import pyrebase
from zipfile import ZipFile

#firebase Credentials
firebaseConfig = {
    'apiKey': "AIzaSyAPDMY23mkmDib0G_NB7WovgKqceByWmSg",
    'authDomain': "raspimage-2b328.firebaseapp.com",
    'databaseURL': "https://raspimage-2b328-default-rtdb.firebaseio.com",
    'projectId': "raspimage-2b328",
    'storageBucket': "raspimage-2b328.appspot.com",
    'messagingSenderId': "915090438516",
    'appId': "1:915090438516:web:3bac95b92c463feed95421",
    'measurementId': "G-6RE6EMQFSY"  
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
zipObj = ZipFile('/home/pi/Desktop/piCodes/zip_files/'+currentdate_hour, 'w')

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
storage.child('FRDC/'+currentdate_hour).put('/home/pi/Desktop/piCodes/zip_files/'+currentdate_hour)
print("Zip upload done")