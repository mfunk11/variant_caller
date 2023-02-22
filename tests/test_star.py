from mf_pkg import main
import urllib.request

ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR181/008/SRR18117708/SRR18117708_1.fastq.gz

def test_run_star2():
    fastq1_url = urllib.request.urlopen("ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR181/008/SRR18117708/SRR18117708_1.fastq.gz")
    fastq2_url = urllib.request.urlopen("ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR181/008/SRR18117708/SRR18117708_2.fastq.gz") 
    with gzip.open(fastq1_url, 'rb') as f_in:
	with open("SRR18117708_1.fastq", 'wb') as f_out:
		shutil.copyfileobj(f_in, f_out)
	with open("SRR19117708_2.fastq", 'wb') as f_out:
		shutil.copyfileobj(f_in, f_out) 
    gtf = urllib.request.urlopen('https://www.arabidopsis.org/download_files/Genes/TAIR10_genome_release/TAIR10_chromosome_files/TAIR10_chr_all.fas.gz')
    ref_url = urllib.request.urlopen('https://www.arabidopsis.org/download_files/Genes/TAIR10_genome_release/TAIR10_chromosome_files/TAIR10_chr_all.fas.gz')
    with gzip.open(ref_url, 'rb') as f_in:
	with open('TAIR10_chr_all.fas', 'wb') as f_out:
		shutil.copyfileobj(f_in, f_out)
    expected_return = 'star --runThreadN 6 --runMode genomeGenerate --genomeDir . --genomeFastaFiles SRR18117709_1.fastq SRR18117708_2.fastq --sjdbGTFFile TAIR10_GFF3_genes.gff --sjdbOverhang 100'
    return_value = test_run_star2(gtf, ref, fastq1, fastq2)
    assert expected_return == actual_return

def test_run_star2():

