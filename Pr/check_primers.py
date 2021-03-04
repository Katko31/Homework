import unittest
from degenerate_primers import string_for_regular, regular_shablon, find_amplicons
import Dicts

class PrimerCase(unittest.TestCase):

    def test_regular_shablon(self):
        test_reg = regular_shablon('ATCGBDTTC', 'GBDHKMRSV')
        self.assertEqual(test_reg, 'TAGC[GCA][TCA]AAG([ATGC]{32,132})G[CGT][AGT][ACT][GT][AC][AG][CG][ACG]')
        self.assertNotEqual(test_reg, '([ATGC]{32,132})')
        with self.assertRaises(ValueError):
            regular_shablon('', 'GBDHKMRSV')

    def test_string_for_regular(self):
        test_string1 = string_for_regular('ATCGBDTTC', Dicts.PRIMER_DICT1)
        test_string2 = string_for_regular('GBDHKMRSV', Dicts.PRIMER_DICT2)
        self.assertEqual(test_string1, 'TAGC[GCA][TCA]AAG')
        self.assertEqual(test_string2, 'G[CGT][AGT][ACT][GT][AC][AG][CG][ACG]')
        with self.assertRaises(ValueError):
            string_for_regular('', Dicts.PRIMER_DICT1)
            string_for_regular('', Dicts.PRIMER_DICT2)

    def test_find_amplicons(self):
        test_amplicon = find_amplicons('spades_scaffolds.fasta', regular_shablon('ATCGBDTTC', 'GBDHKMRSV'))
        test_result = ['CATCGTACACACCTGTGCTAGTAACACCACCA', 'GCCAAAGAGAGTGGCGAACGCGGCCTCCGTAAC', 'AAGATCTCGATGAACTCGAACAGCTCCTCGTCG']
        self.assertEqual(test_amplicon, test_result)


if __name__ == '__main__':
    unittest.main()
