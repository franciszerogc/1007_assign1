from pysentimiento import create_analyzer
import csv
from collections import Counter


class Foo:
    def __init__(self):
        self.analyzer = create_analyzer(task="sentiment", lang="en")
        with open('text.csv', 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            self.articles = [row["Text"] for row in reader]
        self.sentiments = []

    def sentimental_analyse(self):
        for i, article in enumerate(self.articles):
            result = self.analyzer.predict(article)
            sentiment = result.output
            print("[%4d/%4d] %-10s %s" % (i, len(self.articles), sentiment, article))
            self.sentiments.append(sentiment)

        sentiment_counts = Counter(self.sentiments)
        total = len(self.sentiments)
        for sentiment, count in sentiment_counts.items():
            percentage = (count / total) * 100
            print(f"{sentiment}: {percentage:.2f}%")

    def save_csv(self):
        with open('sentiments.csv', 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Sentiment", "Text"])
            for sentiment, article in zip(self.sentiments, self.articles):
                writer.writerow([sentiment, article])


if __name__ == '__main__':
    foo = Foo()
    foo.sentimental_analyse()
    foo.save_csv()
