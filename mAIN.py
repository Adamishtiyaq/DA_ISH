import pandas as pd
import matplotlib as plt
import numpy as np


class DA:
      def read_data(self):
          file = 'Worksheet in D  Lesson 2019 Applied Sriptong Using Python Python Elective (IT49450) - Project_14Mar19.csv'
          df = pd.read_csv(file)
          print(df)



      

        
B=DA
B.read_data()
