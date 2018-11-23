#!/usr/bin/env python

import logging
import re

from Bioinfo.Gene import Gene
from Bioinfo.Transcript import Transcript
from Bioinfo.Exon import Exon
from Bioinfo.CDS import CDS

class GffGeneParser(object):

    def __init__(self, inputGffFile="", logLevel='ERROR'):
        """Constructor"""

        self.inputGffFile = inputGffFile
        self.logLevel = logLevel
        logging.basicConfig(level=self.logLevel) 
        self.lGenes = []

        self._parse()


    def getAllGenes(self):
        """Get all genes"""

        return self.lGenes

    def getAllCodingGenes(self):
        """Get all coding genes"""

        return [gene for gene in self.lGenes if gene.is_coding() and gene.seqid == 'chr10']
        #return [gene for gene in self.lGenes if gene.is_coding()]

    def _parse(self):
        """Parse the gff file"""

        dGenes = {}
        dTranscripts = {}
        dCDS = {}

        with open(self.inputGffFile, 'r') as input:
            for line in input:
                if not re.match('^#', line):
                    line = line.rstrip('\n')
                    values = line.split('\t')

                    if values[2] == 'gene':
                        id = self._getFeatureTagValue('ID',values[8])
                        currentGene = Gene(id, values[0], int(values[3]), int(values[4]), self._getStrand(values[6]))
                        dGenes[id] = currentGene
                        self.lGenes.append(currentGene)

                    if values[2] == 'mRNA' or values[2] == 'tRNA' or values[2] == 'ncRNA':
                        id = self._getFeatureTagValue('ID',values[8])
                        gene_id = self._getFeatureTagValue('Parent', values[8])
                        currentTranscript = Transcript(id, values[0], int(values[3]), int(values[4]), self._getStrand(values[6]), gene_id)
                        dTranscripts[id] = currentTranscript

                        if len(dGenes[gene_id].lTranscripts) > 0:
                            dGenes[gene_id].lTranscripts.append(currentTranscript)
                        else:
                            dGenes[gene_id].lTranscripts = [currentTranscript]

                    if values[2] == 'mRNA':
                        dGenes[gene_id].type = 'coding'
                    if values[2] == 'tRNA':
                        dGenes[gene_id].type = 'transfert'
                    if values[2] == 'ncRNA':
                        dGenes[gene_id].type = 'noncoding'

                    if values[2] == 'exon':
                        id = self._getFeatureTagValue('ID',values[8])
                        lTranscript_ids = self._getFeatureTagValues('Parent', values[8])
                        currentExon = Exon(id, values[0], int(values[3]), int(values[4]), self._getStrand(values[6]), lTranscript_ids)
                        for transcript_id in lTranscript_ids:
                            if len(dTranscripts[transcript_id].lExons) > 0:
                                dTranscripts[transcript_id].lExons.append(currentExon)
                            else:
                                dTranscripts[transcript_id].lExons = [currentExon]

                    if values[2] == 'CDS':
                        id = self._getFeatureTagValue('ID',values[8])
                        transcript_id = self._getFeatureTagValue('Parent', values[8])
                        currentCDS = CDS(id, values[0], int(values[3]), int(values[4]), self._getStrand(values[6]), transcript_id)
                        if len(dTranscripts[transcript_id].lCDS) > 0:
                            dTranscripts[transcript_id].lCDS.append(currentCDS)
                        else:
                            dTranscripts[transcript_id].lCDS = [currentCDS]
                        

    def _getFeatureTagValue(self, tag, line):
        """Return the fist value of the tag property"""
        m = re.search(r".*{mytag}=([^;]*);{{0,1}}.*".format(mytag = tag),line)
        if m:
#            print "ID {}".format(m.group(1))
            return m.group(1).split(',')[0]
        else:
            raise Exception('Cannot find tag {} in string \'{}\''.format(tag, line))

    def _getFeatureTagValues(self, tag, line):
        """Return the list of values of the tag property"""
        m = re.search(r".*{mytag}=([^;]*);{{0,1}}.*".format(mytag = tag),line)
        if m:
            return m.group(1).split(',')
        else:
            raise Exception('Cannot find tag {} in string \'{}\''.format(tag, line))


    def _getStrand(self, strand):
        """Return strand as integer(1,-1) instead of +,- """

        if strand == '+':
            return 1
        elif strand == '-':
            return -1
        else:
            raise Exception('Cannot defined strand for feature')

