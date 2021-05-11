# Color_Difference

Color_Difference é um mini projeto que eu fiz utilizando Python para calcular o Delta E(CIE 2000) entre dois valores RGB, ou seja, calcular a diferença quase visual entre duas cores.

# Conversões

Devido ao fato de que o Delta E utiliza valores em formato Lab para calcular, foi necessário realizar essas conversões: RGB -> SRGB -> SRGB Linear -> XYZ -> Lab. Para acelerá-las, utilizei Numpy e Numba.

# Objetivo

Apresentar uma opção mais rápida e simplificada para calcular essa diferença em Python.
