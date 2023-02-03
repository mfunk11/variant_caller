def read_data(fastq_file):
    with open(fastq_file, 'r') as file:
        lines = f.readlines()
        print(f"{file} has {len(lines)/4} reads.")
    return len(lines)


def sum(num1, num2):
    return num1 + num2





