import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

dt = 0.01
T_max = 50
t = np.arange(0,T_max,dt)

G=1
m1=1
m2=1
m3=1


# Sākuma stāvokļi katram ķermenim
#Ķermenis 1
x1 = np.zeros(len(t))
y1 = np.zeros(len(t))
vx1 = np.zeros(len(t))
vy1 = np.zeros(len(t))

#ķermenis 2
x2 = np.zeros(len(t))
y2 = np.zeros(len(t))
vx2 = np.zeros(len(t))
vy2 = np.zeros(len(t))

#ķermenis 3
x3 = np.zeros(len(t))
y3 = np.zeros(len(t))
vx3 = np.zeros(len(t))
vy3 = np.zeros(len(t))




#

#šeit ir dažas no apskatītajām orbītām

#


#(a)
dt=0.01
T_max=6.3
t=np.arange(0,T_max,dt)
# Sākuma stāvokļi katram ķermenim

#ķermenis 1
x1=np.zeros(len(t))
y1=np.zeros(len(t))
vx1=np.zeros(len(t))
vy1=np.zeros(len(t))

#ķermenis 2
x2=np.zeros(len(t))
y2=np.zeros(len(t))
vx2=np.zeros(len(t))
vy2=np.zeros(len(t))

#ķermenis 3
x3=np.zeros(len(t))
y3=np.zeros(len(t))
vx3=np.zeros(len(t))
vy3=np.zeros(len(t))

#ķermenis 1
x1[0],y1[0]=1,0

#ķermenis 2
x2[0],y2[0]=-1,0

#ķermenis 3
x3[0],y3[0]=0,0
# Ķermenis 1
vx1[0],vy1[0]=0.34711,0.532728

#ķermenis 2
vx2[0],vy2[0]=vx1[0],vy1[0]

#Ķermenis 3
vx3[0],vy3[0]=-2*vx1[0],-2*vy1[0]


###################################

#(c)

# m1=m2=m3=1.0
# dt=0.01
# T_max=82
# t=np.arange(0,T_max,dt)


# #ķermenis 1
# x1=np.zeros(len(t))
# y1=np.zeros(len(t))
# vx1=np.zeros(len(t))
# vy1=np.zeros(len(t))

# #Ķermenis 2
# x2=np.zeros(len(t))
# y2=np.zeros(len(t))
# vx2=np.zeros(len(t))
# vy2=np.zeros(len(t))

# #ķermenis 3
# x3=np.zeros(len(t))
# y3=np.zeros(len(t))
# vx3=np.zeros(len(t))
# vy3=np.zeros(len(t))


# x1[0],y1[0]=1.0,0
# x2[0],y2[0]=-0.5,np.sqrt(3)/2
# x3[0],y3[0]=-0.5,-np.sqrt(3)/2

# #ātrumi (tangenciāli rādītāji, lai iegūtu apli)
# vx1[0],vy1[0]= -0.5,-np.sqrt(3)/2
# vx2[0],vy2[0]=1.0,0
# vx3[0],vy3[0]=-0.5,np.sqrt(3)/2

############################################

#(e) (f)
# dt=0.001
# T_max=5
# t=np.arange(0,T_max,dt)
# x1,y1,vx1,vy1=np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t))
# x2,y2,vx2,vy2=np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t))
# x3,y3,vx3,vy3=np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t))


# m1=m2=1.0
# m3=0.001  #ļoti viegls ķermenis

# # Pozīcijas
# x1[0],y1[0]=-0.5,0
# x2[0],y2[0]=0.5,0
# x3[0],y3[0]=0,1

# # Ātrumi
# vx1[0],vy1[0]=0,-0.5
# vx2[0],vy2[0]=0,0.5
# vx3[0],vy3[0]=1,0

#############################################



#(b)

# dt=0.001
# T_max=35.5
# t=np.arange(0,T_max,dt)


# m1,m2,m3 =1,0.0001,100


# x1,y1,vx1,vy1=np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t))
# x2,y2,vx2,vy2=np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t))
# x3,y3,vx3,vy3=np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t))


# x1[0],y1[0],vx1[0],vy1[0] = 15, 0, 0, 2.58
# x2[0],y2[0],vx2[0],vy2[0] = 14.2, 0, 0,1.5
# x3[0],y3[0],vx3[0],vy3[0] = 0, 0, 0,0

#####################################################

#(d)
# m1,m2,m3=0.0001,0.0001,1
# dt=0.001
# T_max=6.4
# t=np.arange(0,T_max,dt)

# x1,y1,vx1,vy1=np.zeros(len(t)),np.zeros(len(t)),np.zeros(len(t)),np.zeros(len(t))
# x2,y2,vx2,vy2=np.zeros(len(t)),np.zeros(len(t)),np.zeros(len(t)),np.zeros(len(t))
# x3,y3,vx3,vy3=np.zeros(len(t)),np.zeros(len(t)),np.zeros(len(t)),np.zeros(len(t))

# #sākumnosacījumi
# x1[0],y1[0],vx1[0],vy1[0]=1,0,0,1
# x2[0],y2[0],vx2[0],vy2[0]=-1,0,0,-1
# x3[0],y3[0],vx3[0],vy3[0]=0,0,0,0

###############################################

# #(g) (h)
# dt=0.000001
# T_max=6.2356 (g)
# T_max=10.9626 (h)
# t=np.arange(0,T_max,dt)
# m1=1
# m2=1
# m3=1

# #ķermenis 1
# x1=np.zeros(len(t))
# y1=np.zeros(len(t))
# vx1=np.zeros(len(t))
# vy1=np.zeros(len(t))

# #Ķermenis 2
# x2=np.zeros(len(t))
# y2=np.zeros(len(t))
# vx2=np.zeros(len(t))
# vy2=np.zeros(len(t))

# #ķermenis 3
# x3=np.zeros(len(t))
# y3=np.zeros(len(t))
# vx3=np.zeros(len(t))
# vy3=np.zeros(len(t))

# #Ķermenis 1
# x1[0],y1[0]=-1,0

# #Ķermenis 2
# x2[0],y2[0]=1,0

# #Ķermenis 3
# x3[0],y3[0]=0,0
# #Ķermenis 1
# vx1[0],vy1[0]=0.30689,0.12551 ##(g)
# vx1[0],vy1[0]=0.28270,0.32721 ##(h)

# #Ķermenis 2
# vx2[0],vy2[0]=vx1[0],vy1[0]

# #Ķermenis 3
# vx3[0],vy3[0]=-2*vx1[0],-2*vy1[0]



E1,E2,E3=np.zeros(len(t)),np.zeros(len(t)),np.zeros(len(t))

#Eilera-Kromera metode
for i in range(len(t)-1):
    #rādiusvektori
    dx12=x2[i]-x1[i]
    dy12=y2[i]-y1[i]
    r12=np.sqrt(dx12**2+dy12**2)
    
    dx13=x3[i]-x1[i]
    dy13=y3[i]-y1[i]
    r13=np.sqrt(dx13**2+dy13**2)
    
    dx23=x3[i]-x2[i]
    dy23=y3[i]-y2[i]
    r23=np.sqrt(dx23**2+dy23**2)
    E1[i]=0.5*m1*(vx1[i]**2+vy1[i]**2)- (G*(m1*m2)/r12) - (G*(m1*m3)/r13)
    E2[i]=0.5*m2*(vx2[i]**2+vy2[i]**2)- (G*(m2*m1)/r12) - (G*(m2*m3)/r23)
    E3[i]=0.5*m3*(vx3[i]**2+vy3[i]**2)- (G*(m3*m1)/r13) - (G*(m3*m2)/r23)
    
    #paātrinājumu aprēķins katram ķermenim
    #Ķermenis 1
    ax1=G*m2*dx12/r12**3+G*m3*dx13/r13**3
    ay1=G*m2*dy12/r12**3+G*m3*dy13/r13**3
    
    #Ķermenis 2
    ax2=G*m1*(-dx12)/r12**3+G*m3*dx23/r23**3
    ay2=G*m1*(-dy12)/r12**3+G*m3*dy23/r23**3
    
    #Ķermenis 3
    ax3=G*m1*(-dx13)/r13**3+G*m2*(-dx23)/r23**3
    ay3=G*m1*(-dy13)/r13**3+G*m2*(-dy23)/r23**3
    
    #Ķermenis 1
    vx1[i+1]=vx1[i]+ax1*dt
    vy1[i+1]=vy1[i]+ay1*dt
    x1[i+1]=x1[i]+vx1[i+1]*dt
    y1[i+1]=y1[i]+vy1[i+1]*dt
    
    # Ķermenis 2
    vx2[i+1]=vx2[i]+ax2*dt
    vy2[i+1]=vy2[i]+ay2*dt
    x2[i+1]=x2[i]+vx2[i+1]*dt
    y2[i+1]=y2[i]+vy2[i+1]*dt
    
    # Ķermenis 3
    vx3[i+1]=vx3[i]+ax3*dt
    vy3[i+1]=vy3[i]+ay3*dt
    x3[i+1]=x3[i]+vx3[i+1]*dt
    y3[i+1]=y3[i]+vy3[i+1]*dt






plt.figure(figsize=(6,6))
plt.plot(x1,y1,label=r"$m_3$")
plt.plot(x2,y2,label=r"$m_2$")
plt.plot(x3,y3,label=r"$m_3$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper right")
plt.grid()
plt.axis("equal")
plt.title("T={}".format(T_max))

# plt.savefig("ttt.png",dpi=1000)








#gif animācijas:
# fig,ax=plt.subplots(figsize=(6,6))
# # ax.set_xlim(min(np.min(x1),np.min(x2))-1,max(np.max(x1),np.max(x2))+1)
# # ax.set_ylim(min(np.min(y1),np.min(y2))-1,max(np.max(y1),np.max(y2))+1)

# #manuāli: gif animācijas x,y robežas
# ax.set_xlim(-8,8)
# ax.set_ylim(-8,8)
# ax.set_xlabel("x",fontsize=16)
# ax.set_ylabel("y",fontsize=16)
# ax.grid()
# ax.set_aspect('equal')

# line1, = ax.plot([], [], 'b-')
# line2, =ax.plot([], [], 'r-')
# line3, = ax.plot([], [], 'g-')

# point1, = ax.plot([], [], 'bo')
# point2, =ax.plot([], [], 'ro')
# point3, =ax.plot([], [], 'go')


# legend_text1=ax.text(0.7, 0.21, '',fontsize=16, transform=ax.transAxes, color='blue')
# legend_text2=ax.text(0.7, 0.14, '',fontsize=16, transform=ax.transAxes, color='red')
# legend_text3=ax.text(0.7, 0.07, '',fontsize=16, transform=ax.transAxes, color='green')

# x1_traj, y1_traj = [], []
# x2_traj, y2_traj = [], []
# x3_traj, y3_traj = [], []

# # manuāli maina - kadru skaita regulēšana
# skips=range(0,len(t),125)
# def update(frame):
#     point1.set_data(x1[frame],y1[frame])
#     point2.set_data(x2[frame],y2[frame])
#     point3.set_data(x3[frame], y3[frame])
    
#     line1.set_data(x1[:frame+1], y1[:frame+1])
#     line2.set_data(x2[:frame+1],y2[:frame+1])
#     line3.set_data(x3[:frame+1], y3[:frame+1])

#     legend_text1.set_text(r"$E_1$= {}".format(np.round(E1[frame],decimals=3)))
#     legend_text2.set_text(r"$E_2$= {}".format(np.round(E2[frame],decimals=3)))
#     legend_text3.set_text(r"$E_3$= {}".format(np.round(E3[frame],decimals=3)))                          
    
#     ax.set_title("t={}".format(np.round(t[frame],decimals=3)))

#     return point1,point2,point3,line1,line2,line3



# ani=animation.FuncAnimation(fig,update,frames=skips,interval=10,blit=True)

# ani.save("tEST12345679.gif",writer="pillow",fps=30,dpi=150)

# plt.show()
