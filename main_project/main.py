import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pnadium

pnadium.anual.download(ano=2023, t=1, tipo='v', caminho='./pnadium_2020.csv')
