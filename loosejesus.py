import sys

import requests


def loose_starting_title(title, cont=None):
    url = 'https://en.wikipedia.org/w/api.php?action=query&list=backlinks&format=json&bltitle='+title+'&bllimit=max'
    if cont:
        url += "&blcontinue=%s" % cont
    r = requests.get(url)
    backlinks = r.json()
    for link in backlinks['query']['backlinks']:
        yield link['title']
    if "continue" in backlinks:
        for link in loose_starting_title(title, cont=backlinks['continue']['blcontinue']):
            yield link
 
seen_pages = set()

def store_backlink_value(title, rest_of_chain=()):
    rest_of_chain = rest_of_chain
    for link in loose_starting_title(title):
        if link not in seen_pages:
            yield link, (title, ) + rest_of_chain
            seen_pages.add(link)


if __name__ == '__main__':
    
    previous_relations = [("Jesus", ())]
    while True:
        next_relations = []
        for from_page, to_pages in previous_relations:
            for new_from, new_to_pages in store_backlink_value(from_page, to_pages):
                next_relations.append((from_page, to_pages))
                next_steps = " => ".join(new_to_pages)
                print("%s => %s" % (new_from, next_steps))
        previous_relations = next_relations
    




    #for link in loose_starting_title('Jesus'):
    #   print(link)
 



