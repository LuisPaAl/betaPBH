import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.1' #Muy importante, deberéis ir cambiando la versión de vuestra librería según incluyáis nuevas funcionalidades
PACKAGE_NAME = 'betaPBH' #Debe coincidir con el nombre de la carpeta 

URL = 'https://github.com/TadeoDGAguilar'

LICENSE = 'MIT' #Tipo de licencia

DESCRIPTION = 'Library to compute abundances to PBHs in different scenarios on Early Universe' #Descripción corta

LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') #Referencia al documento README con una descripción más elaborada

LONG_DESC_TYPE = "text/markdown"

#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
      'matplotlib',
      'numpy',
      'scipy',
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=['Tadeo D. GA', 'Luis E. PA'],
    maintainer = 'Tadeo D. Gómez Aguilar',
    maintainer_email = 'tadeo.daguilar@gmail.com',
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)
