import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
  print("Speak")
  audio_text = r.listen(source)
  print("Thanks.Time over")
  a = r.recognize_google(audio_text)
  print(a, file=open('WRITE YOUR TEXT FILE PATH OVER HERE /home/edwin/making/t.txt','w'))
  try:
    print("Text :" +r.recognize_google(audio_text))
  except:
    print("sorry i didnt get that")
