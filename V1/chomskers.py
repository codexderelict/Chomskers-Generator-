import random 
import re
from lexicon import lexicon
from illegal import patterns 
class Chomskers:
    lex = lexicon
    patterns = patterns
    def __init__(self):
        self.struct = Chomskers.get_struct()
    @classmethod
    def get_struct(self):
        while True:
            try:
                struct = list(str(input("Enter structure: ")).strip().split(" "))
                for element in struct:
                    if element not in self.lex.keys():
                        raise ValueError
                return struct 
            except ValueError:
                print("Pls input a structure like ADJ N V, it doesn't care which order")
    def verify(self):
        for pattern in self.patterns:
            if re.search(pattern, " ".join(self.struct)):
                return False 
        return True

    def pick(self):
        sentence = []
        for element in self.struct:
            sentence.append(random.choice(self.lex[element]))
        return " ".join(sentence)
    def run(self):
        if self.verify():
            sentence = self.pick()
            print(sentence)

chomskers = Chomskers()
chomskers.run()