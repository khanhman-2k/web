from flask import Flask, flash, redirect, render_template
import speech_recognition
import speech_recognition as sr
from gtts import gTTS
import playsound
import sys
from exitstatus import ExitStatus

#Khai bao app
app = Flask(__name__)
#khởi tạo
bot_brain= ""
bot_ear = speech_recognition.Recognizer()
you=""
#hàm nghe
def hear():
    global you
    with speech_recognition.Microphone() as mic:
        print("\nSiri:Tôi đang nghe")
        audio = bot_ear.record(mic, duration=5)
        print("\nSiri:...")
    try:
        you = bot_ear.recognize_google(audio,language='vi-VN')
    except:
        you = ""
    print("\nYou:  "+you)

#hàm nói
def say(a):
    playsound.playsound(a)
#xác định tuyến (route) cơ bản /
@app.route("/")
#Ham index
def index():
	return render_template('index.html')
#Ham trang siri
@app.route("/result")
def result():
	print("\nXin chào! Tôi là siri trợ lý ảo của Trường Đại học Sao Đỏ. Tôi có thể giúp gì cho bạn.")
	say("gioi_thieu.mp3")
	return render_template('start.html')
@app.route("/start")
def start():
	while True:
		while True:
			print("\n Hãy đặt câu hỏi cho tôi")
			say("cau_hoi.mp3")
			say("beep.mp3")
			hear()
			# Siri hiểu
			if "kết thúc" in you or "stop" in you or "dừng" in you or "tạm dừng" in you or "đóng" in you or "tắt" in you:
				bot_brain = "Tạm biệt"
				say("bye.mp3")
				break
			elif you == "":
				bot_brain = "Xin hãy nói to hơn"
				say("khong_nghe_ro.mp3")
			###################################################################################################
			elif "giới thiệu" in you and "trường" in you:
				return render_template('dhsd.html')
			elif "tuyển sinh" in you and "thông tin" in you:
				return render_template('tuyensinh.html')
			elif "khoa đào tạo" in you:
				return render_template('khoadaotao.html')
			###################################################################################################
			else:
				bot_brain = "tôi không hiểu bạn nói"
				say("khong_hieu.mp3")
			# Siri trả lời
			print("\nSiri: " + bot_brain)
		if "kết thúc" in you:
			return render_template('stop.html')

@app.route("/next/<name>")
def next(name):
	filename=name+".mp3"
	say(filename)
	return render_template('start.html')

if __name__=='__main__':
    app.run(debug=True)
    app.run(host = '127.0.0.1', port=5000)