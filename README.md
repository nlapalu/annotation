# INGENANNOT: INspection of GENe ANNOTation

INGENANNOT is a set of utilities to inspect and generate 
statistics of one or several sets of gene annotations. It allows
structure comparison and can help you to prioritize your 
effort in manual gene curation. INGENNANNOT uses among other
thnigs, the Sequence Ontology gene-splicing classification 
[(1)]() that aims to classify alternative transcripts in seven defined 
categories. 

## Inspect a simple gene annotation

## Inspect several gene annotations

## Validate your GFF/GTF file format

Despite the effort made to propose common format with rules/constraints,
GFF/GTF format are permissives and ...
We propose a simple validator to ensure that your annotation file format
will be tracted by our program.

```
ingenannot validate myfile.gff
```

In case of failure, check your file to fix the missing or required data.
If you need help, or required a specific parsing for 'exotic' format, 
feel free to contact us.     

## References

* [1-ref1]()
