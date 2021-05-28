import unittest
from Pr.degenerate_primers import string_for_regular, regular_shablon, find_amplicons
from Pr.Dicts import PRIMER_DICT1, PRIMER_DICT2


class DegeneratePrimersTest(unittest.TestCase):
    def test_regular_shablon(self):
        test_reg = regular_shablon('ACBD', 'GBDH')
        self.assertEqual(test_reg[0], 'TG[GCA][TCA].*G[CGT][AGT][ACT]')
        self.assertEqual(test_reg[1], 'AC[CGT][AGT].*C[GCA][TCA][TGA]')
        self.assertNotEqual(test_reg[0], 'AC[CGT][AGT].*C[GCA][TCA][TGA]')
        self.assertNotEqual(test_reg[1], 'TG[GCA][TCA].*G[CGT][AGT][ACT]')
        with self.assertRaises(ValueError):
            regular_shablon('', 'GBDHKMRSV')

    def test_string_for_regular(self):
        test_string1 = string_for_regular('ATCGBDTTC', PRIMER_DICT1)
        test_string2 = string_for_regular('GBDHKMRSV', PRIMER_DICT2)
        self.assertEqual(test_string1, 'TAGC[GCA][TCA]AAG')
        self.assertEqual(test_string2, 'G[CGT][AGT][ACT][GT][AC][AG][CG][ACG]')
        with self.assertRaises(ValueError):
            string_for_regular('', PRIMER_DICT1)
            string_for_regular('', PRIMER_DICT2)

    def test_find_amplicons(self):
        shablon = 'TGAT[GCA][TCA].*G[CGT][AGT][ACT]'
        test_amplicon = find_amplicons('/home/kate/PycharmProjects/Homework/Pr/test.fasta', shablon)
        self.assertEqual(test_amplicon, ['TGATGAGGAA', 'TGATGCCGTCTTTGTTAGCAC'])
        self.assertNotEqual(test_amplicon, [''])


if __name__ == '__main__':
    unittest.main()
