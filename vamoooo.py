from tabula.io import read_pdf
import tabula
from itertools import repeat
import os
import re
import numpy
import pandas as pd

direc = os.listdir(adress)
filelist = []
for file in direc:
    if file.endswith('.pdf'):
            filelist.append(file)

# df creation and export to excel
lista_cert = pd.DataFrame(filelist)
n=len(lista_cert)
print('Certidões localizadas: ', n)

prop = []
cp = []
contri = []
for line in range(n):
    lista_tabelas = tabula.read_pdf(file, pages="all")
    tab1 = lista_tabelas[0]
    tab_com = tab1.head(3)
    print(tab_com)
    tab_com.rename(columns={"Unnamed: 0": "adress"}, inplace=True)
    bi=sorted(tab_com)
    a=bi[0]
    b=bi[1]
    print(a,b)
    print(a)
    tab_com.drop([0, 1], axis=0, inplace=True)
    pop = tab_com["adress"]
    # pop.reset_index()
    given_value = pop
    new_list = []
    new_list.extend(repeat(given_value, n))
    s = pd.Series([new_list], index=[2])
    ba = s.to_string(index=False)
    tab2 = tab1.head(15)
    cont = tab2['Certidão de Dados Cadastrais do Imóvel - IPTU 2021'][0]
    bui = re.findall('[0-9]+', cont)
    for trinca in bui:
        contribuinte = ''.join(bui)  # correto. não mexer
    d=contribuinte
    tab3 = tab2["Unnamed: 0"]
    df = pd.DataFrame(tab3)
    df.rename(columns={"Unnamed: 0": "name"}, inplace=True)
    df.drop([0, 1, 2, 3, 4, 5, 6, 7], axis=0, inplace=True)
    se = df[df.name.str.contains('CPF ')]
    ji = []
    ji = str(df[df.name.str.contains('CPF ')])
    nu = ji.replace('CPF ', '')
    io = nu.replace('.', '')
    ui = io.replace('-', '')
    new = str(ui)
    fac = re.findall('[0-9]+', new)
    for fa in fac:
        cpf = ''.join(fac)  # correto. não mexerfac = re.findall('[0-9]+', new)
    fal = re.findall('[^,;\s]+', new)
    for fi in fal:
        nome = ''.join(fal)  # correto. não mexer
    comp = len(cpf)
    if comp == 12:
        CPF = cpf[1:15]
        NOME = nome[16:]
        prop.append(NOME)
        cp.append(CPF)
        contri.append(d)
    elif comp == 13:
        CPF = cpf[2:16]
        NOME = nome[17:]
        prop.append(NOME)
        cp.append(CPF)
        contri.append(d)

#falta a linha do apto
adr = pd.DataFrame(data=ba)
ls = pd.DataFrame(data=prop)
ld = pd.DataFrame(data=cp)
la = pd.DataFrame(data=contri)

era = adr.iloc[:,-1:]
rrr = era.columns['APTO']
ll = ls.iloc[:,-1:]#ultima linha lista todos os proprietários
ll.columns = ['PROPRIETARIO']
LLL = ld.iloc[:,-1:]#ultima linha lista todos os cpfs
LLL.columns = ['CPF']
LAA = la.iloc[:,-1:]#ultima linha lista todos os cod.contribuintes
LAA.columns = ['CONTRIBUINTE']

k = ll.join(LLL)
nx = k.join(LAA)
off = nx.join(rrr)

off.to_csv('cpf.csv', index=False)
print('Transferencia Concluida')

