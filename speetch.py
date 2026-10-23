# Python program to translate 
# speech to text and text to speech 
  
  
import speech_recognition as sr 
import pyttsx3
from  show_image import show_img
import cv2
  
# Initialize the recognizer  
r = sr.Recognizer()  
  
# Function to convert text to 
# speech 
def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
      
      
# Loop infinitely for user to 
# speak 
myword= list()
def split(word): 
    return [char for char in word]  
def call():     
      
    # Exception handling to handle 
    # exceptions at the runtime 
    try: 
          
        # use the microphone as source for input. 
        with sr.Microphone() as source2: 
              
            # wait for a second to let the recognizer 
            # adjust the energy threshold based on 
            # the surrounding noise level  
            r.adjust_for_ambient_noise(source2, duration=0.2) 
              
            #listens for the user's input  
            audio2 = r.listen(source2) 
              
            # Using ggogle to recognize audio 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower()
            
  
            print("Did you say "+MyText)
            SpeakText(MyText)
            #MyText.replace(" ","1")
            print(MyText)
            
            
            nn=split(MyText)
            sn=["1" if x==" " else x for x in nn]
            
            print(sn)
            show_img(sn)
            img = cv2.imread('test.jpg',0)
            #cv2.imshow('test',img)
            #
            
                
            
            
            
            
            
             
              
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("unknown error occured")
#while(1):
   # print("...")
      
    
