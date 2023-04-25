from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("xlnet-base-cased")

from collections import defaultdict
from math import log


class UnigramLanguageModel:
  def __init__(self, sentences, smoothing=False):

    self.word_freqs = defaultdict(int)
    self.new_words = []
    self.sentences = sentences

  def train(self):
    words = [nltk.word_tokenize(sentence.lower()) for sentence in tqdm(self.sentences, desc="Tokenize")]
    for i in words:
      for j in i:
        self.new_words.append(j)
    for word in self.new_words:
        self.word_freqs[word] = self.word_freqs.get(word, 0) + 1

  def suggestion(self, previous_ngram):
    filtered_log_prob = {token: prob for token, prob in self.word_freqs.items() if previous_ngram in token}
    sorted_subwords = sorted(filtered_log_prob.items(), key=lambda x: x[1], reverse=True)
    result = []
    for token, prob in sorted_subwords[:5]:
      #print(f"Token: {token}, Log Probability: {prob}")
      result.append(token)
    return result