#returning function as an arguement
def html_tag(tag):

    def text_wrap(msg):
        print(f"<{tag}>{msg}</{tag}")
    return text_wrap

print_h1=html_tag('h1')
print(print_h1)
#print_h1('test headline!')