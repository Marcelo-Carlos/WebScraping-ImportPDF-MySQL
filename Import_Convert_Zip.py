import tabula
from zipfile import *
import os

#TRANSFORMA EM DF POR QUESTÃO DE CONFERENCIA. ESSA PARTE DA EXECUÇÃO PODE SER COMENTADA
path = ("C:/IntuitiveCare/Padrao_TISS_Componente_Organizacional_202006.pdf")
df = tabula.read_pdf(path, pages=(str(81)+'-'+str(87)), multiple_tables=True)
print(df)

#CONVERTE O PDF EM CSV COM O NOME E LOCAL INFORMADOS
arq_csv = ("C:/IntuitiveCare/marcelo.csv")
tabula.convert_into(path, arq_csv, output_format="csv", pages=(str(81)+'-'+str(87))) 

#POR FIM COMPACTA O ARQUIVO
with ZipFile("C:/IntuitiveCare/marcelo.zip", "w") as myzip:  
    myzip.write("C:/IntuitiveCare/marcelo.csv") 







    
      
    


    






