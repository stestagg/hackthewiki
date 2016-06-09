import sys

import bfs
import signal_handeling



def main():
    signal_handeling.prepareToFindJesus()
    print(bfs.bfs("http://en.wikipedia.org/wiki/Special:Random"))
    signal_handeling.jesusFound()


if __name__ == '__main__':
    sys.exit(main())
