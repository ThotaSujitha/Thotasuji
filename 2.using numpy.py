Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

import numpy as np
matrix_1 = [
      [1, 2, 3], [4, 5, 6], [7, 8, 9]
   ] matrix_2 = [
      [7, 8, 9], [4, 5, 6],[1, 2, 3]
   ]
result = np.dot(matrix1, matrix2)
print(result)
