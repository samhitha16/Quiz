import socket
import select
from thread import *
import sys
import time
import random

flag=0

# AF_NET is the address of the socket
# SOL_SOCKET means the type of the socket
#SOCK_STREAM means that the data or characters are read in a flow
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Setting up the server
if len(sys.argv) != 3:
    print ("Print in the following order : xxx.py, IP address, port number")
    exit()

#Allots the first argument of the string as the IP Address
IP_address = str(sys.argv[1])
#Allocates the second argument as the port number
Port = int(sys.argv[2])

#These are the values that the client must be aware about
server.bind((IP_address, Port))
server.listen(100)

list_of_clients=[]


Q = [" The world's smallest country.. \n a.Canada b.Russia c.Maldives d.Vatican city",
     " Which buliding is not in IIITB \n a.Bhaskara b.Lilavathi c.C V Raman d.Aryabatta",
     " Most affected country till date by Corona virus \n a.Germany b.Italy c.USA d.China",
     " Which state has the highest literacy rate \n a.Uttar Pradesh b.Kerala c.Goa d.Karnataka",
     " How many bones does an adult human have? \n a.206 b.208 c.201 d.196",
     " The tallest waterfall in the world..\n a.Gullfoss b. Venezuela's Angel Falls c.Victoria Falls d.Niagara Falls",
     " How many eyes does a bee have? \n a.3 b.5 c.2 d.4",
     " How many states are there in India? \n a.24 b.29 c.30 d.31",
     " Who won the IPL in 2019?\n a.Royal Challengers Bangalore b.Sunrisers Hyderabad c.Kolkata Knight riders d.Mumbai Indians ",
     " What name is used to refer to a group of frogs? \n a.A Clutch b.A Colony c.An Army d.A Nest",
     " Who was the first Indian female astronaut ? \n a.Sunita Williams b.Kalpana Chawla c.None of them d.Both of them ",
     " Which planet has the most gravity? \n a.Jupiter b.Saturn c.Uranus d.Earth",
     " How many Lord of the Rings films are there? \n a.3 b.7 c.5 d.4",
     " How many players are on the field in soccer? \n a.7 b.11 c.9 d.10",
     " Which country produces the most coffee in the world? \n a.Brazil b.Vietnam c.Columbia d.Indonesia",
     " Who gifted the Statue of Libery to the US? \n a.Brazil b.France c.Wales d.Germany",
     " Hottest planet in the solar system \n a.Mercury b.Pluto c.Earth d.Venus"
     " How are elements numbered 58 to 71 in the periodic table called? \n a.Magnets b.Lanthanons c.Halogens d.Metals",
     " Which city is known as Garden City \n a.Bangalore b.Agra c.Hyderabad d.Kerala",
     " Richest man in the world .. \n a.Bill gates b.Jeff bezos c.Warren Buffett d.Larry Ellison",
     " Which country has more lakes than the rest of the world combined? \n a.Finland b.China c.Canada d.Norway",
     " What do paleontologists study? \n a.Mountains b.Lost Civilisation c.Animals d.Fossils",
     " What is a SuperNova? \n a.An underwater valcano b.The explosion of Star c.The eye of tornado d.An intense lightning storm",
     " Which chess piece can't move in a straight line? \n a.Knight b.Rook c.Bishop d.King",
     " Which company owns Audi \n a.BMW b.Ford c.Volkswagen d.KIA",
     " What's the technical term for a lie detector? \n a.Teragraph b.Polygraph c.Seismograph d.Omnigraph",
     " Complete this proverb: All roads lead to _______. \n a.Rome b.Home c.Wisdom d.Charity",
     " Pet of Mickey Mouse \n a.Scooby-Doo b.Pluto c.Odie d.Mortimer"]

A = ['d', 'c', 'c', 'b', 'a', 'b', 'b', 'b', 'd', 'c', 'b', 'a', 'a', 'b', 'a', 'b', 'd','b','a','b','c','d','b','a','c','b','a','b']

Count=[]
client = ["address",-1]
bzr =[0, 0, 0] #Buzzer List

def clientthread(conn, addr):
    conn.settimeout(10)
    conn.send("Hello Genius!!!\n Welcome to this quiz! Answer any 5 questions correctly before your opponents do\n Press any key on the keyboard as a buzzer for the given question\n")
    #Welcome message
    while True:
        try:
            message = conn.recv(2048)
            if message:
                if bzr[0]==0:
                    client[0] = conn
                    bzr[0] = 1
                    i = 0
                    while i < len(list_of_clients):
                            if list_of_clients[i] == client[0]:
                                break
                            i +=1
                    client[1] = i

                elif bzr[0] ==1 and conn==client[0]:
                        bol = message[0] == A[bzr[2]][0]
                        print A[bzr[2]][0]
                        if bol:
                            broadcast("player" + str(client[1]+1) + " +1" + "\n\n")
                            Count[i] += 1
                            if Count[i]==5:
                                broadcast("player" + str(client[1]+1) + " WON" + "\n")
                                end_quiz()
                                sys.exit()

                        else:
                            broadcast("player" + str(client[1]+1) + " -0.5" + "\n\n")
                            Count[i] -= 0.5
                        bzr[0]=0
                        if len(Q) != 0:
                            Q.pop(bzr[2])
                            A.pop(bzr[2])
                        if len(Q)==0:
                            end_quiz()
                            break
                        quiz()

                else:
                        conn.send(" player " + str(client[1]+1) + " pressed buzzer first\n\n")
            else:
                    remove(conn)
        except socket.timeout:
            if len(Q) != 0:
                Q.pop(bzr[2])
                A.pop(bzr[2])
            if len(Q)==0:
                end_quiz()
                break
            else:
                quiz()


def broadcast(message):
    for clients in list_of_clients:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)

def end_quiz():
    global flag
    if(flag == 0):
        broadcast("GAME OVER!!!\n")
        bzr[1]=1
        i = Count.index(max(Count))
        broadcast("player " + str(i+1)+ " wins!! by scoring "+str(Count[i])+" points.")
        for x in range(len(list_of_clients)):
            list_of_clients[x].send("You scored " + str(Count[x]) + " points.")
            print "Player"+str(x+1)+"-->"+str(Count[x])
        #remove(clients)
        flag=1
        server.close()


def quiz():
    bzr[2] = random.randint(0,10000)%len(Q)
    if len(Q) != 0:
        for connection in list_of_clients:
            connection.send(Q[bzr[2]])
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    Count.append(0)
    print addr[0] + " connected"
    start_new_thread(clientthread,(conn,addr))
    if(len(list_of_clients)==3):
        quiz()
conn.close()
server.close()
