library(topGO)


Sfio_geneID2GO <- readMappings(file='/Path/to/GO_terms_table.tsv') 
Sfio_geneNames <- names(Sfio_geneID2GO)

### Sets of sequences with stage-associated expression ###
Lib_associated <- read.csv('/Path/to/library-specific_genes_table.txt', header=F)

### GO-enrichment analysis ###
Sfio_stage_specific_genes <- factor(as.integer(Sfio_geneNames %in% Lib_associated$V1))
names(Sfio_stage_specific_genes) <- Sfio_geneNames
GOdata_Sfio_stage_BP <- new("topGOdata", ontology="BP", allGenes=Sfio_stage_specific_genes,
                            annot=annFUN.gene2GO, gene2GO=Sfio_geneID2GO)
resultsFisher_Sfio_stage_BP <- runTest(GOdata_Sfio_stage_BP, algorithm='classic', statistic='fisher')
resultsFisher_Sfio_stage_BP     # get number of terms with p-value < 0.01

results_Sfio_stage_BP <- GenTable(GOdata_Sfio_stage_BP, classicFisher=resultsFisher_Sfio_stage_BP,
                                ranksOf='classicFisher', topNodes= # insert number of terms)
Sfio_stage_BP_significant <- subset(results_Sfio_stage_BP, Significant >= 10)
write.table(Sfio_stage_BP_significant, file='good.Sfio_ref.clustered.stage_GOenrichment_BP_Fisher.min_10_genes.tsv',
            sep='\t', quote=F, col.names=T, row.names=F)
