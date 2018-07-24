from american import CNFD_amer_ds,CNFD_amer_dx
import numpy as np
div = [0,0.1,0.2,0.3,0.4,0.5]
for ddiv in div:
    call_dx = CNFD_amer_ds(8.0,ddiv)
    print(call_dx)

