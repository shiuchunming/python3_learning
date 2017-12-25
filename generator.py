import re

def build_match_and_apply(pattern, search, replace):
    def match_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (match_rule, apply_rule)

def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as file:
        for line in file:
            pattern, search, replace = line.split(None, 3)
            yield build_match_and_apply(pattern, search, replace)

def pluralize(noun, rules_filename='plural4-rules.txt'):
    for match_rule, apply_rule in rules(rules_filename):
        if match_rule(noun):
            return apply_rule(noun)

if __name__ == '__main__':
    print(pluralize("park"))
    print(pluralize("fly"))
    print(pluralize("apple"))