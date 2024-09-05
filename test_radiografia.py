from radiografía import Radiografia
from radiacionerror import RadiacionError

try:
    radiografia = Radiografia(dosis=6.0, duracion=15)
except RadiacionError as e:
    print(e)

try:
    radiografia = Radiografia(dosis=3.0, duracion=35)
except RadiacionError as e:
    print(e)