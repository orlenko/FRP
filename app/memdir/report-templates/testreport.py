import os
import sys
import time
from appy.pod.renderer import Renderer


dirname = os.path.abspath(os.path.dirname(__file__))

def main():
    template = os.path.join(dirname, 'testreport.odt')
    output = os.path.join(dirname, 'testreport-%s.pdf' % time.time())
    renderer = Renderer(template,
                        {'timestr': time.ctime()},
                        output)
    renderer.run()


if __name__ == '__main__':
    main()