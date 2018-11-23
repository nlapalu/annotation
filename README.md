# INGENANNOT: INspection of GENe ANNOTation

INGENANNOT is a set of utilities to inspect and generate 
statistics for one or several sets of gene annotations. It allows
structure comparison and can help you to prioritize your 
efforts in manual curation. INGENNANNOT uses among other
things, the Sequence Ontology gene-splicing classification 
[(1)]() that aims to classify alternative transcripts in seven 
categories. 


As described above, this classification is based on exon boundaries,
that could be highly problematic for de-novo annotations with poorly
defined UTR parts. To avoid such problem, you can choose to perform
the same classification based on CDS coordinates. In this case you 
will obtained less biased results.

## Inspect a simple gene annotation

## Inspect several gene annotations

In case of several annotations, gene boundaries are often different
(especially if you tried to predict UTR regions), that implies to
clusterize gene, to propose new loci sharing a list of transcripts.
We define these new loci as 'meta-gene' and propose several methods
to clusterize them:
* cds-span: 
* gene-span:
* oriented: complete `cds-span` and `gene-span` but take into account
strand orientation 

 

## Validate your GFF/GTF file format

Despite the effort made to propose common format with rules/constraints,
GFF/GTF format are permissive and contents could be misunderstood 
during file parsing.

We propose a simple validator to ensure that your annotation file format
is supported by our program.

```
ingenannot validate myfile.gff
```

In case of failure, check your file to fix the missing or required data.
If you need help, or required a specific parser for your 'exotic' format, 
feel free to contact us.     

## References

* [1-ref1]()
