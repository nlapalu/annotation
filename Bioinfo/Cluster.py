#!/usr/bin/env python3

class Cluster(object):

    def __init__(self, seqid, start, end, genes=None):
        """init"""

#        self.id = id
        self.seqid = seqid
        self.start = start
        self.end = end
        if genes == None:
            self.genes = []
        else:
            self.genes = genes

    @classmethod
    def merge(cls,clusters):
        """merge list of clusters"""

        seqid = clusters[0].seqid
        start = min([cl.start for cl in clusters])
        end = max([cl.end for cl in clusters])
        genes = []
        for cl in clusters:
            genes.extend(cl.genes)
        #print(genes)
        genes = set(genes)
        #print(genes)
        return cls(seqid,start,end,genes)

    def add_gene(self, gene):
        """add gene"""

        self.genes.append(gene)

    def is_cluster_spanning(self, cluster):
        """todo"""

        if self.start <= cluster.start <= self.end:
            return True
        if self.start <= cluster.end <= self.end:
            return True
        if cluster.start <= self.start and cluster.end >= self.end:
            return True
        return False



    def is_gene_spanning(self, gene):
        """todo"""

        if self.start <= gene.get_min_cds_start() <= self.end:
            return True
        if self.start <= gene.get_max_cds_end() <= self.end:
            return True
        if gene.get_min_cds_start() <= self.start and gene.get_max_cds_end() >= self.end:
            return True
        return False


#    def __eq__(self, other):
#        """Equality on all args"""

#        return ((self.id,self.seqid,self.start,self.end,self.strand, self.lTranscripts) == (other.id, other.seqid, other.start, other.end, other.strand, other.lTranscripts))

    def __str__(self):
        """Cluster representation"""

        return 'Cluster: {}-{}-{}-{}'.format(self.seqid,self.start,self.end,self.genes)

#    def __gt__(self, other):

#        return ((self.seqid, self.start) > (other.seqid, other.start))

