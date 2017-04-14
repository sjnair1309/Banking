line=raw_input('Enter a line where each word is seperated by commas:')
fh=line.lower()
words=fh.strip().split(',')
print words
counts=dict()
for word in words:
 if word not in counts:
  counts[word]=1
 else:
  counts[word]=counts[word]+1
print counts
print len(counts)
bigcount= None
bigword= None
for word,count in counts.items():
 if bigcount is None or count > bigcount:
  bigcount=count
  bigword=word
print bigword,bigcount