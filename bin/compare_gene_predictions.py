#!/usr/bin/env python3.7

import sys
import logging
import argparse

from Bioinfo.GffGeneParser import GffGeneParser
from Bioinfo.SOSplicingClassifier import SOSplicingClassifier
from Bioinfo.Cluster import Cluster
from Bioinfo.MetaGene import MetaGene

class Compare(object):

    def __init__(self, inputFile):

        self.files = self.__read_inputfile(inputFile)
        genes = []
        for i in self.files:
            parser = GffGeneParser(i[0])
            genes.extend(parser.getAllCodingGenes())
        self.clusters = self.clusterize(genes)
        self.classif = { "N:O:O" : [],
                         "N:N:O" : [],
                         "N:O:N" : [],
                         "N:N:N" : [],
                         "O:N:O" : [],
                         "O:N:N" : [],
                         "O:O:N" : [],
                         "O:O:O" : []}

        self.transcripts_same_cds = []

        for i,cl in enumerate(self.clusters):
            seqid = cl.seqid
            start = min([gene.start for gene in cl.genes])
            end = max([gene.end for gene in cl.genes])
            transcripts = []
            for gene in cl.genes:
                transcripts.extend(gene.lTranscripts)
            m = MetaGene(i,seqid, start, end, transcripts)

            classif = SOSplicingClassifier.classify_gene(m, 'CDS')
            #print(f"MetaGene: {m} -- classif: {classif}")
            if (classif[0]>0 and classif[1]== 0 and classif[2] == 0):
                self.classif["N:O:O"].append(m)
            if (classif[0]>0 and classif[1]> 0 and classif[2] == 0):
                self.classif["N:N:O"].append(m)
            if (classif[0]>0 and classif[1]== 0 and classif[2] > 0):
                self.classif["N:O:N"].append(m)
            if (classif[0]>0 and classif[1]> 0 and classif[2] > 0):
                self.classif["N:N:N"].append(m)
            if (classif[0]==0 and classif[1]> 0 and classif[2] ==0):
                self.classif["O:N:O"].append(m)
#                print(f"MetaGene: {m} -- classif: {classif}")
            if (classif[0]==0 and classif[1]> 0 and classif[2] > 0):
                self.classif["O:N:N"].append(m)
            if (classif[0]==0 and classif[1]==0 and classif[2] >0):
                self.classif["O:O:N"].append(m)
                if m.have_transcripts_same_cds():
                    self.transcripts_same_cds.append(m)
                    print(f"same:{m.id}-{m.seqid}-{m.start}-{m.end}")
                else:
                    print(f"diff:{m.id}-{m.seqid}-{m.start}-{m.end}")
            if m.start == 2877969:
                print(m.have_transcripts_same_cds())
            if (classif[0]==0 and classif[1]==0 and classif[2] == 0):
                self.classif["O:O:O"].append(m)

        for k in self.classif.keys():
            print(f'{k}:{len(self.classif[k])}')

        print(len(self.transcripts_same_cds))


    def __read_inputfile(self, inputfile):

        files = []
        with open(inputfile, 'r') as f:
            for line in f:
                files.append(line.rstrip().split("\t"))
        return files

    def clusterize(self, genes):

        clusters = []
        for gene in genes:
            include = False
            for cl in clusters:
                if gene.seqid != cl.seqid:
                    next
                elif cl.is_gene_spanning(gene):
                    cl.add_gene(gene)
                    cl.start = min(cl.start, gene.get_min_cds_start())
                    cl.end = max(cl.end, gene.get_max_cds_end())
                    include = True
            if not include:
                cl = Cluster(gene.seqid, gene.get_min_cds_start(), gene.get_max_cds_end())
                cl.add_gene(gene)
                clusters.append(cl)
        print(len(clusters))
        # join spanning clusters
        merged_clusters = []
        for cl in clusters:
            merge = False
            for cl2 in merged_clusters:
                if cl.seqid != cl2.seqid:
                    next
                elif cl2.is_cluster_spanning(cl):
                    cl2 = Cluster.merge([cl2,cl])
                    merge = True
            if not merge:
                merged_clusters.append(cl)

        print(len(merged_clusters))

        return merged_clusters


if __name__ == "__main__":

    program = sys.argv[0]
    version = None
    description = "TODO"

    parser = argparse.ArgumentParser(prog=program)
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--version', action='version', version='{} {}'.format(program,version))
    parser.add_argument("-v", "--verbosity", type=int, choices=[1,2,3],
                        help="increase output verbosity 1=error, 2=info, 3=debug")
    parser.add_argument("Input", help="Input file, tab delimited, <file path><TAB><program/run>", type=str)
    args = parser.parse_args()

    logLevel='ERROR'
    if args.verbosity == 1:
        logLevel = 'ERROR'
    if args.verbosity == 2:
        logLevel = 'INFO'
    if args.verbosity == 3:
        logLevel = 'DEBUG'
    logging.getLogger().setLevel(logLevel)


    compare = Compare(args.Input)
