import mf_pkg.star
from datetime import datetime
import urllib.request
import gzip
import shutil
import unittest
class TestSTAR(unittest.TestCase):
    
    def test_run_star2(self):
        fastq1_url = urllib.request.urlopen("ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR181/008/SRR18117708/SRR18117708_1.fastq.gz")
	print(datetime.now() + ' First file read in.')
        fastq2_url = urllib.request.urlopen("ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR181/008/SRR18117708/SRR18117708_2.fastq.gz")
	print(datetime.now() + ' Second file read in.') 
        with gzip.open(fastq1_url, 'rb') as f_in:
            with open("SRR18117708_1.fastq", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
	print(datetime.now() + ' First fastq file copied.')
	with gzip.open(fastq2_url, 'rb') as f_in2:
            with open("SRR19117708_2.fastq", 'wb') as f_out2:
                shutil.copyfileobj(f_in2, f_out2)
	print(datetime.now() + ' Second fastq file copied.') 
        gtf = urllib.request.urlopen('https://www.arabidopsis.org/download_files/Genes/TAIR10_genome_release/TAIR10_chromosome_files/TAIR10_chr_all.fas.gz')
        ref_url = urllib.request.urlopen('https://www.arabidopsis.org/download_files/Genes/TAIR10_genome_release/TAIR10_chromosome_files/TAIR10_chr_all.fas.gz')
<<<<<<< HEAD
	print(datetime.now() + 'Reference file read in.')
        with gzip.open(ref_url, 'rb') as f_in_ref:
            with open('TAIR10_chr_all.fas', 'wb') as f_out_ref:
                shutil.copyfileobj(f_in_ref, f_out_ref)
	print(datetime.now() + 'Reference file copied')
=======
        with gzip.open(ref_url, 'rb') as f_in:
            with open('TAIR10_chr_all.fas', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
>>>>>>> 591beab4cc858f3213361f14e71615ea781b7540
        expected_return = 'star --runThreadN 6 --runMode genomeGenerate --genomeDir . --genomeFastaFiles SRR18117709_1.fastq SRR18117708_2.fastq --sjdbGTFFile TAIR10_GFF3_genes.gff --sjdbOverhang 100', 'star --runThreadN 4 --runMode alignReads --readFilesIn SRR18117708_1.fastq SRR18117708_2.fastq'
        fastq1 = 'SRR18117708_1.fastq'
        fastq2 = 'SRR18117708_2.fastq'
        ref = 'TAIR10_chr_all.fas'
        return_value = star.run_star2(gtf, ref, fastq1, fastq2)
        assert expected_return == actual_return

        def test_run_star1(self):
            fastq1_url = urllib.request.urlopen("ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR181/008/SRR18117708/SRR18117708_1.fastq.gz")
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
            expected_return = 'star --runThreadN 6 --runMode genomeGenerate --genomeDir . --genomeFastaFiles SRR18117709_1.fastq --sjdbGTFFile TAIR10_GFF3_genes.gff --sjdbOverhang 100', 'star --runThreadN 4 --runMode alignReads --readFilesIn SRR18117708_1.fastq SRR18117708_2.fastq'
            fastq1 = 'SRR18117708_1.fastq'
            ref = 'TAIR10_chr_all.fas'
            return_value = star.run_star1(gtf, ref, fastq1)
            assert expected_return == actual_return

    def test_run_star_no_gtf_case1(self):
            fastq1_url = urllib.request.urlopen("ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR181/008/SRR18117708/SRR18117708_1.fastq.gz")
            with gzip.open(fastq1_url, 'rb') as f_in:
                with open("SRR18117708_1.fastq", 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            ref_url = urllib.request.urlopen('https://www.arabidopsis.org/download_files/Genes/TAIR10_genome_release/TAIR10_chromosome_files/TAIR10_chr_all.fas.gz')
            with gzip.open(ref_url, 'rb') as f_in:
                with open('TAIR10_chr_all.fas', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            expected_return = 'star --runThreadN 6 --runMode alignReads  --readFilesIn SRR18117708_1.fastq'
            fastq1 = 'SRR18117708_1.fastq'
            ref = 'TAIR10_chr_all.fas'
            return_value = star.run_star_no_gtf(ref, fastq1, None)
            assert expected_return == actual_return

    def test_run_star_no_gtf_case2(self):
        fastq1_url = urllib.request.urlopen("ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR181/008/SRR18117708/SRR18117708_1.fastq.gz")
        fastq2_url = urllib.request.urlopen("ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR181/008/SRR18117708/SRR18117708_1.fastq.gz")
        with gzip.open(fastq1_url, 'rb') as f_in:
                with open("SRR18117708_1.fastq", 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
        with gzip.open(fastq2_url, 'rb') as f_in:
                with open('SRR18117708_2.fastq', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
        expected_return = 'star --runThreadN 6 --runMode alignReads --readFilesIn SRR18117708_1.fastq SRR18117708_2.fastq'
        fastq1 = 'SRR18117708_1.fastq'
        fastq2 = 'SRR18117708_2.fastq'
        ref = 'TAIR10_chr_all.fas'
        return_value = star.run_star_no_gtf(ref, fastq1, fastq2)
        assert expected_return == actual_return







