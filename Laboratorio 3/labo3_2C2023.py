import matplotlib.pyplot as plt
import numpy as np


def proyectarPts(T, wz):
    assert(T.shape == (2,2)) # chequeo de matriz 2x2
    assert(T.shape[1] == wz.shape[0]) # multiplicacion matricial valida   
    xy = None
    ############### Insert code here!! ######################3    
    xy = np.matmul(T,wz)
    ############### Insert code here!! ######################3
    return xy

def proyectar_pts_3x3(T,wz,ab):
    T_nueva = np.vstack((T,ab))
    T_nueva = np.hstack((T_nueva,[0,0,1]))
    wz = [x.append(1) for x in wz ]
    xy = np.matmul(T_nueva,wz)
    return xy
    
def circle(r):
    x = np.linspace(-r,r,1000)
    y1 = np.sqrt(r*r - x*x)
    y2 = -np.sqrt(r*r - x*x)
    y = np.concatenate((y1,y2))
    x = np.concatenate((x,x))

    wz = np.concatenate((x,y)).reshape(2,2000)
    return wz

def matriz_rotacion(ang):
    res = np.array([[np.cos(ang),-np.sin(ang)],
                     [np.sin(ang),np.cos(ang)]])
    return res
    
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
          
def vistform(ab,T, wz, titulo=''):
    # transformar los puntos de entrada usando T
    #xy = proyectarPts(T, wz)
    xy = proyectar_pts_3x3(T,wz,ab)
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
    
def grid_plot(ax, ab, limits, a_label, b_label):
    ax.plot(ab[0,:], ab[1,:], '.')
    ax.set(aspect='equal',
           xlim=limits[0], ylim=limits[1],
           xlabel=a_label, ylabel=b_label)


def main():
    print('Ejecutar el programa')
    # generar el tipo de transformacion dando valores a la matriz T
    
    #Ejercicio 1.>>>>>>>>>>>>>>>>>>>>>>>>>>>
    T_resc = np.array([[2, 0],[0,3]])
    T_inv = np.linalg.inv(T_resc)
    corners = np.array([[0,0],[100,100]])
    circunferencia = circle(10)
    #vistform(T_resc, circunferencia, 'Ejer.1:Dilatar')
    xy = proyectarPts(T_resc,circunferencia)
    #vistform(T_inv, xy, 'Ejer.1:Dilatar T inversa')
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #Ejercicio 2
    T = np.array([[1., 0.4],[0,1.]])
    wz = pointsGrid(corners)
    #vistform(T, wz, 'Ejercicio 2')
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #Ejercicio 3
    T_rot = matriz_rotacion(45)
    wz = pointsGrid(corners)
    #vistform(T_rot, wz, 'Ejercicio 3')
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #Ejercicio 4
    T_rot_inv = matriz_rotacion(-45)
    T_rot_esc = T_rot_inv @ T_resc @ T_rot
    #vistform(T_rot_esc, wz, 'Ejercicio 4')
    #vistform(T_rot_esc, circunferencia, 'Ejercicio 4:Circunferencia')
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #Ejercicio 5
    ab = np.array([5,3])
    #wz = proyectar_pts_3x3(T,wz,ab)
    print(T)
    vistform(ab,T, wz, 'Ejercicio 5')
    
if __name__ == "__main__":
    main()
