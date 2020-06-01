# *De novo* assembly and analysis of pogonophore *Siboglinum fiordicum* transcriptome at different larval stages

---
![venn diagramm of diffexpression](venn_diagramm.jpg "venn diagramm of diffexpression")
![heat map of orthogroups](orthogroups.jpg "heat map of orthogroups")

## Aim of the project: 

To study the molecular basis for the segmentation of *Siboglinum fiordicum* using transcriptomic data from different stages of the life cycle.

### Objectives 

- *de novo* transcriptome assembly of a non-model organism 
- expression analysis at different stages of development

## Methods
- RNAseq libraries from 3 trochophores (before and after septum formation) and an adult organism were analyzed
- primary quality control and raw data preparation were performed with FastQC, Karect, FastP
- *de novo* assembly with Trinity
- sequence clusterization (CDHIT-est) 
- estimation of the completeness (BUSCO) and quality (TransRate) of assembly, filtering contigs with low scores
- determinaion of possible contamination by analyzing ribosome subunits sequences (RNAmmer) and transcriptome composition (BlobTools), filtering ribosomal, prokaritic (bacterial and archaeal), protists', vertebrate sequences
- expression quantification with Salmon (v1.0.1)
- the determination of encoded amino acid sequences using a two-step analysis of TransDecoder
- annotation (NCBInt, NCBInr, SwissProt, PfamA, and eggNOG databases)
- co-expression clusters building (Clust)
- Construction of orthogroups using OrthoFinder and filtered reference sets of proteins from two other Annelida species: *Capitella teleta* and *Helobdella robusta*
- pathway enrichment analysis (GeneOntology) of “genes” with predominant expression at a particular stage of the cycle

## References
__Articles__

__Databases__
- https://www.ncbi.nlm.nih.gov/nucleotide/
- https://www.ncbi.nlm.nih.gov/protein/
- https://pfam.xfam.org/
- https://www.uniprot.org/
- http://eggnog-mapper.embl.de/

__Tools__
