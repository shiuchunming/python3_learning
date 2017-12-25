import re

patterns = (
    ('[sxz]$',           '$',  'es'),
    ('[^aeioudgkprt]h$', '$',  'es'),
    ('(qu|[^aeiou])y$',  'y$', 'ies'),
    ('$',                '$',  's')
)

def build_match_and_apply(pattern, search, replace):
    def match_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (match_rule, apply_rule)

rules = [build_match_and_apply(pattern, search, replace)
         for (pattern, search, replace) in patterns]

def pluralize(noun):
    for match_rule, apply_rule in rules:
        if match_rule(noun):
            return apply_rule(noun)

if __name__ == '__main__':
    print(pluralize("park"))
    print(pluralize("fly"))
    print(pluralize("apple"))