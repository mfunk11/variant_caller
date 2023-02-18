import sys
import os


def run_star(gtf, ref):
    if (len(sys.argv) != 4) and (len(sys.argv) != 5):
        print("usage: [gtf][reference genome][fastq_1](fastq_2)")
    else:
        if len(sys.argv) == 4:
            fastq_file = sys.argv[3]
            cmd = f"star --runThreadN 6 --runMode genomeGenerate --genomeDir . --genomeFastaFiles {ref} --sjdbGTFfile {gtf} --sjdbOverhang 100"
            print(cmd)
            os.system(cmd)

            cmd2 = f"star --runThreadN 4 --runMode alignReads --genomeDir . --readFilesIn {fastq_file}"
            os.system(cmd2)

        elif len(sys.argv) == 5:
            fastq_1 = sys.argv[3]
            fastq_2 = sys.argv[4]
            cmd = f"star --runThreadN 6 --runMode genomeGenerate --genomeDir . --genomeFastaFiles {ref} --sjdbGTFfile {gtf} --sjdbOverhang 100"
            print(cmd)
            os.system(cmd)
            cmd2 = f"star --runThreadN 4 --runMode alignReads --genomeDir . --readFilesIn {fastq_1} {fastq_2}"
            print(cmd)
            os.system(cm
        return cmd, cmd2




run_star(sys.argv[1], sys.argv[2])










