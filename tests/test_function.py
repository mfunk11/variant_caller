from mf_pkg import main

#ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR181/008/SRR18117708/SRR18117708_1.fastq.gz
#def test_compute_dist_gen():
    #num1 = 2
    #num2 = 7
    #expected_sum = 9
    #n_sum = main.sum(num1, num2)
    #assert n_sum == expected_sum, "The sum of 2 and 7 is 9 not" + str(sum)


#def test_lines_function():
    #file = "six-lines.txt"
    #expected_lines = 6
    #n_lines = main.read_data(file)
    #assert n_lines == expected_lines, "The expected number of lines is 6."


def test_run_star():
    gtf = 'TAIR10_GFF3_genes.gff'
    ref = 'TAIR10_chr_all.fas'
    fastq1 = 'SRR18117708_1.fastq'
    fastq2 = 'SRR18117708_2.fastq'
    expected_return = 'star --runThreadN 6 --runMode genomeGenerate --genomeDir . --genomeFastaFiles SRR18117709_1.fastq SRR18117708_2.fastq --sjdbGTFFile TAIR10_GFF3_genes.gff --sjdbOverhang 100'
    return_value = test_run_star(gtf, ref, fastq1, fastq2)
    assert expected_return == actual_return
