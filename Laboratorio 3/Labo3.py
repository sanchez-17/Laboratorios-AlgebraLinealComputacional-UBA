import matplotlib.pyplot as plt
import numpy as np


def proyectarPts(T, wz):
    assert(T.shape == (2,2)) # chequeo de matriz 2x2
    assert(T.shape[1] == wz.shape[0]) # multiplicacion matricial valida   
    xy = None
    ############### Insert code here!! ######################3    
    xy = np.dot(T,wz)
    ############### Insert code here!! ######################3
    return xy

def pointsGrid(corners):
    # crear 10 lineas horizontales
    [w1, z1] = np.meshgrid(np.linspace(corners[0,0], corners[1,0], 46),
                        np.linspace(corners[0,1], corners[1,1], 10))

    [w2, z2] = np.meshgrid(np.linspace(corners[0,0], corners[1,0], 10),
                        np.linspace(corners[0,1], corners[1,1], 46))

    w = np.concatenate((w1.reshape(1,-1),w2.reshape(1,-1)),1)
    z = np.concatenate((z1.reshape(1,-1),z2.reshape(1,-1)),1)
    wz = np.concatenate((w,z))
                         
    return wz

def matrizRotacion(phi):
    fila1 = [np.cos(phi),-np.sin(phi)]
    fila2 = [np.sin(phi),np.cos(phi)]
    res = np.array([fila1,fila2])
    return res

def pointsCircle(radio,Cw=0,Cz=0):
    
    ang = np.linspace(0,2* np.pi,100)
    w = radio * np.cos(ang) + Cw
    z = radio * np.sin(ang) + Cz
    
    w = w.reshape(1,-1)
    z = z.reshape(1,-1)
    wz = np.concatenate((w,z))
    #plt.plot(w,z,'.')
    return wz

def vistform(T, wz, titulo=''):
    # transformar los puntos de entrada usando T
    xy = proyectarPts(T, wz)
    if xy is None:
        print('No fue implementada correctamente la proyeccion de coordenadas')
        return
    # calcular los limites para ambos plots
    minlim = np.min(np.concatenate((wz, xy), 1), axis=1)
    maxlim = np.max(np.concatenate((wz, xy), 1), axis=1)

    bump = [np.max(((maxlim[0] - minlim[0]) * 0.05, 0.1)),
            np.max(((maxlim[1] - minlim[1]) * 0.05, 0.1))]
    limits = [[minlim[0]-bump[0], maxlim[0]+bump[0]],
               [minlim[1]-bump[1], maxlim[1]+bump[1]]]             
    
    fig, (ax1, ax2) = plt.subplots(1, 2)         
    fig.suptitle(titulo)
    grid_plot(ax1, wz, limits, 'w', 'z')    
    grid_plot(ax2, xy, limits, 'x', 'y')    
    # fig = plt.figure()
    # ax = fig.add_subplot()
    # ax.set_aspect('equal')
    
def grid_plot(ax, ab, limits, a_label, b_label):
    ax.plot(ab[0,:], ab[1,:], '.')
    ax.set(aspect='equal',
           xlim=limits[0], ylim=limits[1],
           xlabel=a_label, ylabel=b_label)


def main():
    print('Ejecutar el programa')
    # generar el tipo de transformacion dando valores a la matriz T
    T = np.array([[2.,0],[0,3.]])
    corners = np.array([[0,0],[100,100]])
    wz = pointsGrid(corners)
    vistform(T, wz, 'Encoger coordenadas')
    
    # generar el tipo de transformacion dando valores a la matriz T
    T2 = np.array([[1/2,0],[0,1/3]])
    corners = np.array([[0,0],[100,100]])
    wz = pointsGrid(corners)
    vistform(T2, wz, 'Achicar coordenadas')
    
    # Sobre una circunfernecia
    T = np.array([[1/2,0],[0,1/3]])
    wz = pointsCircle(5)
    vistform(T, wz, 'Circunferencia ')
    
    # Sobre una circunfernecia
    T = matrizRotacion(np.pi/4)
    corners = np.array([[0,0],[100,100]])
    wz = pointsGrid(corners)
    vistform(T, wz, 'Rotacion ')
    
    
if __name__ == "__main__":
    main()
