from funciones import *

puntos_epsilon_fino = np.round(np.arange(1.1,9.6,0.1),2)
puntos_alpha_fino = np.round(np.arange(0.01,1.0,0.01),2)
control = ctl_num([20,512,50,500], 'control-2mat.ctl')

rutina_doble(num_bandas=20,
             archivo_control=control,
             control=[2.4,1.0,0.8,0.2], 
             puntos1=puntos_epsilon_fino,
             puntos2=puntos_alpha_fino,
             tipo=['2mat',0,2], # num, mat o lineal. indice (en control) para introduccion   
             cifras=3, # solo se usa para el balance de proporciones
             nombre='2mat-doble',
             funcion=partial(balance_proporcional_n,
                             control_balance=[2.4,1.0,0.8,0.2],
                             material=0,
                             cifras=3
                            ) # obligatorio para balance dimensional
                              # hace posible lista de parametros mas exotica
            )






