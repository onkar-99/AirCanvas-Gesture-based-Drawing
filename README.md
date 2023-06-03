# AirCanvas: Gesture-based Drawing using OpenCV

This is a doodle drawing game which can be played by a maximum of 5 players.
Here the doodles can be drawn in air and MAGICALLY the strokes are plotted on canvas to draw the doodles.   
Here the game first randomly gives categories to user and they have 60 seconds to draw as many doodles as possible. 
Scores are awarded based on successful prediction by the model which is trained on the Quick Draw Dataset.
26 categories which are easy to draw (eg clock, apple, bucket etc) are selected and model is trained specifically on them. 
Before starting the game, it is made mandatory to select the marker HSV colour range to select the object which is to be used for drawing doodles. 
index.py is the start file, and make sure to include all the other files in same folder and also change path in the IDE to that folder. 

Model: Model is trained on quickdraw dataset which is proprocessed to grayscale images in shape 64x64x1.  
[Link to Dataset](https://drive.google.com/drive/folders/1_abk1HS7DFUOTpK7Dx9aT0t46R5rEONl?usp=sharing)  
  
# Output
![Image](/run.gif)
