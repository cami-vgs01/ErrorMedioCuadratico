import matplotlib.pyplot as plt

def error_medio_cuadratico(x,y,theta):
    JTheta = 0

    for i in range(len(x)):
        JTheta = JTheta+ ((theta*x[i] - y[i])**2)

    JTheta = (1/(2*len(x)))*JTheta
    return JTheta

def calculoThetaSiguiente(acumuladorJtheta,acumuladorTheta,x,y,theta,factorAprendizaje):
    while True:
        JTheta=error_medio_cuadratico(x,y,theta)
        acumuladorJtheta.append(JTheta)
        acumuladorTheta.append(theta)
        theta = theta + factorAprendizaje
        var = True
        for i in range(len(acumuladorJtheta)):
            if acumuladorJtheta[i] < acumuladorJtheta[i-1] or len(acumuladorJtheta) == 1:
            #if(acumuladorTheta[i] <=3)or len(acumuladorJtheta) == 1:
                var = True
            else:
                var = False
        if var == False:
            break
    acumuladorJtheta.pop()
    acumuladorTheta.pop()
    print("JTheta: ", acumuladorJtheta)
    print("Theta: ", acumuladorTheta)

def f(x, theta):
    funcionObtenida = []
    for i in range(len(x)):
        funcionObtenida.append(theta*x[i])
    return funcionObtenida

def dibujarH(ultimoElemento,x,y):
    plt.scatter(x,y)
    funcionObtenidaMejorTheta = f(x,ultimoElemento)
    plt.plot(x,funcionObtenidaMejorTheta, color="red")
    plt.title("h(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def dibujarJTheta(acumuladorTheta,acumuladorJtheta):
    plt.title("J(θ)")
    plt.xlabel("θ")
    plt.ylabel("J(θ)")
    plt.plot(acumuladorTheta,acumuladorJtheta)
    plt.show()

def dibujarError(acumuladorTheta,x,y):
    plt.title("Error")
    plt.xlabel("Epocas")
    plt.ylabel("Error")
    h=[]
    contador = 0
    errorTotal = []
    while True:
        if acumuladorTheta:
            for j in range(len(x)):
                h.append(acumuladorTheta[contador]*x[j])
            error = []
            for j in range(len(h)):
                error.append(abs(y[j] - h[j]))
            errorTotal.append(sum(error)**2)
            h.clear()
            contador = contador + 1
            if contador >= len(acumuladorTheta):
                break
    plt.plot(errorTotal)
    plt.show()

def menu():
    while True:
        try:
            print("Error Medio Cuadratico")
            print("1. Ingresar datos")
            print("2. Salir")
            opc = int(input("Ingrese opcion: "))
            if opc == 1:
                x = []
                y = []
                n = int(input("Ingrese tamaño a vector: "))
                for i in range(n):
                    print("Ingrese valor", i+1, "de x: ")
                    x.append(float(input()))
                    print("Ingrese valor", i+1, "de y: ")
                    y.append(float(input()))

                theta = float(input("Ingrese theta: "))
                factorAprendizaje = float(input("Ingrese factor de aprendizaje: "))
                acumuladorJtheta = []
                acumuladorTheta = []
                calculoThetaSiguiente(acumuladorJtheta,acumuladorTheta,x,y,theta,factorAprendizaje)
                ultimoElemento = acumuladorTheta[-1]
                dibujarH(ultimoElemento,x,y)
                dibujarJTheta(acumuladorTheta,acumuladorJtheta)
                dibujarError(acumuladorTheta,x,y)
            if opc == 2:
                break
        except ValueError:
            print("Error, ingrese solo numero")
            print()

menu()