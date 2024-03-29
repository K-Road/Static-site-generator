from textnode import TextNode, text_type_text
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, text_to_textnodes
from block_markdown import block_to_block_type

def main():
    # tnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(tnode)


    # l1 = LeafNode("p", "This is a paragraph of text.")
    # l2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    # print(l1)
    # print(l1.to_html())
    # print(l2.to_html())

    # node = ParentNode(
    # "p",
    # [
    #     LeafNode("b", "Bold text"),
    #     LeafNode(None, "Normal text"),
    #     LeafNode("i", "italic text"),
    #     LeafNode(None, "Normal text"),
    # ],
    # )
    # print(node.to_html())

    # text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
    # print(extract_markdown_images(text))

    # text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    # print(extract_markdown_links(text))
    # node = TextNode(
    #     "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    #     text_type_text,
    # )
    # print(split_nodes_image([node]))
    # text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
    # print(text_to_textnodes(text))
    
    md = """1. This is **bolded** paragraph
2.
3. This is another paragraph with *italic* text and `code` here
4. This is the same paragraph on a new line
5. 
6. This is a list
7. with items"""
    print(block_to_block_type(md))

main()