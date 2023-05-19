# Quickstar

Una forma de revisar que la librería `betaPBH` se haya instalado correctamente, sería inmediatemente importar la librería y todos los modulos que la componen.

```{code-block}
from betaPBH import *
```

Ademas se recomienda al usuario importar `numpy` y `matplotlib.pyplot`, por lo que la cabecera principal del codigo quedaría escrita de la siguiente forma:

```{code-block}
from betaPBH import *
import matplotlib.pyplot as plt
import numpy as np
```

La primera función que ejecutaremos será {py:func}`betaPBH.functions.put_M_array`, la cual contiene la instrucción para generar un array de masas, a partir de un parametro llamado delta_M

```{code-block}
betaPBH.functions.put_M_array()
```


```{note}
La librería contiene un modulo llamado `contraints.py` en el cual se almacenara el `return` de {py:func}`betaPBH.functions.put_M_array`. 
```



