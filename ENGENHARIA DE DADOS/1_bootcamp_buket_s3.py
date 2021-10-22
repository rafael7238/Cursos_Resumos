import boto3 #Para interagir com o AWS S3
import pandas as pd


s3_client = boto3.client('s3')
s3_client.download_file("datalake-rafa-igti","data/Cronograma de Estudo.xlsx","Download_efetuado.xlsx") #Fazendo o Dowload no Arquivo

pf = pd.read_excel("Download_efetuado.xlsx")
print(pf)

s3_client.upload_file("Arquivo_para_Upload.xlsx","datalake-rafa-igti","data/Arquivo_para_Upload.xlsx")