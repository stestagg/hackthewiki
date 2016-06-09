from collections import deque
import subprocess


def bfs(start):
    jesus = b'http://en.wikipedia.org/wiki/Jesus'
    if start == jesus:
        return 0

    visited = set()
    visited.add(start)
    queue = deque([]) # make a queue from deque object
    queue.appendleft(start)
    path = [start]
    counter = 1
    last_in_gen = None
    while queue:
        parent = queue.pop()
        if parent == last_in_gen:
            counter += 1
        children = subprocess.check_output('./findlinks.py').splitlines()
        last_in_gen = children[-1]
        children = subprocess.check_output(
            ['./findlinks.py', parent]).splitlines()
        if jesus in children:
            return counter
        else:
            for child in children:
                if child not in visited:
                    visited.add(child)
                    queue.appendleft(child)

    return counter
