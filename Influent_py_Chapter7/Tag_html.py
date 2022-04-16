def tag(name,*content,class_=None,**attrs):
    """Gnegrate one or more HTML tags"""
    if class_ is not None:
        attrs['class'] = class_
    attr_pairs = (f' {attr}="{value}"' for attr,value
                  in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    if content:
        elements = (f'<{name}{attr_str}>{C}</{name}>'
                    for C in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str} />'

print(tag('br')+'\n'+tag('p','hello',id=33))
#<br />
#<p id="33">hello</p>