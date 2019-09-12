# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print('-> {} > {}'.format(*attr))
        
html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()
