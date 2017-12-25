import re

def build_match_and_apply(pattern, search, replace):
    def match_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (match_rule, apply_rule)

rules = []

def pluralize(noun):
    for match_rule, apply_rule in rules:
        if match_rule(noun):
            return apply_rule(noun)

if __name__ == '__main__':

    with open("plural4-rules.txt", encoding='utf-8') as file:
        for line in file:
            pattern, search, replace = line.split(None, 3)
            rules.append(build_match_and_apply(pattern, search, replace))

    print(pluralize("park"))
    print(pluralize("fly"))
    print(pluralize("apple"))