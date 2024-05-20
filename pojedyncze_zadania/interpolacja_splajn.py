import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('punkty.txt')

y_values = data[:, 1]

def interpolacja_splajn():
    chosen_y = y_values[0]
    
    chosen_points = data[data[:, 1] == chosen_y]
    x_chosen = chosen_points[:, 0]
    F_chosen = chosen_points[:, 2]
    
    X = np.zeros((len(chosen_points)+2,len(chosen_points)+2))
    Y = np.zeros((len(chosen_points)+2))
    K = np.zeros((len(chosen_points)+2))

    def wypelnianieMacierzyX():

        h = x_chosen[1]-x_chosen[0]
    
        for i in range(len(chosen_points)+1):
            X[i,i] = 4
            X[i,i+1] = 1
            X[i+1,i] = 1
            
        X[0,0]=-3/h
        X[0,2]=3/h
        X[0,1]=0
        X[len(chosen_points)+1,len(chosen_points)+1]=3/h
        X[len(chosen_points)+1,len(chosen_points)-1]=-3/h
        X[len(chosen_points)+1,len(chosen_points)]=0
     
    def wypelnianieMacierzyY():
        for i in range (0,len(chosen_points)):
            Y[i+1] = F_chosen[i]
        Y[0] = 1
        Y[len(chosen_points)+1] = -1
        
    wypelnianieMacierzyX()
    wypelnianieMacierzyY()

    K = np.linalg.solve(X,Y)
    print(K)
    x_values = np.linspace(np.min(x_chosen), np.max(x_chosen), 1000)
    interpolated_values = []
    for x in x_values:       # obliczanie wartosci interpolowanej dla kazdego punktu x, ze wzoru na interpolacje kubiczna
        for i in range(len(chosen_points)):
            if x >= chosen_points[i, 0] and x <= chosen_points[i+1, 0]:
                h = chosen_points[i+1, 0] - chosen_points[i, 0]
                t = (x - chosen_points[i, 0]) / h
                interpolated_value = (1 - t) * chosen_points[i, 2] + t * chosen_points[i+1, 2] + (t * (1 - t) * ((h ** 2) / 6) * ((1 - t) * K[i] + t * K[i+1]))
                interpolated_values.append(interpolated_value)
                break
        
    plt.plot(x_chosen, F_chosen, 'bo', label='Dane')
    plt.plot(x_values, interpolated_values, 'r-', label='Interpolacja')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Interpolacja funkcją sklejaną')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
interpolacja_splajn()