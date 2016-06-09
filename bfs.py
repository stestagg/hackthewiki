import sys
import requests
from bs4 import BeautifulSoup
from collections import deque
import subprocess

def bfs(start):
    jesus = 'http://en.wikipedia.org/wiki/Jesus'
    if start == jesus:
        return 0
    
    visited = set()
    visited.add(start)
    queue = deque([]) # make a queue from deque object
    queue.appendleft(start)
    path = [start]
    counter = 1
    while queue:
        parent = queue.pop()
        children = subprocess.check_output('./findlinks.py').splitlines()
        if jesus in children:
            path.append(parent)
            return counter
        else:
            counter += 1 
            for child in children:
                if child not in visited:
                    visited.add(child)
                    queue.appendleft(child)

    return counter