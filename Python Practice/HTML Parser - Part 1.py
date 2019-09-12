# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser as htp

class MyHTMLParser(htp):
    def handle_starttag(self, tag, attrs):        
        print('Start :',tag)
        for e in attrs:
            print('->', e[0],'>', e[1])
            
    def handle_endtag(self, tag):
        print('End   :', tag)
        
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for e in attrs:
            print ('->', e[0], '>', e[1])
            
parser = MyHTMLParser()
parser.feed(''.join([input() for _ in range(int(input()))]))
parser.close()
