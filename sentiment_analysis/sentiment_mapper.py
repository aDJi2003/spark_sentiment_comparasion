import sys
import re

with open("positive-words.txt", "r") as f:
    positive_words = set(word.strip() for word in f.readlines())

with open("negative-words.txt", "r") as f:
    negative_words = set(word.strip() for word in f.readlines())

for line in sys.stdin:
    line = line.strip()
    fields = line.split(",")
    if len(fields) > 2:
        tweet = fields[2].lower()
        words = re.findall(r'\w+', tweet)

        pos_count = sum(1 for word in words if word in positive_words)
        neg_count = sum(1 for word in words if word in negative_words)
        sentiment = "positive" if pos_count > neg_count else "negative" if neg_count > pos_count else "neutral"

        print(f"{sentiment}\t1")