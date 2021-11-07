# -Electric-Meter-Image-Transmission
need to import fswebcam,pyrebase
executable files are check_all_files.sh,webcam.sh

setUp crontab:
0 * * * * python3 /home/pi/Desktop/piCodes/take_img.py
* * * * 0,2,6 python3 /home/pi/Desktop/piCodes/delete_files.sh
