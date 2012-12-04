import random

#from faker.generators.name import first_name, last_name
from faker.generators.utils import numerify, letterify, bothify

def fr_phone_number():
    return numerify('0#########')

def fr_zip_code():
    return numerify('#####')

def fr_street_suffix():
    return random.choice("""Allee Avenue Rue Passage Centre Place Quartier Boulevard""".split())

def fr_street_name():
    return random.choice([
        ' '.join([last_name(), street_suffix()]),
        ' '.join([first_name(), street_suffix()])
    ])

def fr_street_address():
    addr = numerify(random.choice([
        '##### %s' % street_name(),
        '#### %s' % street_name(),
        '### %s' % street_name()
    ]))
    return addr

def fr_nir():
    return numerify('3############')

def fr_nir_cle(vallien):
    tmp_nir = vallien.replace('2A', '19')
    tmp_nir = tmp_nir.replace('2B', '18')

    return '{0:0>2}'.format(97 - int(tmp_nir) % 97)
