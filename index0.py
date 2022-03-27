import re
import sys

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no,line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # # ugly?
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences
            index.setdefault(word,[]).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
