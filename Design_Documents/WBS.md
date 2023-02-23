Project Input: Single or Paired end fastq files; reference genome
Project Output: Genome Browser Pop-up Window with highlighted variants

- [x] Task 1: Develop the Alignment Pipeline
 - [x] 1.1 - write code to generate index in STAR
   - [x] 1.1.1- use STAR reference genome
 - [x] 1.2 - write code to generate alignment in STAR
 - [x] 1.3 - Test
  - [x] 1.3.1 - Download TAIR10 Reference Genome and fastq files from Arabidopsis and test.
 - [x] 1.4 - Completion Criteria: Should create sorted BAM file
- [x] Task 2: Create the GATK Pipeline
 - [x] 2.1 - look at dogmap code for reference for using GATK functions
 - [x] 2.2 - model GATK code based on Dogmap Code
 - [] 2.3 - Test on TAIR 10
 - [] 2.4 - Completion Criteria: Should create GVCF file
- [] Task 3: Develop the API
  - [] 3.1 - Use OpenAPI 3.0 as a platform
  - [] 3.2 - Connect from local machine to USGS website
  - [] 3.3 - Completion Criteria - Should be able to pass data from local machine to Genome Browser.
- [] Task 4: Modify Genome Browser
  - [] 4.1- Highlight variant regions
   - [] 4.1.1- Consider different options for highlighting; probably try to make highlights an additional track on Genome Browser
- [] Task 5: Display Output Window
  - [] 5.1 - Find an appropriate tool for this purpose
- [] Task 6: Consider Options
  - [] 6.1 - Potentially add a different aligner like bwa or hisat2
  - [] 6.2 - enable different GATK settings
