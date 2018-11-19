#!/usr/bin/env python3

from EMOperators import EMOperators as EM


class SOSplicingClassifier(object):

    @staticmethod
    def classify_gene(gene):
        """
            classify transcripts of a gene

            :param gene: gene to classify
            :type gene: Gene
            :return: a tuple of 3 integers, corresponding to EM-questions
            :rtype: tuple
        """

        classification=(0,0,0)
        print(len(gene.lTranscripts))
        if len(gene.lTranscripts) > 0:
            for i,t1 in enumerate(gene.lTranscripts):
                for t2 in gene.lTranscripts[i+1::]:
                    classification = tuple([sum(x) for x in zip(classification,SOSplicingClassifier.classify_pair_of_transcripts(t1,t2))])

        return classification


    @staticmethod
    def classify_pair_of_transcripts(t1, t2):
        """
            classify 

            :param t1: Transcript 1
            :param t2: Transcript 2
            :type t1: type
            :type t2: type
            :return: desc
            :rtype: type

        """

        return (1,0,1)

    @staticmethod
    def are_transcripts_sequence_disjoint(t1, t2):
        """
           Test if 2 transcripts are sequence disjoint

           Two transcripts are sequence disjoint if
           None of their exons shares any sequence
           in common.

           :param t1: Transcript 1
           :param t2: Transcript 2
           :type t1: Transcript
           :type t2: Transcript
           :return: True/False
           :rtype: bool
        """

        return EM.disjoint(t1.lExons, t2.lExons)

    @staticmethod
    def are_transcripts_parts_disjoint(t1,t2):
        """
            todo

        """

        return True

    @staticmethod
    def are_transcripts_overlapping(t1,t2):
        """
           Test if 2 transcripts are overlapping 

           Two transcripts are overlapping if at least 
           one of their exons (parts) is shared

        """

        return EM.overlap(t1, t2)
