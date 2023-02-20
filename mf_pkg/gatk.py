import os

def run_mark_duplicates_spark(name, bam):
    cmd = f"gatk MarkDuplicatesSpark -I {bam} -O {bam}.marked_duplicates -M {name}.sort.md.metricts.txt"
    os.system(cmd)
    return cmd

def run_bqsr(dup_bam, ref, bed):
    cmd = f"gatk BaseRecalibrator -I {dup_bam} -R{ref}, --known-sites {bed}, -O recal-table.table"
    os.system(cmd)


def run_qual_cab(dup_bam, ref, bed):
    run_bqsr(dup_bam, ref, bed)
    cmd = f"gatk ApplyBQSR -R {ref} -I {dup_bam} --bqsr-recal-file recal-table.table -O output.bam"
    os.system(cmd)
    return(cmd)

def run_haplotype_caller(name, dup_bam, ref, bed):
    cmd = f"gatk HaplotypeCaller -R {ref} -I {dup_bam} -O {name}.g.vcf.gz"
    os.system(cmd)
    return cmd

def run_gatk(name, bam, ref, bed):
    cmd1 = run_mark_duplicates_spark(name, bam)
    print("Ran Mark Duplicates.")
    cmd2 = run_qual_cab(bam, ref, bed)
    print("Ran Base Recalibration")
    cmd3 = run_haplotype_caller(name, bam, ref, bed)
    print("GATK run successfully.")