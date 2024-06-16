# Zaczynamy od zaÅ‚adowania bibliotek. Te najpopularniejsze to
# pandas - do pracy z danymi
# matplotlib - do rysowania wykresow
# sklearn - zawierajÄ…cy gotowe funkcje modelujÄ…ce dane
 
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
# tutaj ładujemy dane do obiektu data frame z biblioteki pandas
# plik CSV nie posiada nagłówka dlatego header=None
# kolumnom nadajemy nazwy korzystając z parametru names
# W skryptach ML dane trzeba skądś pobrać, stad znajomość polecenia 
# read_csv jest super przydatna
 
iris = pd.read_csv(r"F:\Repozytoria\IntrotoML\data\iris.csv",
                   header = None, 
                   names = ['petal length', 'petal width', 
                            'sepal length', 'sepal width', 'species'])

# dalej przygotowujemy wykres - tutaj wyznaczenie wartości min i max dla 
# 2 wybranych kolumn z rozmiarami kwiatów. Kiedy chcesz się odwołać do całej kolumny w data frame,
 
# każdy gatunek ma być wyświetlony w innym kolorze - definiujemy słownik
colors = {'Iris-setosa':'red', 'Iris-versicolor':'blue', 'Iris-virginica':'green'}
 
# tworzymy obiekt odpowiedzialny za rysowany wykres i jego współrzędne
# instrukcje odtąd aż do plt.show() uruchom zaznaczając cały ten blok kodu
colors = {'Iris-setosa':'red', 'Iris-versicolor':'blue', 'Iris-virginica':'green'}
 
# tworzymy obiekt odpowiedzialny za rysowany wykres i jego współrzędne
# instrukcje odtąd aż do plt.show() uruchom zaznaczając cały ten blok kodu
fig, ax = plt.subplots(figsize=(8, 6))
 
# grupujemy dane ze względu na gatunek i rysujemy dane. Korzystamy tu z metody groupby obiektu data frame
# funkcja zwraca klucz identyfikujący nazwę grupy (tutaj jest to nazwa gatunku kwiatu) oraz
# próbki wchodzące w skład tej grupy. To pozwala rysować każdą grupę w innym kolorze
for key, group in iris.groupby(by='species'):
    plt.scatter(group['petal length'], group['petal width'], c=colors[key], label=key)
 
# dodajemy legendę i opis osi
ax.legend()
ax.set_title("IRIS DATASET CATEGORIZED")
 
plt.show()
 
# teraz podobny wykres można sporządzić dla sepal
# pamiętaj o uruchomieniu mając zaznaczony blok kodu odtąd aż do plt.show()
# kroki są takie same jak w poprzednim przykładzie
 
colors = {'Iris-setosa':'red', 'Iris-versicolor':'blue', 'Iris-virginica':'green'}
 
fig, ax = plt.subplots(figsize=(8, 6))
 
for key, group in iris.groupby(by='species'):
    # funkcja scatter przyjmuje argumenty - współrzędne X punktów, współrzędne Y punktów,
    # kolor i nazwę rysowanej grupy
    plt.scatter(group['sepal length'], group['sepal width'], 
                c=colors[key], label=key)
 
ax.legend()
ax.set_title("IRIS DATASET CATEGORIZED")
 
plt.show()
# utwórz wykres składający się z 4 małych wykresów
fig, ax = plt.subplots(2,2,figsize=(10, 6))
 
# aktualnie rysowanie odbędzie się w określonym pod-wykresie
plt_position = 1
 
# obrazujemy zależność miedzy tą zmienną, a pozostałymi cechami próbek
feature_x= 'petal width'
 
# dla każdej cechy opisującej kwiaty
for feature_y in iris.columns[:4]:
 
    # wybierz kolejny pod wykres
    plt.subplot(2, 2, plt_position) 
 
    # i rysuj osobne wykresy dla każdego gatunku (te 3 rysowane tu wykresy
    # nakładają sie na siebie, co pozwala automatycznie generować legendę)
    for species, color in colors.items():
        # podczas rysowanie należy odfiltrować tylko kwiaty jednego gatunku
        # zobacz jak filtrować dane. Służy do tego funkcja loc wywoływana dla data frame
        # wyrażenie w nawiasie kwadratowym ma zwracać True/False. Zwrócone będą wiersze,
        # gdzie wyrażenie ma wartość True. Po przecinku znajduje się nazwa kolumny, która ma być zwrócona
        plt.scatter(iris.loc[iris['species']==species, feature_x],
                    iris.loc[iris['species']==species, feature_y],
                    label=species,
                    alpha = 0.45, # transparency
                    color=color)
 
    # opisujemy wykres
    plt.xlabel(feature_x)
    plt.ylabel(feature_y)
    plt.legend()
    plt_position += 1
 
plt.show()
# Zamiast analizować każdą parę niezależnie można generować tzw. scatter matrix,
# czyli gotową macierz z wykresami dla każdej pary właściwości
# tutaj wykorzystujemy funkcję scatter_matrix zaimplementowaną w pandas...
# Do wyznaczenia koloru skorzystaliśmy z funkcji apply. Pozwala ona wywołać prostą funkcję na rzecz
# każdego wiersza z data frame lub serii danych
pd.plotting.scatter_matrix(iris, figsize=(8, 8), 
                           color = iris['species'].apply(lambda x: colors[x]));
plt.show()
 
# ... a tutaj podobny wykres generowany przez funkcję pairplot z modułu seaborn
import seaborn as sns
sns.set()
sns.pairplot(iris, hue="species")