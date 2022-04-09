import os
def CountWordsTxt(path):
    with(open(path), 'r') as f:
        content = f.read
        word_count = len(content.spli())
        return word_count


CountWordsTxt('poem.txt')