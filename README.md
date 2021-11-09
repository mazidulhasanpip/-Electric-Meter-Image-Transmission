# -Electric-Meter-Image-Transmission

1.Need to install fswebcam,pyrebase

2.Create a folder named "piCodes" inside home/pi/Desktop/ and copy paste all the files

3. Make files Executable : check_all_files.sh,webcam.sh

setUp crontab:

=>0 * * * * python3 /home/pi/Desktop/piCodes/take_img.py

=>* * * 0,2,6 python3 /home/pi/Desktop/piCodes/delete_files.sh
