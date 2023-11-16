# Transcribe RNA to DNA by replacing all instances of "T" with "U"

my_file = open("rosalind_rna.txt", "r")
data = my_file.read() # a string with a DNA sequence
my_file.close()

# transcribe to RNA by replacing all instances of "T" with "U"
transcribed = data.replace("T", "U") # built-in string function

print(transcribed)

