#!/usr/bin/env python3

class Gene(object):

    def __init__(self, id, seqid, start, end, strand):
        """init"""

        self.id = id
        self.seqid = seqid
        self.start = start
        self.end = end
        self.strand = strand
        self.type = None
        self.lTranscripts = []

    def isOnReverseStrand(self):
        """return True if strand -"""

        if self.strand == -1:
            return True
        else:
            return False

    def add_transcript(self, transcript):
        """add transcript"""

        self.lTranscripts.append(transcript)

    def is_coding(self):

        if self.type == "coding":
            return True
        else:
            False

    def get_min_cds_start(self):

        return min([tr.get_min_cds_start() for tr in self.lTranscripts])

    def get_max_cds_end(self):

        return max([tr.get_max_cds_end() for tr in self.lTranscripts])

    def __hash__(self):

        return hash(self.id)

    def __eq__(self, other):
        """Equality on all args"""
      
        return ((self.id,self.seqid,self.start,self.end,self.strand, self.lTranscripts) == (other.id, other.seqid, other.start, other.end, other.strand, other.lTranscripts))

    def __repr__(self):
        """Gene representation"""

        return 'Gene: {}-{}-{}-{}-{}-{}'.format(self.id,self.seqid,self.start,self.end,self.strand, self.lTranscripts)

    def __gt__(self, other):

        return ((self.seqid, self.start) > (other.seqid, other.start))

