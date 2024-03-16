

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError("to_html not implemented")
    

    def props_to_html(self):
        if self.props is None:
            return ""
        propshtml = ""
        for prop in self.props:
            propshtml += f' {prop}="{self.props[prop]}"'
        return propshtml
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    