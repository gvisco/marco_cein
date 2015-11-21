# marco_cein
Naive Markov Chain written in Python.

Sample usage:
```python

# instantiate a new order 2 chain
mc = MarkovChain(2)

# train it
for sentence in input:
    mc.learn(sentence)

# print the model (may be huge)
print mc

# generate a sentence that starts with 'foo'
st = random.choice(mc.search_states_by_keyword("foo"))
print mc.generate_sentence(st)

# generate a random sentence
print mc.get_random_sentence()

```
