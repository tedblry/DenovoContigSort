import subprocess
import argparse
import os

def run_blastn(contigs_path, reference_path, output_path, contigname):
    print("Running BLASTN...")
    # Run BLASTN
    blastn_cmd = f"blastn -query {contigs_path} -subject {reference_path} -outfmt '6' -evalue 1e-10 -max_hsps 1"
    blastn_process = subprocess.Popen(blastn_cmd, shell=True, stdout=subprocess.PIPE)
    
    print("Sorting the BLASTN output...")
    # Sort the output
    sort_cmd = "sort -nk 9"
    sort_process = subprocess.Popen(sort_cmd, shell=True, stdin=blastn_process.stdout, stdout=subprocess.PIPE)
    
    print("Extracting contig IDs...")
    # Cut the output
    cut_cmd = "cut -f 1"
    cut_process = subprocess.Popen(cut_cmd, shell=True, stdin=sort_process.stdout, stdout=subprocess.PIPE)
    
    print("Writing contig IDs to a file...")
    # Write the output to a file
    with open("ordered_contig_list.txt", "w") as f:
        f.write(cut_process.communicate()[0].decode())
    
    print("Running seqtk...")
    # Run seqtk
    seqtk_cmd = f"seqtk subseq {contigs_path} ordered_contig_list.txt > temp.fasta"
    subprocess.run(seqtk_cmd, shell=True)

    print("Reordering contigs...")
    # Reorder contigs
    with open("ordered_contig_list.txt", "r") as list_file, open("temp.fasta", "r") as fasta_file, open(output_path, "w") as output_file, open("ordered_renamed_" + output_path, "w") as renamed_output_file:
        contig_order = [line.strip() for line in list_file]
        contigs = fasta_file.read().split(">")[1:]
        contigs_dict = {contig.split("\n", 1)[0]: contig for contig in contigs}
        for i, contig_name in enumerate(contig_order, start=1):
            output_file.write(">" + contigs_dict[contig_name])
            renamed_output_file.write(f">{contigname}_{i}\n" + "\n".join(contigs_dict[contig_name].split("\n")[1:]))

    print("Done!")
    os.remove("temp.fasta")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Order contigs using BLASTN and seqtk.")
    parser.add_argument("contigs_path", help="Path to the contigs file.")
    parser.add_argument("reference_path", help="Path to the reference genome file.")
    parser.add_argument("output_path", help="Path to the output file.")
    parser.add_argument("--contigname", default="contig", help="Prefix for renamed contigs.")
    
    args = parser.parse_args()
    
    run_blastn(args.contigs_path, args.reference_path, args.output_path, args.contigname)


"""
Code Used
python3 DenovoContigSort.py /Users/byeongyeoncho/kosticlab_ev/Manuscript_assembly/p1_assembly_output/medaka_output/medaka_racon_5/consensus.fasta /Users/byeongyeoncho/kosticlab_ev/MappCountFlow/input/ref_reannotated.fna ordered_EV_contigs.fasta --contigname EV_contig

echo 'export PATH="$PATH:/Users/byeongyeoncho/kosticlab_ev/DenovoContigSort/ncbi-blast-2.14.1+/bin"' >> ~/.bash_profile
"""