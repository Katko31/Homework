"""
Написать программу, которая для заданного автора находит
статьи в Pubmed, создает массив из их ключевых слов, находит
статьи за последний год с использованием одного из этих
ключевых слов и возвращает гены, связанные с этими статьями.
"""

import datetime
from Bio import Entrez
from Bio import Medline
Entrez.email = "kate.smirnova.2016@gmail.com"

now = datetime.datetime.now()
prev_year = now.strftime("%d/%m/"+str(int(now.strftime("%Y"))-1))


def find_id_by_author(author):
    """находим статьи по заданному автору, сохраняем их в переменную result, возвращаем только список айдишников"""
    with Entrez.esearch(db="pubmed", term=author+"[AUTHOR]") as handle:
        result = Entrez.read(handle)

    id = result["IdList"]
    return id


def create_key_word_massiv(id):
    massiv = []
    for i in id:
        with Entrez.efetch(db="pubmed", id=i, retmode="text", rettype="medLine") as handle:
            r = Medline.read(handle)
            if 'OT' in r:
                for word in r['OT']:
                    if word not in massiv:
                        massiv.append(word)
    return massiv


def create_id_massiv(key_words):
    """получаем id статей, опубликованных в течении года, поиск осуществляется по дате и найденным ключевым словам"""
    id_list = []
    for word in key_words:
        with Entrez.esearch(db="pubmed",
                            term=word + " AND ((" + prev_year + "[Date - Completion] : " + "3000" + "[Date - Completion]))") as handle:
            rs = Entrez.read(handle)
            for i in rs["IdList"]:
                if i not in id_list:
                    id_list.append(i)
    return id_list


author = input("Введите автора статьи: ")
id_by_author = find_id_by_author(author)
key_words = create_key_word_massiv(id_by_author)
id_massiv = create_id_massiv(key_words)
print(len(key_words))
print(len(id_massiv))

# with Entrez.efetch(db="pubmed", id = id, retmode = "text", rettype = "medLine") as handle:
#     rt = Medline.read(handle)
# # result
# """выводим абстракт и ключевые слова"""
#
# print(rt['OT'])
# print(rt['AB'])
# key = rt['OT'][0]
# """получаем сптсок ключевых слов, одно для дальнейшего поиска"""
#
# for word in massive:
#     """получаем id наших новых статей, найденных по ключевым словам"""
#     with Entrez.esearch(db="pubmed", term=word + " AND ((" + prev_year + "[Date - Completion] : " + "3000" + "[Date - Completion]))") as handle:
#         rs = Entrez.read(handle)
#         """поиск новых статей по ключевому слову и дате"""
#
# id2 = rs["IdList"][0]
#
#
for i in id_massiv:
    with Entrez.elink(dbfrom="pubmed", linkname='pubmed_gene', id=i) as handle:
        rlt = Entrez.read(handle)
    if len(rlt[0]['LinkSetDb']) > 0 and len(rlt[0]['LinkSetDb'][0]['Link']) > 0:
        print([int(i['Id'])] for i in rlt[0]['LinkSetDb'][0]['Link'])

