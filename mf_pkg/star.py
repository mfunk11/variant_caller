import sys
import os

def run_star_no_gtf(ref, fastq_1, fastq_2):
	if fastq_2 is None:
		cmd = "star --runThreadN 4 --runMode alignReads --genomeDir . --readFilesIn {fastq}"
	else:
		cmd = f"star --runThreadN 4 --runMode alignReads --genomeDir . --readFilesIn {fastq_1} {fastq_2}"

def run_star1(gtf, ref, fastq_file):
            if gtf is None:
		return run_star_no_gtf(ref, fastq_file, None)
	    else:
            	cmd = f"star --runThreadN 6 --runMode genomeGenerate --genomeDir . --genomeFastaFiles {ref} --sjdbGTFfile {gtf} --sjdbOverhang 100"
            	cmd2 = f"star --runThreadN 4 --runMode alignReads --genomeDir . --readFilesIn {fastq_file}"
            	os.system(cmd, cmd2)
	    return cmd, cmd2

def run_star2(gtf, ref, fastq_1, fastq_2):
            if gtf is None:
		return run_star_no_gtf(ref, fastq_1, fastq_2)
	    else:
            	cmd = f"star --runThreadN 6 --runMode genomeGenerate --genomeDir . --genomeFastaFiles {ref} --sjdbGTFfile {gtf} --sjdbOverhang 100"
            	os.system(cmd)
            	cmd2 = f"star --runThreadN 4 --runMode alignReads --genomeDir . --readFilesIn {fastq_1} {fastq_2}"
            	print(cmd)
            	os.system(cmd2)
        	return cmd, cmd2





run_star(sys.argv[1], sys.argv[2])










