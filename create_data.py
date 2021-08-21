import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()

import string
import timeit
from random import choice, random, randint
from projeto.produto.models import Produto


class Utils:  # para gerar numeros aleatorios
    '''Métodos genéricos'''

    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))


class ProdutoClass:

    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                produto=produto,
                importado=choice((True, False)),
                ncm=Utils.gen_digits(8),
                preco=random() * randint(10, 50),
                    estoque = randint(10, 200),
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)

produtos = (
    'Brahma Lata',
    'Antartica Lata',
    'Heinekein Lata',
    'Original Lata',
    'Baden 600ml',
    'Serramalte Lata',
    'Coxinha',
    'Brahma Litro',
    'Amendoim',
    'Guaraná Lata',
    'Suco de laranja',
    'Paçoca',
    'Água',
    'Sprite Lata',
    'Skol Litrão',
    'Torcida',
)

tic = timeit.default_timer()

ProdutoClass.criar_produtos(produtos)

toc = timeit.default_timer()

print('Tempo:', toc - tic)
