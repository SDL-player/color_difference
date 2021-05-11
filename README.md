# Color_Diff

Color_Diff é um mini projeto que eu fiz utilizando Python para calcular o Delta E(CIE 2000) entre dois valores RGB, ou seja, calcular a diferença visual entre duas cores.

# Como Usar

```python
from color_diff import Color_Diff

cor_1 = (9, 2, 0)

cor_2 = (234, 56, 1)

diff = Color_Diff(cor_1, cor_2)

result = diff.calcule()
```

# Conversões

Devido ao fato de que o Delta E utiliza valores em formato Lab para calcular, foi necessário realizar essas conversões: RGB -> SRGB -> SRGB Linear -> XYZ -> Lab. Para acelerá-las, utilizei Numpy e Numba.

# Objetivo

Apresentar uma opção mais rápida e simplificada para calcular essa diferença em Python.
