# A program to generate OTP
import math , random

digits = "0123456789"
otp = ""
for i in range(4):
    otp += digits[math.floor(random.random() * 10)]

print("OTP of 4 digits: " + str(otp))

# Program to generate alphanumeric OTP

aldig = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = len(aldig)
alotp = ""
for i in range(6):
    alotp += aldig[math.floor(random.random()*length)]

print("Alphanumeric OTP of 6 characters: " + str(alotp))
