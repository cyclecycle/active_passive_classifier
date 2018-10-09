import os
import sys
from pprint import pprint


TO_BE_FORMS = {
    'is',
    'be',
    'were',
    'are'
}

PREP_DEP = {
    'agent',
    'prep'
}


def find_passive_verbs(doc):
    for word in doc:
        # print(word, word.pos_, word.tag_)
        if not word.pos_ == 'VERB' or word.tag_ == 'VBD':
            continue
        for pre in doc[word.i-1:word.i]:
            # print(pre.text)
            if pre.text in TO_BE_FORMS:
                yield word
        # for post in doc[word.i+1:word.i+2]:
        #     # print(word)
        #     # print(post.dep_)
        #     if post.dep_ in PREP_DEP:
        #         yield word


if __name__ == '__main__':
    import spacy
    import en_core_web_sm
    nlp = en_core_web_sm.load()

    try:
        filename = sys.argv[0]
        text = sys.argv[1]
    except:
        pass