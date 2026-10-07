"""Small HTML tree reader shared by the AI builder and validator (stdlib only)."""
import re
from html.parser import HTMLParser
VOID = set("area base br col embed hr img input link meta param source track wbr".split())

class Node:
    def __init__(self, tag='', attrs=(), parent=None, data=''):
        self.tag, self.attrs, self.parent, self.data = tag, dict(attrs), parent, data
        self.children = []
    def all(self, tag=None):
        for child in self.children:
            if tag is None or child.tag == tag:
                yield child
            yield from child.all(tag)
    def text(self):
        return re.sub(r'\s+', ' ', self.data + ''.join(c.text_raw() for c in self.children)).strip()
    def text_raw(self):
        return self.data + ''.join(c.text_raw() for c in self.children)
    def has(self, cls):
        return cls in self.attrs.get('class', '').split()

class Parser(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.root = Node(); self.current = self.root
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.current)
        self.current.children.append(node)
        if tag not in VOID:
            self.current = node
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)
    def handle_endtag(self, tag):
        node = self.current
        while node.parent:
            if node.tag == tag:
                self.current = node.parent; return
            node = node.parent
    def handle_data(self, data):
        self.current.children.append(Node(parent=self.current, data=data))

def absolute(value, canonical):
    from urllib.parse import urljoin
    return urljoin(canonical, value)

def markdown(node, canonical):
    if node.tag in ('script', 'style', 'nav', 'form', 'button', 'svg', 'iframe') or node.attrs.get('aria-hidden') == 'true':
        return ''
    if not node.tag:
        return re.sub(r'\s+', ' ', node.data)
    body = ''.join(markdown(c, canonical) for c in node.children).strip()
    if node.tag in ('h1','h2','h3','h4'):
        return '\n\n' + '#' * int(node.tag[1]) + ' ' + body + '\n\n'
    if node.tag == 'a' and node.attrs.get('href'):
        return '[' + body + '](' + absolute(node.attrs['href'], canonical) + ') '
    if node.tag == 'img':
        return '\n\n!['+node.attrs.get('alt','')+']('+absolute(node.attrs['src'],canonical)+')\n\n'
    if node.tag in ('p','div','section','article','main','figure','figcaption','address'):
        return '\n\n'+body+'\n\n' if body else ''
    return body + ' ' if body else ''

def clean(text):
    return re.sub(r'\n{3,}', '\n\n', re.sub(r'[ \t]+\n', '\n', text)).strip()+'\n'
