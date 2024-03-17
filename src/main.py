from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    tnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(tnode)


    l1 = LeafNode("p", "This is a paragraph of text.")
    l2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(l1)
    print(l1.to_html())
    print(l2.to_html())

    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )
    print(node.to_html())
    
main()