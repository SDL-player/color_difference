# Color_Difference

Color_Difference é um mini projeto que eu fiz utilizando Python para calcular o Delta E(CIE 2000) entre dois valores RGB, ou seja, calcular a diferença visual entre duas cores.

# Como Usar

```python
from color_difference import Color_Diff

cor_1 = (9, 2, 0)

cor_2 = (234, 56, 1)

diff = Color_Diff(cor_1, cor_2)

result = diff.calculate()
```

# Conversões

Devido ao fato de que o Delta E utiliza valores em formato Lab para calcular, foi necessário realizar essas conversões: RGB -> SRGB -> SRGB Linear -> XYZ -> Lab. Para acelerá-las, utilizei C.

# Objetivo

Apresentar uma opção mais rápida e simplificada para calcular essa diferença em Python.

# Atualização

A antiga versão havia falhas em relação ao desempenho e ao valor final da conta. Essa apresenta um desempenho 300x maior que a versão feita em numba e numpy.
