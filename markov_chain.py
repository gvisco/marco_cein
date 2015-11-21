# This Python file uses the following encoding: utf-8
import random


class MarkovChain:
    EOC = "**EOC**"  # End of chain

    def __init__(self, k=3):
        """Create new empty Markov chain of order equals to k"""
        self.K = k
        self.graph = {}  # {vertex : [next vertices] }

    def get_random_sentence(self):
        s0 = random.choice(self.graph.keys())
        return self.generate_sentence(s0)

    def search_states_by_keyword(self, keyword):
        states = []
        for s in self.graph.keys():
            if keyword in s:
                states.append(s)
        return states

    def generate_sentence(self, s0):
        vertex = s0
        next_vertex = ""
        sentence = []
        while next_vertex is not self.EOC:
            next_vertex = random.choice(self.graph[vertex])
            if next_vertex is self.EOC:
                sentence.append(vertex)
            else:
                sentence.append(vertex.split()[0])
                vertex = next_vertex
        return " ".join(sentence)

    def learn(self, sentence):
        index = self.K
        tokens = sentence.strip().split()
        l = len(tokens)
        while index < l:
            s1 = tokens[(index - self.K):index]
            s2 = tokens[(index - self.K + 1):index + 1]
            self.__add_transition(" ".join(s1), " ".join(s2))
            index += 1
        # end of sentence
        if l >= self.K:
            s1 = tokens[l - self.K:l]
            self.__add_transition(" ".join(s1), self.EOC)

    def __add_transition(self, s1, s2):
        if s1 not in self.graph:  # create new state
            self.graph[s1] = [s2]
        else:  # modify existing state
            self.graph[s1].insert(0, s2)

    def __str__(self):
        return str(self.graph)
