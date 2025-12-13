A fun little computational linguistics project. This is a program that generates semantically dubious (potentially, at least!) but syntactically well-formed sentences in the style of Chomsky's Syntactic Structures. This could be developed into a Mad Lib style game which would be  
quite fun.  

Well-formedness is based upon constraints defined in a list of regular expressions (in illegal.py). So far, there's only two rules, but this can of course be expanded with the addition of new POS. It picks from a bank of words in a dictionary, sorted by part of speech. 
# POTENTIAL IMPROVEMENTS:
Addition of new parts of speech (adverbs, for example)  
New words for each category
Transitivity separations (V N is illegal under certain circumstances)
Either a command-line (argparse) based input method, or a tiny little GUI  
