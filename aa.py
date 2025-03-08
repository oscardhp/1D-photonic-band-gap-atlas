from funciones import *

puntos_alpha1_aa_fino = np.round(np.arange(0.01,1.0,0.01),2) 
puntos_propor23_aa_fino = np.round(np.arange(0.0,1.01,0.01),2)
control = ctl_num([20,1024,50,500], 'control-3mat.ctl')

rutina_doble(num_bandas=20,
             archivo_control=control,
             control=[5.0,2.5,1.0,0.0,0.8,0.2], 
             puntos1=puntos_alpha1_aa_fino,
             puntos2=puntos_propor23_aa_fino,
             tipo=['3mat',3,4], # num, mat o lineal. indice (en control) para introduccion   
             cifras=5, # solo se usa para el balance de proporciones
             nombre='3mat-aa',
             funcion=partial(para_aa,cifras=6)
            )


























