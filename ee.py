from funciones import *

puntos_epsilon1_ee_fino = np.round(np.arange(2.5,9.1,0.1),2)
puntos_frac_delta12_ee_fino = np.round(np.arange(0.0,1.01,0.01),2) #aclarar
control = ctl_num([20,512,50,500], 'control-3mat.ctl')

rutina_doble(num_bandas=20,
             archivo_control=control,
             control=[5.0,2.5,1.0,0.4,0.48,0.12], 
             puntos1=puntos_epsilon1_ee_fino,
             puntos2=puntos_frac_delta12_ee_fino,
             tipo=['3mat',0,1], # num, mat o lineal. indice (en control) para introduccion   
             cifras=4, # solo se usa para el balance de proporciones
             nombre='3mat-ee',
             funcion=partial(para_ee,cifras=5)
            )




















