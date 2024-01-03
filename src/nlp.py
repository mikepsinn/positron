import spacy

nlp = spacy.load('en_core_web_sm')

def get_request_type(request):
    doc = nlp(request)
    for token in doc:
        if token.dep_ == 'ROOT':
            if token.lemma_ in ['retrieve', 'get', 'fetch']:
                return 'data_retrieval'
            elif token.lemma_ in ['analyze', 'examine', 'study']:
                return 'repository_analysis'
            elif token.lemma_ in ['manage', 'handle', 'deal']:
                return 'issue_management'
            elif token.lemma_ in ['pull', 'merge', 'request']:
                return 'pull_request_management'
    return 'unknown'

def parse_request(request):
    doc = nlp(request)
    details = {'type': get_request_type(request)}
    for ent in doc.ents:
        if ent.label_ == 'ORG':
            details['repository'] = ent.text
    return details
