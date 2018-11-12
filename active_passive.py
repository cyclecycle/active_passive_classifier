import os
import sys
from pprint import pprint


TO_BE_FORMS = {
    'is',
    'be',
    'were',
    'are'
}

PREP_FORMS = {
    'by'
}

# PREP_DEPS = {
#     'prep',
#     'agent',
# }


def find_passive_verbs(doc):
    for word in doc:
        # print(word, word.pos_, word.tag_)
        if not word.pos_ == 'VERB' or word.tag_ == 'VBD':
            continue
        # pre = doc[word.i-1]
        # if not pre.text in TO_BE_FORMS:
        #     continue
        post = doc[word.i+1]
        if not post.text in PREP_FORMS:
            continue
        yield word


if __name__ == '__main__':
    import spacy
    import en_core_web_sm
    nlp = en_core_web_sm.load()

    try:
        filename = sys.argv[0]
        text = sys.argv[1]
    except:
        pass