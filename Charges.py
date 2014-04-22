WorkSalt
========
import string as st
import numpy as np
import matplotlib.pyplot as mp #Importing tools
from mpl_toolkits.mplot3d import Axes3D

#start = "\033[1m"
#end = "\033[0;0m"  #This is to make some text bold
#print "Hi, you have to introduce the geometric figure to select the points where the charges are going to be located"
#print "The figures that are available are" + start + " cube" + end + "," #The introduction of the program
#vil=raw_input("Insert just the name of one figure which is mentioned above") #A raw_input to introduce the figure of choice

fig = mp.figure() #Ploting the base
ax = fig.add_subplot(111, projection='3d') #Making the Axes
ax.set_title("Crystal of Salt")
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')  #Naming labels
ax.set_zlabel('Z Label')
grace,hop,need=0,1,2 #Making things easier


a,b=[0,0,0],[0.5,0,0]
c,d=[1,0,0],[0,0.5,0]
e,f=[0.5,0.5,0],[1,0.5,0]
g,h=[0,1,0],[0.5,1,0]
i,j=[1,1,0],[0,0,0.5]
k,l=[0.5,0,0.5],[1,0,0.5]		#Introducing the position of the charges to select them later
m,n=[0,0.5,0.5],[0.5,0.5,0.5]		#P.D. There is no easier way to do this
o,p=[1,0.5,0.5],[0,1,0.5]
q,r=[0.5,1,0.5],[1,1,0.5]
s,t=[0,0,1],[0.5,0,1]
u,v=[1,0,1],[0,0.5,1]
w,x=[0.5,0.5,1],[1,0.5,1]
y,z=[0,1,1],[0.5,1,1]
aa=[1,1,1]


forever=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa] #Making a list with all the things above
useful=list(st.ascii_lowercase) #Another list with the alphabet to name each point that will be plotted 
useful.append("aa") #But it doesn't contain "aa", so we need to append it manually
for bad in range(0, 27, 2):
     forever[bad].append(-1)
for rage in range(1, 27, 2):
    forever[rage].append(1)           
for guilty in forever: #This "for" will work in the range of len(forever) #I had problems here, so I changed x to guilty
    eraw=forever.index(guilty) #Here we will find the first ocurrence of x
    ax.scatter(guilty[grace], guilty[hop], guilty[need]) #Plotting a point in (x, y, z)
    ax.text(guilty[grace], guilty[hop], guilty[need], useful[eraw], style="oblique") #Plotting text in the same coordenates to identificate each one

put=forever #I don't need to explain this
send=[] #An empty list
for selfish in range(27): #I was a little paranoid, so I didn't use x again 
    ill=put[grace] #ill is the first integrator of put
    put.pop(grace) #And we erase this first element in put
    for shine in put: #Another for that makes the below operation for each letter of the alphabet making all the combinatorials
        sun=((((shine[grace]-ill[grace])**2.0)+((shine[hop]-ill[hop])**2.0)+((shine[need]-ill[need])**2.0))**0.5)*(shine[3]*ill[3]) #This operation is the calculus of a vector with x,y,z components by Pythagoras
        send.append(sun) #When we do the operation of above we get a number that we send to the list made before

    
send=[x*2 for x in send] #The work is mutual so...
send=[1/x for x in send] #And the distance is dividing so...
ax.text(0, 0, 1.5, "$E_p$="+str(sum(send))+"$kQ^2$"+"$r^-$"+"$^1$", style="oblique") #Plotting the U in the plot


mp.show() #Showing the plot
#print "Here you have the distribution of the charges"
#mp.show() #Showing the plot3D
#hey=raw_input("Do you want to remove some of them [y/n]")
#if hey==y:
#    return fig
