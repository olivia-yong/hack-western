# hack-western
<img width="230" alt="image" src="https://user-images.githubusercontent.com/116043965/202909316-37b397d2-aa64-45d1-b670-0325ebe3d21c.png">


## Inspiration
Ever wish you didn’t need to purchase a stylus to handwrite your digital notes? Each person at some point hasn’t had the free hands to touch their keyboard. Whether you are a student learning to type or a parent juggling many tasks, sometimes a keyboard and stylus are not accessible. We believe the future of technology won’t even need to touch anything in order to take notes. HyperTouch utilizes touchless drawings and converts your (finger)written notes to typed text! We also have a text to speech function that is Google adjacent.

## What it does
Using your index finger as a touchless stylus, you can write new words and undo previous strokes, similar to features on popular note-taking apps like Goodnotes and OneNote. As a result, users can eat a slice of pizza or hold another device in hand while achieving their goal. HyperTouch tackles efficiency, convenience, and retention all in one.  

## How we built it
Our pre-trained model from media pipe works in tandem with an Arduino nano, flex sensors, and resistors to track your index finger’s drawings. Once complete, you can tap your pinky to your thumb and HoverTouch captures a screenshot of your notes as a JPG. Afterward, the JPG undergoes a masking process where it is converted to a black and white picture. The blue ink (from the user’s pen strokes) becomes black and all other components of the screenshot such as the background become white. With our game-changing Google Cloud Vision API, custom ML model, and vertex AI vision, it reads the API and converts your text to be displayed on our web browser application.

## Challenges we ran into
Given that this was our first hackathon, we had to make many decisions regarding feasibility of our ideas and researching ways to implement them. In addition, this entire event has been an ongoing learning process where we have felt so many emotions — confusion, frustration, and excitement. This truly tested our grit but we persevered by uplifting one another’s spirits, recognizing our strengths, and helping each other out wherever we could.

One challenge we faced was importing the Google Cloud Vision API. For example, we learned that we were misusing the terminal and our disorganized downloads made it difficult to integrate the software with our backend components. Secondly, while developing the hand tracking system, we struggled with producing functional Python lists. We wanted to make line strokes when the index finger traced thin air, but we eventually transitioned to using dots instead to achieve the same outcome.

## Accomplishments that we're proud of
Ultimately, we are proud to have a working prototype that combines high-level knowledge and a solution with significance to the real world. Imagine how many students, parents, friends, in settings like your home, classroom, and workplace could benefit from HyperTouch’s hands free writing technology. 

This was the first hackathon for ¾ of our team, so we are thrilled to have undergone a time-bounded competition and all the stages of software development (ideation, designing, prototyping, etc.) toward a final product. We worked with many cutting-edge softwares and hardwares despite having zero experience before the hackathon.

In terms of technicals, we were able to develop varying thickness of the pen strokes based on the pressure of the index finger. This means you could write in a calligraphy style and it would be translated from image to text in the same manner. 

## What we learned
This past weekend we learned that our **collaborative** efforts led to the best outcomes as our teamwork motivated us to preserve even in the face of adversity. Our continued **curiosity** led to novel ideas and encouraged new ways of thinking given our vastly different skill sets.

## What's next for HoverTouch
In the short term, we would like to develop shape recognition. This is similar to Goodnotes feature where a hand-drawn square or circle automatically corrects to perfection.

In the long term, we want to integrate our software into web-conferencing applications like Zoom. We initially tried to do this using WebRTC, something we were unfamiliar with, but the Zoom SDK had many complexities that were beyond our scope of knowledge and exceeded the amount of time we could spend on this stage.

## What we built with
- Python
- OpenCV
- Arduino nano
- Adobe Illustrator
- Mediapipe
- Google Cloud Vision API
- Flask
- Text to Speech (TTS)

### [HoverTouch Website] (hoverpoggers.tech)


