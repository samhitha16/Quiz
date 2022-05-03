# Quiz
Instructions to run my code -
    • Open a terminal in the directory of my server.py and client.py files. Run this command ‘python server.py **Your IP Address** **Any port number**’
    • Open three more terminals and run this command ‘python client.py **Your IP Address** **Server’s Port number**’ in each of them .
    • You can connect from different desktops i.e, connect to server as client from different desktop or on the same desktop.
    
    
Description of the project-
	There is a host to conduct the quiz(server). There are three participants (3 clients). Once all the three contestants connect to the host , the quiz starts. Host sends the question to all the three of them. Host waits for 10 seconds for one of the participant to press the buzzer. Buzzer is any key on the key board. And once the buzzer is pressed by a participant , host waits for 10 more seconds for the answer from that particular participant.If he answers it right he gets ‘+1’ points . If he fails to answer within time or answers it wrong he gets ‘-0.5’ points. After the host displays a particular question , if none of the clients respond with a buzzer within 10 seconds the host moves on to the next question. The game continues till any one of the player scores ‘+5’ points. That player to score ‘+5’ points is the winner. And in case the questions at server exhaust before anyone scores ‘+5’ , the player with the highest points till then will be declared as the winner.Every time a player answers a question the points he gain or lose will be displayed in his terminal. For every answered question the correct answer is displayed in the server terminal. At the end server terminal has the score  card and each individual will get their respective scores and get to know who is the winner. 
