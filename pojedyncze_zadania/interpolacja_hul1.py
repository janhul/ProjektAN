import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('punkty.txt')

y_values = np.unique(data[:, 1])

def interpolacja():
    chosen_y = y_values[0]
    
    chosen_points = data[data[:, 1] == chosen_y]
    x_chosen = chosen_points[:, 0]
    F_chosen = chosen_points[:, 2]

    n = len(x_chosen)
    B = np.zeros((n, n))
    
    for i in range(0,n):
        for j in range(0,n):
            B[i, j] = x_chosen[i] ** j
    
    A = np.linalg.solve(B, F_chosen)
    
    print(F_chosen)
    print(B)

    def eval_polynomial(x, coeffs):
        return sum(coeffs[j] * x ** j for j in range(len(coeffs)))
    



    # Wykres
    plt.scatter(x_chosen, F_chosen, label='Dane')
    x_range = np.linspace(min(x_chosen), max(x_chosen), 1000)
    y_interp = [eval_polynomial(x, A) for x in x_range]
    plt.plot(x_range, y_interp, label='Interpolacja wielomianowa', color='red')
    
    plt.xlabel('x')
    plt.ylabel('F(x,y)')
    plt.title('Interpolacja wielomianowa dla y = ' + str(chosen_y))
    plt.grid(True)
    plt.legend()
    plt.show()
    
    # plt.scatter(x_chosen, F_chosen, label='Dane', color='blue')
    # plt.xlabel('x')
    # plt.ylabel('F(x,y)')
    # plt.title('Punkty dla y = ' + str(chosen_y))
    # plt.legend()
    # plt.show()
    
    
    
    
    
    

# Wywołanie funkcji interpolacji
interpolacja()





# y_values = np.unique(data[:, 1])

# def interpolacja():
#     chosen_y = y_values[0]

#     # Wyodrębnij punkty dla wybranej wartości y
#     chosen_points = data[data[:, 1] == chosen_y]
#     x_chosen = chosen_points[:, 0]
#     F_chosen = chosen_points[:, 2]


#     n = len(x_chosen)
#     B = np.zeros((n, n))
    
#     # Tworzenie macierzy Vandermonde'a
#     for i in range(0,n):
#         for j in range(0,n):
#             B[i, j] = x_chosen[i] ** j
#     print(B)
#     print("koniec B")
    
#     # Rozwiązanie układu równań liniowych w celu znalezienia współczynników wielomianu
#     A = np.linalg.solve(B, F_chosen)
#     print(A)
    

#     # Funkcja do oceny wielomianu na podstawie współczynników
#     def eval_polynomial(x, coeffs):
#         return sum(coeffs[j] * x ** j for j in range(len(coeffs)))

#     # Wykres oryginalnych danych i interpolacji wielomianowej
#     plt.scatter(x_chosen, F_chosen, label='Dane')
#     x_range = np.linspace(min(x_chosen), max(x_chosen), 1000)
#     y_interp = [eval_polynomial(x, A) for x in x_range]
#     plt.plot(x_range, y_interp, label='Interpolacja wielomianowa', color='red')
#     plt.xlabel('x')
#     plt.ylabel('F(x,y)')
#     plt.title('Interpolacja wielomianowa dla y = ' + str(chosen_y))
#     plt.legend()
#     plt.show()
#     print("Interpolacja wielomianowa zakończona")

# # Wywołanie funkcji interpolacji
# # interpolacja()