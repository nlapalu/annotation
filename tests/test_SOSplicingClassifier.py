#!/usr/bin/env python3

import unittest

from Bioinfo.SOSplicingClassifier import SOSplicingClassifier
from Bioinfo.Gene import Gene
from Bioinfo.Transcript import Transcript

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
        # gene N:O:O
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
        # gene O:N:O
        # gene O:N:N
        # gene O:O:N
        cls.gene_OON = Gene("gene_OON", "chr1", 200000, 201000, 1)
        cls.mRNA_OON_1 = Transcript("mRNA_OON_1", "chr1", 200000, 201000, 1, "gene_OON")
        cls.mRNA_OON_2 = Transcript("mRNA_OON_2", "chr1", , , 1, "gene_OON")
        cls.mRNA_OON_3 = Transcript("mRNA_OON_3", "chr1", , , 1, "gene_OON")
        cls.gene_OON.add_transcript(cls.mRNA_OON_1)
        cls.gene_OON.add_transcript(cls.mRNA_OON_2)
        cls.gene_OON.add_transcript(cls.mRNA_OON_3)



    def tearDown(self):
        """teardown"""

        pass

    @unittest.SkipTest
    def test_classify_gene(self):
        """test classify gene"""

        expected_classification = (1,1,1)
        self.assertEqual(SOSplicingClassifier.classify_gene(TestSOSplicingClassifier.gene_OOO), expected_classification)

    @unittest.SkipTest
    def test_classify_pair_of_transcript(self):
        """test classify pair of transcripts"""

        pass

    @unittest.SkipTest
    def test_are_transcripts_sequence_disjoint(self):
        """test"""

        self.assertTrue(SOSplicingClassifier.are_transcripts_sequence_disjoint(TestSOSplicingClassifier.mRNA_NOO_1,TestSOSplicingClassifier.mRNA_NOO_2))

    @unittest.SkipTest
    def test_are_transcripts_parts_disjoint(self):
        """test"""

        self.assertFalse(SOSplicingClassifier.are_transcripts_parts_disjoint(TestSOSplicingClassifier.mRNA_NOO_1,TestSOSplicingClassifier.mRNA_NOO_2))

    @unittest.SkipTest
    def test_are_transcripts_overlapping(self):
        """test"""

        self.assertFalse(SOSplicingClassifier.are_transcripts_overlapping(TestSOSplicingClassifier.mRNA_NOO_1,TestSOSplicingClassifier.mRNA_NOO_2))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSOSplicingClassifier)
    unittest.TextTestRunner(verbosity=2).run(suite)




