#AG002 - MATHEUS HENRIQUE MARTINS - 1445

#IMPORTAÇÃO DAS BIBLIOTECAS
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import hamming_loss
from sqlalchemy import create_engine
import pymysql


#CONEXÃO COM O BANCO DE DADOS
sqlEngine = create_engine('mysql+pymysql://root:Matheus1399@localhost', pool_recycle=3600)

dbConnection = sqlEngine.connect()

dtFrame = pd.read_sql("select * from statlog.germancredit", dbConnection);

pd.set_option('display.expand_frame_repr', False)
#print(dtFrame)

dbConnection.close()


#DADOS - Tratamento dos dados vindos do BD:
feature_cols = ['laufkont', 'laufzeit', 'moral', 'verw', 'hoehe', 'sparkont', 'beszeit', 'rate', 'famges', 'buerge', 'wohnzeit',
                'verm', 'alter', 'weitkred', 'wohn', 'bishkred', 'beruf', 'pers', 'telef', 'gastarb', 'kredit']

X = dtFrame.iloc[:, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]].values
y = dtFrame.iloc[:, 21].values


#SEPARAÇÃO DA PORCENTAGEM DE DADOS P/ TESTE E TREINAMENTO DA REDE
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0) #80% treino e 20% teste


#CLASSIFICAÇÃO ATRAVÉS DA ÁRVORE DE DECISÃO
classifier = DecisionTreeClassifier()
classifier = classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

#MEDINDO A ACURÁCIA DO MODELO COM BASE NAS MÉTRICAS DE AVALIAÇÃO
print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
print('\n', classification_report(y_test, y_pred))
print(cohen_kappa_score(y_test, y_pred))
print(hamming_loss(y_test, y_pred))
print(metrics.fbeta_score(y_test, y_pred, beta=0.5), '\n\n')



#DATA INSERT - (ENTRADA DE DADOS DO USUÁRIO P/ SEREM CLASSIFICADOS PELO MODELO - AVALIAÇÃO DE CRÉDITO)
print('\nEntre com os dados solicitados abaixo: ')

while True:
    laufkont = int(input('laufkont: '))
    if( 1 <= laufkont <= 4):
        break

while True:
    laufzeit = int(input('laufzeit: '))
    if( 0 <= laufzeit ):
        break

while True:
    moral = int(input('moral: '))
    if( 1 <= moral <= 4):
        break

while True:
    verw = int(input('verw: '))
    if( 0 <= verw ):
        break

while True:
    hoehe = int(input('hoehe: '))
    if( 0 <= hoehe):
        break

while True:
    sparkont = int(input('sparkont: '))
    if( 1 <= sparkont <= 5):
        break

while True:
    beszeit = int(input('beszeit: '))
    if( 1 <= beszeit <= 5):
        break

while True:
    rate = int(input('rate: '))
    if( 1 <= rate <= 4):
        break

while True:
    famges = int(input('famges: '))
    if( 1 <= famges <= 4):
        break

while True:
    buerge = int(input('buerge: '))
    if( 1 <= buerge <= 3):
        break

while True:
    wohnzeit = int(input('wohnzeit: '))
    if( 1 <= wohnzeit <= 4):
        break

while True:
    verm = int(input('verm: '))
    if( 1 <= verm <= 4):
        break

while True:
    alter = int(input('alter: '))
    if( 1 <= alter ):
        break

while True:
    weitkred = int(input('weitkred: '))
    if( 1 <= weitkred <= 3):
        break

while True:
    wohn = int(input('wohn: '))
    if( 1 <= wohn <= 3):
        break

while True:
    bishkred = int(input('bishkred: '))
    if( 1 <= bishkred <= 4):
        break

while True:
    beruf = int(input('beruf: '))
    if( 1 <= beruf <= 4):
        break

while True:
    pers = int(input('pers: '))
    if( 1 <= pers <= 2):
        break

while True:
    telef = int(input('telef: '))
    if( 1 <= telef <= 2):
        break

while True:
    gastarb = int(input('gastarb: '))
    if( 1 <= gastarb <= 2):
        break


#Inserindo os valores passados pelo usuário p/ realizar a predição - classificação
X_input = [[laufkont, laufzeit, moral, verw, hoehe, sparkont, beszeit, rate, famges, buerge, wohnzeit, verm, alter,
            weitkred, wohn, bishkred, beruf, pers, telef, gastarb]]

if classifier.predict(X_input) == 1:
    print('Bom')

if classifier.predict(X_input) == 2:
    print("Ruim")
