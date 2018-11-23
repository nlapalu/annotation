#!/usr/bin/env python3

class MetaGene(object):

    def __init__(self, id, seqid, start, end, transcripts = None):
        """init"""

        self.id = id
        self.seqid = seqid
        self.start = start
        self.end = end
        self.genes = []
        if transcripts == None:
            self.lTranscripts = []
        else:
            self.lTranscripts = transcripts

    def add_gene(self, gene):
        """add gene"""

        self.genes.append(gene)

    def have_transcripts_same_cds(self):
        """all transcsipts have same Protein"""

        for tr in self.lTranscripts:
            for tr2 in self.lTranscripts[1::]:
                if self.start == 2877969:
                    print(sorted([(x.start,x.end) for x in tr.lCDS]))
                    print(sorted([(y.start, y.end) for y in tr2.lCDS]))
                if (sorted([(x.start,x.end) for x in tr.lCDS]) != sorted([(y.start, y.end) for y in tr2.lCDS])):
                    return False
        return True

#    def __eq__(self, other):
#        """Equality on all args"""

#        return ((self.id,self.seqid,self.start,self.end,self.strand, self.lTranscripts) == (other.id, other.seqid, other.start, other.end, other.strand, other.lTranscripts))

    def __str__(self):
        """MetaGene representation"""

        return 'MetaGene: {}-{}-{}-{}'.format(self.seqid,self.start,self.end,",".join([tr.id for tr in self.lTranscripts]))

#    def __gt__(self, other):

#        return ((self.seqid, self.start) > (other.seqid, other.start))

