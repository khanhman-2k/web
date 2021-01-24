from flask import Flask, flash, redirect, render_template
import speech_recognition
import speech_recognition as sr
from gtts import gTTS
import playsound
import sys
from exitstatus import ExitStatus
print("\nSiri:...")