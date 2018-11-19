#!/usr/bin/env python3

class Gene(object):

    def __init__(self, id, seqid, start, end, strand):
        """init"""

        self.id = id
        self.seqid = seqid
        self.start = start
        self.end = end
        self.strand = strand
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

    def __eq__(self, other):
        """Equality on all args"""
      
        return ((self.id,self.seqid,self.start,self.end,self.strand, self.lTranscripts) == (other.id, other.seqid, other.start, other.end, other.strand, other.lTranscripts))

    def __repr__(self):
        """Gene representation"""

        return 'Gene: {}-{}-{}-{}-{}-{}'.format(self.id,self.seqid,self.start,self.end,self.strand, self.lTranscripts)

    def __gt__(self, other):

        return ((self.seqid, self.start) > (other.seqid, other.start))

