# DenovoContigSort

DenovoContigSort is a Python script designed to help researchers in the field of genomics order contigs based on a reference genome. It uses BLASTN and seqtk, two powerful bioinformatics tools, to perform this task efficiently and accurately. The script also includes an option to rename the ordered contigs.

## Table of Contents

- **[Prerequisites](https://github.com/tedblry/DenovoContigSort#troubleshooting)**
- **[Installation](https://github.com/tedblry/DenovoContigSort#installation)**
- **[Usage](https://github.com/tedblry/DenovoContigSort#usage)**
- **[How It Works](https://github.com/tedblry/DenovoContigSort#how-it-workss)**
- **[Troubleshooting](https://github.com/tedblry/DenovoContigSort#troubleshooting)**
- **[Contributing](https://github.com/tedblry/DenovoContigSort#contributing)**
- **[Contact](https://github.com/tedblry/DenovoContigSort#contact)**

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the following:
    - **[Python 3.9.1 or later](https://www.python.org/downloads/)**
    - **[BLAST+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download)**
    - **[seqtk](https://github.com/lh3/seqtk)**
    - **[GNU Core Utilities](https://www.gnu.org/software/coreutils/coreutils.html)**
    - **[Homebrew](https://brew.sh/)**

For M1 Mac users, you might need to use Rosetta 2 to run BLAST+. Follow these steps:

1. Open Terminal and type the following commands:
    
    ```
    # Install Homebrew
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    # Install seqtk
    brew install seqtk
    
    # Install GNU Core Utilities
    brew install coreutils
    
    # Install BLAST+
    # As of now, you might need to use Rosetta 2 to run BLAST+ on M1 Macs
    arch -x86_64 /bin/bash
    # Then, in the new shell, download and install BLAST+
    curl -O https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.14.1+-x64-macosx.tar.gz
    tar -zxvf ncbi-blast-2.14.1+-x64-macosx.tar.gz
    # Add BLAST+ to your PATH
    echo 'export PATH="$PATH:/path/to/ncbi-blast-2.14.1+/bin"' >> ~/.bash_profile
    # Exit the Rosetta 2 shell
    exit
    
    ```
    
    Please replace `/path/to/ncbi-blast-2.14.1+/bin` with the actual path to the `bin` directory inside the extracted `ncbi-blast-2.14.1+` directory.
    

## Installation

To install DenovoContigSort, follow these steps:

1. Clone the repository:
    
    ```
    git clone https://github.com/yourusername/DenovoContigSort.git
    
    ```
    
2. Navigate to the cloned repository:
    
    ```
    cd DenovoContigSort
    
    ```
    

## Usage

To use DenovoContigSort, follow these steps:

1. Run the script with the path to your contigs file, the path to the reference genome file, and the path to the output file. You can also specify a prefix for the renamed contigs using the `-contigname` option. If you don't provide this option, the script will use "contig" as the default prefix.
    
    ```
    python3 DenovoContigSort.py your_contigs.fasta reference.fasta ordered_contigs.fasta --contigname EV_contig
    
    ```
    
    Replace `your_contigs.fasta`, `reference.fasta`, and `ordered_contigs.fasta` with the paths to your actual files.
    

## How It Works

The script works by performing the following steps:

1. Running BLASTN to compare the contigs to the reference genome.
2. Sorting the BLASTN output by the start position of the alignment on the reference genome.
3. Extracting the contig IDs from the sorted BLASTN output.
4. Writing the extracted contig IDs to a file.
5. Running seqtk to extract the contigs in the order specified in the file and writing them to the output file.
6. Renaming the contigs based on the user-specified prefix (or the default prefix "contig" if not specified) and writing them to a new output file.

## Troubleshooting

If you encounter any issues while using DenovoContigSort, please check the following:

- Ensure that all the prerequisites are correctly installed and available in your system's PATH.
- Check that the paths to your contigs file, reference genome file, and output file are correct.

## Contributing

Contributions to DenovoContigSort are always welcome. If you have a feature request or find a bug, please open an issue on the GitHub repository.

## Contact

If you want to contact me, you can reach me at `byeongyeon_cho@hms.harvard.edu`.