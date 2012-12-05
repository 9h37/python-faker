import random

from faker.generators.name import first_name, last_name
from faker.generators.utils import numerify, letterify, bothify

def fr_phone_number():
    return numerify('0#########')

def fr_zip_code():
    return numerify('#####')

def fr_street_suffix():
    return random.choice("""Allee Avenue Rue Passage Centre Place Quartier Boulevard""".split())

def fr_street_name():
    return random.choice([
        ' '.join([fr_street_suffix(), last_name()]),
        ' '.join([fr_street_suffix(), first_name()])
    ])

def fr_street_address():
    addr = numerify(random.choice([
        '##### %s' % fr_street_name(),
        '#### %s' % fr_street_name(),
        '### %s' % fr_street_name()
    ]))
    return addr

def fr_ville():
    return random.choice(['Lille', 'Roubaix', 'Tourcoing', 'Lambersart', 'La Madeleine'])


def fr_formater(formatage):
    """ retourne une chaine aleatoire suivant le formatage """
    return bothify(formatage)

def fr_nir_cle(valeur):
    tmp_nir = valeur.replace('2A', '19')
    tmp_nir = tmp_nir.replace('2B', '18')

    return '{0:0>2}'.format(97 - int(tmp_nir) % 97)

def fr_identifiant_cle(valeur):
    resultat = ''
    cle = 0

    for (index, chiffre) in enumerate(reversed(valeur)):
        if ord(chiffre) < 65:
            current = chiffre
        else:
            current = chr((ord(chiffre) - 64))

        if (index + 1) % 2:
            resultat += str(2 * int(current))
        else:
            resultat += current

    for chiffre in resultat:
        cle += int(chiffre)

    return str((10 - cle % 10) % 10)
