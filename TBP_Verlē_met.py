import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#parametri:
dt=0.001
T_max=82  #ilgums 
t=np.arange(0,T_max,dt)

G = 1
m1 = 1
m2 = 1
m3 = 1


# sākuma stāvokļi katram ķermenim:
# Ķermenis 1
x1 = np.zeros(len(t))
y1 = np.zeros(len(t))
vx1 = np.zeros(len(t))
vy1 = np.zeros(len(t))

# Ķermenis 2
x2 = np.zeros(len(t))
y2 = np.zeros(len(t))
vx2 = np.zeros(len(t))
vy2 = np.zeros(len(t))

# Ķermenis 3
x3 = np.zeros(len(t))
y3 = np.zeros(len(t))
vx3 = np.zeros(len(t))
vy3 = np.zeros(len(t))


#

#šeit ir dažas no apskatītajām orbītām

#


#(a)
# dt=0.01
# T_max=6.3
# t=np.arange(0,T_max,dt)
# # Sākuma stāvokļi katram ķermenim
# # Ķermenis 1
# x1=np.zeros(len(t))
# y1=np.zeros(len(t))
# vx1=np.zeros(len(t))
# vy1=np.zeros(len(t))

# # Ķermenis 2
# x2=np.zeros(len(t))
# y2=np.zeros(len(t))
# vx2=np.zeros(len(t))
# vy2=np.zeros(len(t))

# # Ķermenis 3
# x3=np.zeros(len(t))
# y3=np.zeros(len(t))
# vx3=np.zeros(len(t))
# vy3=np.zeros(len(t))

# # Ķermenis 1
# x1[0],y1[0]=1,0

# # Ķermenis 2
# x2[0],y2[0]=-1,0

# # Ķermenis 3
# x3[0],y3[0]=0,0
# # Ķermenis 1
# vx1[0],vy1[0]=0.34711,0.532728

# # Ķermenis 2
# vx2[0],vy2[0]=vx1[0],vy1[0]

# # Ķermenis 3
# vx3[0],vy3[0]=-2*vx1[0],-2*vy1[0]


###################################

# (c)

# m1=m2=m3=1.0
# dt=0.001
# T_max=82
# t=np.arange(0,T_max,dt)

# x1=np.zeros(len(t))
# y1=np.zeros(len(t))
# vx1=np.zeros(len(t))
# vy1=np.zeros(len(t))

# # Ķermenis 2
# x2=np.zeros(len(t))
# y2=np.zeros(len(t))
# vx2=np.zeros(len(t))
# vy2=np.zeros(len(t))

# # Ķermenis 3
# x3=np.zeros(len(t))
# y3=np.zeros(len(t))
# vx3=np.zeros(len(t))
# vy3=np.zeros(len(t))

# # Pozīcijas
# x1[0],y1[0]=1.0,0
# x2[0],y2[0]=-0.5,np.sqrt(3)/2
# x3[0],y3[0]=-0.5,-np.sqrt(3)/2

# # Ātrumi (tangenciāli rādītāji, lai iegūtu apli)
# vx1[0],vy1[0]= -0.5,-np.sqrt(3)/2
# vx2[0],vy2[0]=1.0,0
# vx3[0],vy3[0]=-0.5,np.sqrt(3)/2

############################################

#(e) (f)
dt=0.001
T_max=5
t=np.arange(0,T_max,dt)
x1,y1,vx1,vy1=np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t))
x2,y2,vx2,vy2=np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t))
x3,y3,vx3,vy3=np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t)), np.zeros(len(t))


m1=m2=1.0
m3=0.001  # ļoti viegls ķermenis

# Pozīcijas
x1[0],y1[0]=-0.5,0
x2[0],y2[0]=0.5,0
x3[0],y3[0]=0,1.2

# Ātrumi
vx1[0],vy1[0]=0,-0.5
vx2[0],vy2[0]=0,0.5
vx3[0],vy3[0]=1,0

#############################################



# (b)

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
# dt=0.000001   # Laika solis [s]
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

# # Ķermenis 1
# x1[0],y1[0]=-1,0

# # Ķermenis 2
# x2[0],y2[0]=1,0

# # Ķermenis 3
# x3[0],y3[0]=0,0
# # Ķermenis 1
# vx1[0],vy1[0]=0.30689,0.12551 (g)
# vx1[0],vy1[0]=0.28270,0.32721 (h)

# # Ķermenis 2
# vx2[0],vy2[0]=vx1[0],vy1[0]

# # Ķermenis 3
# vx3[0],vy3[0]=-2*vx1[0],-2*vy1[0]






#funkcija, kas aprēķina paātrinājumus dotajā laikā
def compute_acc(x1, y1, x2, y2, x3, y3):
    #attālumi
    dx12,dy12=x2-x1, y2-y1
    dx13,dy13=x3-x1, y3-y1
    dx23,dy23=x3-x2, y3-y2
    
    r12=np.sqrt(dx12**2+dy12**2)
    r13=np.sqrt(dx13**2+dy13**2)
    r23=np.sqrt(dx23**2+dy23**2)
    
    #paātrinājumi (katram ķermenim)
    ax1=G*m2*dx12/r12**3+G*m3*dx13/r13**3
    ay1=G*m2*dy12/r12**3+G*m3*dy13/r13**3
    
    ax2=G*m1*(-dx12)/r12**3+G*m3*dx23/r23**3
    ay2=G*m1*(-dy12)/r12**3+G*m3*dy23/r23**3
    
    ax3=G*m1*(-dx13)/r13**3+G*m2*(-dx23)/r23**3
    ay3=G*m1*(-dy13)/r13**3+G*m2*(-dy23)/r23**3
    
    return ax1,ay1,ax2,ay2,ax3,ay3

#sākuma paātrinājumi
ax1,ay1,ax2,ay2,ax3,ay3=compute_acc(x1[0],y1[0],x2[0],y2[0],x3[0],y3[0])

#iterācija ar Verlē metodi
for i in range(len(t)-1):
    #atjaunina pozīcijas
    x1[i+1]=x1[i]+vx1[i]*dt+0.5*ax1*dt**2
    y1[i+1]=y1[i]+vy1[i]*dt+0.5*ay1*dt**2
    
    x2[i+1]=x2[i]+vx2[i]*dt+0.5*ax2*dt**2
    y2[i+1]=y2[i]+vy2[i]*dt+0.5*ay2*dt**2
    
    x3[i+1]=x3[i]+vx3[i]*dt+0.5*ax3*dt**2
    y3[i+1]=y3[i]+vy3[i]*dt+0.5*ay3*dt**2

    #aprēķina jaunos paātrinājumus no jaunajām pozīcijām
    ax1_new,ay1_new,ax2_new,ay2_new,ax3_new,ay3_new=compute_acc(x1[i+1], y1[i+1], x2[i+1], y2[i+1], x3[i+1], y3[i+1])

    #atjaunina ātrumus
    vx1[i+1]=vx1[i]+0.5*(ax1+ax1_new)*dt
    vy1[i+1]=vy1[i]+0.5*(ay1+ay1_new)*dt

    vx2[i+1]=vx2[i]+0.5*(ax2+ax2_new)*dt
    vy2[i+1]=vy2[i]+0.5*(ay2+ay2_new)*dt

    vx3[i+1]=vx3[i]+0.5*(ax3+ax3_new)*dt
    vy3[i+1]=vy3[i]+0.5*(ay3+ay3_new)*dt

    #sagatavo paātrinājumus nākamajam solim
    ax1,ay1=ax1_new,ay1_new
    ax2,ay2=ax2_new,ay2_new
    ax3,ay3=ax3_new,ay3_new


#Enerģijas aprēķins:
E1=0.5*m1*(vx1**2+vy1**2)- (G*(m1*m2)/np.sqrt((x1-x2)**2+(y1-y2)**2)) - (G*(m1*m3)/np.sqrt((x1-x3)**2+(y1-y3)**2))
E2=0.5*m2*(vx2**2+vy2**2)- (G*(m2*m1)/np.sqrt((x2-x1)**2+(y2-y1)**2)) - (G*(m2*m3)/np.sqrt((x2-x3)**2+(y2-y3)**2))
E3=0.5*m3*(vx3**2+vy3**2)- (G*(m3*m1)/np.sqrt((x1-x3)**2+(y1-y3)**2)) - (G*(m3*m2)/np.sqrt((x3-x1)**2+(y3-y1)**2))
print(np.max(E1))
print(np.max(E2))
print(np.max(E3))
print(np.max(E1+E2+E3))











plt.figure(figsize=(6,6))
plt.plot(x1,y1,label=r"$m_1$")
plt.plot(x2,y2,label=r"$m_2$")
plt.plot(x3,y3,label=r"$m_3$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper right")
plt.grid()
plt.axis("equal")
plt.title("T={}".format(T_max))

#plt.savefig("test12345.png",dpi=1000)
plt.show()


#gifu veidošana
# fig, ax = plt.subplots(figsize=(6,6))
# # # pēc nepieciešamības:
# # ax.set_xlim(min(np.min(x1),np.min(x2))-1, max(np.max(x1),np.max(x2))+1)
# # ax.set_ylim(min(np.min(y1),np.min(y2))-1, max(np.max(y1),np.max(y2))+1) 

#manuāli maina:
    
# ax.set_xlim(-1.5,1.5)
# ax.set_ylim(-1,1.5)
# ax.set_xlabel("x",fontsize=16)
# ax.set_ylabel("y",fontsize=16)
# ax.grid()
# ax.set_aspect('equal')

# line1, = ax.plot([], [], 'b-')
# line2, = ax.plot([], [], 'r-')
# line3, = ax.plot([], [], 'g-')

# point1, = ax.plot([], [], 'bo')
# point2, = ax.plot([], [], 'ro')
# point3, = ax.plot([], [], 'go')


# legend_text1 = ax.text(0.7, 0.21, '',fontsize=16, transform=ax.transAxes, color='blue')
# legend_text2 = ax.text(0.7, 0.14, '',fontsize=16, transform=ax.transAxes, color='red')
# legend_text3 = ax.text(0.7, 0.07, '',fontsize=16, transform=ax.transAxes, color='green')

# x1_traj, y1_traj = [], []
# x2_traj, y2_traj = [], []
# x3_traj, y3_traj = [], []

# # funkcija katram kadram
#manuāli maina - kadru skaita regulēšanai
# skips=range(0,len(t),50)
# def update(frame):
#     point1.set_data(x1[frame], y1[frame])
#     point2.set_data(x2[frame], y2[frame])
#     point3.set_data(x3[frame], y3[frame])
    
#     line1.set_data(x1[:frame+1], y1[:frame+1])
#     line2.set_data(x2[:frame+1], y2[:frame+1])
#     line3.set_data(x3[:frame+1], y3[:frame+1])

#     legend_text1.set_text(r"$E_1$= {}".format(np.round(E1[frame],decimals=3)))
#     legend_text2.set_text(r"$E_2$= {}".format(np.round(E2[frame],decimals=3)))
#     legend_text3.set_text(r"$E_3$= {}".format(np.round(E3[frame],decimals=3)))                          
    
#     ax.set_title("t={}".format(np.round(t[frame],decimals=3)))

#     return point1,point2,point3,line1,line2,line3



# ani = animation.FuncAnimation(fig,update,frames=skips,interval=5,blit=False)

# ani.save("Binārā izsviešana v3=1 dt=0.001.gif",writer="pillow",fps=30,dpi=150)

# plt.show()



