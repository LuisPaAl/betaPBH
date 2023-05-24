# Quickstar

We can check if `PBHBeta` is installed correctly by importing the library and all the modules that compose it.

```{code-block}
from betaPBH import *
```

In addition, the user is recommended to import `numpy` and `matplotlib.pyplot`, so the main header of the code would be written as follows:

```{code-block}
from betaPBH import *
import matplotlib.pyplot as plt
import numpy as np
```


```{note}
Lo que está abajo se lee raro, no? A partir de acá hay que poner los ejemplos que te había pedido, tanto el de obtener la figura con las rectas, para diferentes valores de M como el obtener las constraints de PBHs en un fondo de radiación.
...
La primera función que ejecutaremos será {py:func}`betaPBH.functions.put_M_array`, la cual contiene la instrucción para generar un array de masas, a partir de un parametro llamado delta_M

```{code-block}
betaPBH.functions.put_M_array()
```


```{note}
La librería contiene un modulo llamado `contraints.py` en el cual se almacenara el `return` de {py:func}`betaPBH.functions.put_M_array`. 
```



