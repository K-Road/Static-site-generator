import re
from textnode import (
    TextNode
)

def markdown_to_blocks(markdown):
    new_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:  
        if block == "":
            continue
        block = block.strip()
        new_blocks.append(block)
        
    return new_blocks