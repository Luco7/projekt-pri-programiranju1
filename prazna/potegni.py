import orodja
import re

def potegni():
    for stran in range(1, 422, 4):
        osnovni_naslov = 'https://ratings.fide.com/toparc.phtml'
        parametri = '?cod='
        naslov = '{}{}{}'.format(osnovni_naslov, parametri, stran)
        datoteka = 'lista/{:003}.html'.format(stran)
        orodja.shrani(naslov, datoteka)

potegni()