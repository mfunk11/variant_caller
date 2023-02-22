import star
import gatk
import argparse
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument("--name", help= 'The name of the sample.', default=f"{datetime.now()}-run")
parser.add_argument("--fastq1", help='A fastq file.', required=True)
parser.add_argument("--fastq2", help='A second fastq file from paired-end analysis.', default=None)
parser.add_argument("--ref", help='A reference genome.', required=True)
parser.add_argument("--gtf", help='A genome annotation file.', default=None)
parser.add_argument("--bed", help='A bed file with known polymorphisms', default=None)

args = parser.parse_args()

if args.fastq2 is None:
    star.run_star1(args.gtf, args.ref, args.fastq1)
else:
    star.run_star2(args.gtf, args.ref, args.fastq1, args.fastq2)


gatk.run_gatk(args.name, f"{args.name}.bam.sortedByCoordinate", args.ref, args.bed)

