import sys

letter_file = sys.argv[1]
output_file = sys.argv[2]
with open(letter_file, "r", encoding="utf-8") as f, open(output_file, "w", encoding="utf-8") as output_f:
    for line in f:
        output_f.write(f'\n\t\t\t\t<span class="comments">{line.strip()}</span><br />')
