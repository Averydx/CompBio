import numpy as np
import matplotlib.pyplot as plt


# Defining our problem

a = 10
r = 0.5 #growth rate
k = 100 #carrying capacity
mu = 0.1 #death rate
length = 50 #mm
time = 50 #seconds
nodes = 40

# Initialization 

dx = length / nodes
dy = length / nodes

dt = min(   dx**2 / (4 * a),     dy**2 / (4 * a))

t_nodes = int(time/dt)

u = np.zeros((nodes, nodes))  # Plate is initially as 20 degres C

# Boundary Conditions 

u[0, :] = u[-1,:]
u[-1, :] = u[0,:]

u[:, 0] = np.linspace(0, 0, nodes)
u[:, -1] = np.linspace(0, 40, nodes)

# Visualizing with a plot

fig, axis = plt.subplots()

pcm = axis.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)

# Simulating

counter = 0

while counter < time :

    w = u.copy()

    for i in range(1, nodes-1):
        for j in range(1, nodes - 1):

            dd_ux = (w[i-1, j] - 2*w[i, j] + w[i+1, j])/dx**2 
            dd_uy = (w[i, j-1] - 2*w[i, j] + w[i, j+1])/dy**2

            u[i, j] = dt * a * (dd_ux + dd_uy) + dt * r * w[i,j]*(1-w[i,j]/k) - dt * mu * w[i,j] + w[i,j]

    counter += dt

    print("t: {:.3f} [days], Average Saturation: {:.2f} percent".format(counter, np.average(u)))

    # Updating the plot

    pcm.set_array(u)
    axis.set_title("Saturation at t: {:.3f} [days].".format(counter))
    plt.pause(0.01)


plt.show()












