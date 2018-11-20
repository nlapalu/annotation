#!/usr/bin/env python3

import unittest

from Bioinfo.SOSplicingClassifier import SOSplicingClassifier
from Bioinfo.Gene import Gene
from Bioinfo.Transcript import Transcript
from Bioinfo.Exon import Exon

class TestSOSplicingClassifier(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """setup"""

        # gene O:O:O
        cls.gene_OOO = Gene("gene_OOO", "chr1", 100, 1000, 1)
        cls.mRNA_OOO_1 = Transcript("mRNA_OOO_1", "chr1", 100, 1000, 1, "gene_OOO")
        cls.mRNA_OOO_2 = Transcript("mRNA_OOO_2", "chr1", 100, 1000, 1, "gene_OOO")
        cls.gene_OOO.add_transcript(cls.mRNA_OOO_1)
        cls.gene_OOO.add_transcript(cls.mRNA_OOO_2)
        # gene N:O:O (TODO)
        cls.gene_NOO = Gene("gene_NOO", "chr1", 2000, 3000, 1)
        cls.mRNA_NOO_1 = Transcript("mRNA_NOO_1", "chr1", 2000, 3000, 1, "gene_NOO")
        cls.mRNA_NOO_2 = Transcript("mRNA_NOO_2", "chr1", 2800, 2900, 1, "gene_NOO")
        cls.mRNA_NOO_3 = Transcript("mRNA_NOO_3", "chr1", 2400, 2750, 1, "gene_NOO")
        cls.gene_NOO.add_transcript(cls.mRNA_NOO_1)
        cls.gene_NOO.add_transcript(cls.mRNA_NOO_2)
        cls.gene_NOO.add_transcript(cls.mRNA_NOO_3)
        # gene N:N:O
        # gene N:O:N
        # gene N:N:N
        cls.gene_NNN = Gene("gene_NNN", "chr1", 2000, 3000, 1)
        cls.mRNA_NNN_1 = Transcript("mRNA_NNN_1", "chr1", 2000, 3000, 1, "gene_NNN")
        cls.mRNA_NNN_2 = Transcript("mRNA_NNN_2", "chr1", 2000, 2100, 1, "gene_NNN")
        cls.mRNA_NNN_3 = Transcript("mRNA_NNN_3", "chr1", 2000, 2100, 1, "gene_NNN")
        cls.mRNA_NNN_4 = Transcript("mRNA_NNN_4", "chr1", 2200, 2400, 1, "gene_NNN")
        cls.mRNA_NNN_5 = Transcript("mRNA_NNN_5", "chr1", 2500, 3000, 1, "gene_NNN")
        cls.exon_NNN_1 = Exon("exon_NNN_1", "chr1", 2000, 2050, 1, ["mRNA_NNN_1"])
        cls.exon_NNN_2 = Exon("exon_NNN_2", "chr1", 2000, 2100, 1, ["mRNA_NNN_2"])
        cls.exon_NNN_3 = Exon("exon_NNN_3", "chr1", 2000, 2030, 1, ["mRNA_NNN_3"])
        cls.exon_NNN_4 = Exon("exon_NNN_4", "chr1", 2040, 2100, 1, ["mRNA_NNN_3"])
        cls.exon_NNN_5 = Exon("exon_NNN_5", "chr1", 2200, 2300, 1, ["mRNA_NNN_4"])
        cls.exon_NNN_6 = Exon("exon_NNN_6", "chr1", 2350, 2400, 1, ["mRNA_NNN_4"])
        cls.exon_NNN_7 = Exon("exon_NNN_7", "chr1", 2500, 2550, 1, ["mRNA_NNN_5"])
        cls.exon_NNN_8 = Exon("exon_NNN_8", "chr1", 2600, 2650, 1, ["mRNA_NNN_1","mRNA_NNN_5"])
        cls.exon_NNN_9 = Exon("exon_NNN_9", "chr1", 2680, 2720, 1, ["mRNA_NNN_1","mRNA_NNN_5"])
        cls.exon_NNN_10 = Exon("exon_NNN_10", "chr1", 2750, 2850, 1, ["mRNA_NNN_1","mRNA_NNN_5"])
        cls.exon_NNN_11 = Exon("exon_NNN_11", "chr1", 2900, 3000, 1, ["mRNA_NNN_1","mRNA_NNN_5"])
        cls.mRNA_NNN_1.add_exon(cls.exon_NNN_1)
        cls.mRNA_NNN_1.add_exon(cls.exon_NNN_8)
        cls.mRNA_NNN_1.add_exon(cls.exon_NNN_9)
        cls.mRNA_NNN_1.add_exon(cls.exon_NNN_10)
        cls.mRNA_NNN_1.add_exon(cls.exon_NNN_11)
        cls.mRNA_NNN_2.add_exon(cls.exon_NNN_2)
        cls.mRNA_NNN_3.add_exon(cls.exon_NNN_3)
        cls.mRNA_NNN_3.add_exon(cls.exon_NNN_4)
        cls.mRNA_NNN_4.add_exon(cls.exon_NNN_5)
        cls.mRNA_NNN_4.add_exon(cls.exon_NNN_6)
        cls.mRNA_NNN_5.add_exon(cls.exon_NNN_7)
        cls.mRNA_NNN_5.add_exon(cls.exon_NNN_8)
        cls.mRNA_NNN_5.add_exon(cls.exon_NNN_9)
        cls.mRNA_NNN_5.add_exon(cls.exon_NNN_10)
        cls.mRNA_NNN_5.add_exon(cls.exon_NNN_11)
        cls.gene_NNN.add_transcript(cls.mRNA_NNN_1)
        cls.gene_NNN.add_transcript(cls.mRNA_NNN_2)
        cls.gene_NNN.add_transcript(cls.mRNA_NNN_3)
        cls.gene_NNN.add_transcript(cls.mRNA_NNN_4)
        cls.gene_NNN.add_transcript(cls.mRNA_NNN_5)
        # gene O:N:O
        # gene O:N:N
        # gene O:O:N
        cls.gene_OON = Gene("gene_OON", "chr1", 1000,2000, 1)
        cls.mRNA_OON_1 = Transcript("mRNA_OON_1", "chr1", 1000, 2000, 1, "gene_OON")
        cls.mRNA_OON_2 = Transcript("mRNA_OON_2", "chr1", 1500, 2000, 1, "gene_OON")
        cls.mRNA_OON_3 = Transcript("mRNA_OON_3", "chr1", 1600, 2000, 1, "gene_OON")
        cls.exon_OON_1 = Exon("exon_OON_1", "chr1", 1000, 1009, 1, ["mRNA_NOO_1"])
        cls.exon_OON_2 = Exon("exon_OON_2", "chr1", 1300, 1350, 1, ["mRNA_NOO_1"])
        cls.exon_OON_3 = Exon("exon_OON_3", "chr1", 1400, 1450, 1, ["mRNA_NOO_1"])
        cls.exon_OON_4 = Exon("exon_OON_4", "chr1", 1500, 1530, 1, ["mRNA_NOO_2"])
        cls.exon_OON_5 = Exon("exon_OON_5", "chr1", 1600, 1650, 1, ["mRNA_NOO_1","mRNA_OON_2"])
        cls.exon_OON_6 = Exon("exon_OON_6", "chr1", 1670, 1720, 1, ["mRNA_NOO_1","mRNA_OON_2","mRNA_OON_3"])
        cls.exon_OON_7 = Exon("exon_OON_7", "chr1", 1750, 1800, 1, ["mRNA_NOO_1","mRNA_OON_2","mRNA_OON_3"])
        cls.exon_OON_8 = Exon("exon_OON_8", "chr1", 1820, 1870, 1, ["mRNA_NOO_1","mRNA_OON_2","mRNA_OON_3"])
        cls.exon_OON_9 = Exon("exon_OON_9", "chr1", 1920, 2000, 1, ["mRNA_NOO_1","mRNA_OON_2","mRNA_OON_3"])
        cls.mRNA_OON_1.add_exon(cls.exon_OON_1)
        cls.mRNA_OON_1.add_exon(cls.exon_OON_2)
        cls.mRNA_OON_1.add_exon(cls.exon_OON_3)
        cls.mRNA_OON_1.add_exon(cls.exon_OON_5)
        cls.mRNA_OON_1.add_exon(cls.exon_OON_6)
        cls.mRNA_OON_1.add_exon(cls.exon_OON_7)
        cls.mRNA_OON_1.add_exon(cls.exon_OON_8)
        cls.mRNA_OON_1.add_exon(cls.exon_OON_9)
        cls.mRNA_OON_2.add_exon(cls.exon_OON_4)
        cls.mRNA_OON_2.add_exon(cls.exon_OON_5)
        cls.mRNA_OON_2.add_exon(cls.exon_OON_6)
        cls.mRNA_OON_2.add_exon(cls.exon_OON_7)
        cls.mRNA_OON_2.add_exon(cls.exon_OON_8)
        cls.mRNA_OON_2.add_exon(cls.exon_OON_9)
        cls.mRNA_OON_3.add_exon(cls.exon_OON_6)
        cls.mRNA_OON_3.add_exon(cls.exon_OON_7)
        cls.mRNA_OON_3.add_exon(cls.exon_OON_8)
        cls.mRNA_OON_3.add_exon(cls.exon_OON_9)
        cls.gene_OON.add_transcript(cls.mRNA_OON_1)
        cls.gene_OON.add_transcript(cls.mRNA_OON_2)
        cls.gene_OON.add_transcript(cls.mRNA_OON_3)


    def tearDown(self):
        """teardown"""

        pass

#    @unittest.SkipTest
    def test_classify_gene(self):
        """test classify gene"""

        expected_classification = (3,0,0)
        self.assertEqual(SOSplicingClassifier.classify_gene(TestSOSplicingClassifier.gene_NOO), expected_classification)
        expected_classification = (0,0,3)
        self.assertEqual(SOSplicingClassifier.classify_gene(TestSOSplicingClassifier.gene_OON), expected_classification)
        expected_classification = (6,3,1)
        self.assertEqual(SOSplicingClassifier.classify_gene(TestSOSplicingClassifier.gene_NNN), expected_classification)

#    @unittest.SkipTest
    def test_classify_pair_of_transcript(self):
        """test classify pair of transcripts"""

        expected_classification = (1,0,0)
        self.assertEqual(SOSplicingClassifier.classify_pair_of_transcripts(TestSOSplicingClassifier.mRNA_NOO_1, TestSOSplicingClassifier.mRNA_NOO_2), expected_classification)
        self.assertEqual(SOSplicingClassifier.classify_pair_of_transcripts(TestSOSplicingClassifier.mRNA_NOO_1, TestSOSplicingClassifier.mRNA_NOO_3), expected_classification)
        self.assertEqual(SOSplicingClassifier.classify_pair_of_transcripts(TestSOSplicingClassifier.mRNA_NOO_2, TestSOSplicingClassifier.mRNA_NOO_3), expected_classification)
        expected_classification = (0,0,1)
        self.assertEqual(SOSplicingClassifier.classify_pair_of_transcripts(TestSOSplicingClassifier.mRNA_OON_1, TestSOSplicingClassifier.mRNA_OON_2), expected_classification)
        self.assertEqual(SOSplicingClassifier.classify_pair_of_transcripts(TestSOSplicingClassifier.mRNA_OON_1, TestSOSplicingClassifier.mRNA_OON_3), expected_classification)
        self.assertEqual(SOSplicingClassifier.classify_pair_of_transcripts(TestSOSplicingClassifier.mRNA_OON_2, TestSOSplicingClassifier.mRNA_OON_3), expected_classification)

    @unittest.SkipTest
    def test_are_transcripts_sequence_disjoint(self):
        """test"""

        self.assertTrue(SOSplicingClassifier.are_transcripts_sequence_disjoint(TestSOSplicingClassifier.mRNA_NOO_1,TestSOSplicingClassifier.mRNA_NOO_2))

    @unittest.SkipTest
    def test_are_transcripts_parts_disjoint(self):
        """test"""

        self.assertFalse(SOSplicingClassifier.are_transcripts_parts_disjoint(TestSOSplicingClassifier.mRNA_NOO_1,TestSOSplicingClassifier.mRNA_NOO_2))

#    @unittest.SkipTest
    def test_are_transcripts_overlapping(self):
        """test"""

        #self.assertFalse(SOSplicingClassifier.are_transcripts_overlapping(TestSOSplicingClassifier.mRNA_NOO_1,TestSOSplicingClassifier.mRNA_NOO_2))
        self.assertTrue(SOSplicingClassifier.are_transcripts_overlapping(TestSOSplicingClassifier.mRNA_OON_1,TestSOSplicingClassifier.mRNA_OON_2))
        self.assertTrue(SOSplicingClassifier.are_transcripts_overlapping(TestSOSplicingClassifier.mRNA_OON_1,TestSOSplicingClassifier.mRNA_OON_3))
        self.assertTrue(SOSplicingClassifier.are_transcripts_overlapping(TestSOSplicingClassifier.mRNA_OON_2,TestSOSplicingClassifier.mRNA_OON_3))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSOSplicingClassifier)
    unittest.TextTestRunner(verbosity=2).run(suite)




