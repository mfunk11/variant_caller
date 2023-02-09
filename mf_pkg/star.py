import sys
import os


if (len(sys.argv) != 4) and (len(sys.argv) != 5):
    print("usage: [gtf][reference genome][fastq_1](fastq_2)")
else:
    gtf= sys.argv[1]
    ref = sys.argv[2]
    if len(sys.argv) == 4:
        fastq = sys.argv[3]
        cmd = f"star --runThreadN 6 --runMode genomeGenerate --genomeDir . --genomeFastaFiles {ref} --sjdbGTFfile {gtf} --sjdbOverhang 100"
        print(cmd)
        os.system(cmd)

        cmd2 = f"star --runThreadN 4 --runMode alignReads --genomeDir . --readFilesIn {fastq}"
        os.system(cmd2)

    elif len(sys.argv) == 5:
        fastq_1 = sys.argv[3]
        fastq_2 = sys.argv[4]
        cmd = f"star --runThreadN 6 --runMode genomeGenerate --genomeDir . --genomeFastaFiles {ref} --sjdbGTFfile {gtf} --sjdbOverhang 100"
        print(cmd)
        os.system(cmd)
        cmd2 = f"star --runThreadN 4 --runMode alignReads --genomeDir . --readFilesIn {fastq_1} {fastq_2}"
        print(cmd)
        os.system(cmd2)










