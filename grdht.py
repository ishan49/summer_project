import RPi.GPIO as GPIO
import socket
import csv
import time
import RPi
import math
import struct
import cv2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
pwm1=GPIO.PWM(7,50)
pwm1.start(7.5)
GPIO.setup(8,GPIO.OUT)
pwm2=GPIO.PWM(8,50)
pwm2.start(7.5)
UDP_IP = "192.168.43.216"
UDP_PORT = 5050
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))
video_capture = cv2.VideoCapture(0)
while True:
    _,frame = video_capture.read()
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        data,addr=sock.recvfrom(1024)
        azu = struct.unpack_from('!f', data, 36)
        azimuth = abs(azu[0])
        rol = struct.unpack_from('!f', data, 44)
        roll = abs(rol[0])
        duty1=float(azimuth)/10+2.5
        pwm1.ChangeDutyCycle(duty1)
        time.sleep(0.002)
        duty2=float(roll)/10+2.5
        pwm2.ChangeDutyCycle(duty2)
        time.sleep(0.002)
        print(azimuth, "                  ",roll)
            

        
