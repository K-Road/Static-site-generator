#from textnode import TextNode, text_type_text
#from htmlnode import HTMLNode, LeafNode, ParentNode
#from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, text_to_textnodes
#from block_markdown import block_to_block_type
import os
import shutil
from copystatic import copy_files_recursive
from generate import generate_page, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory")
    copy_files_recursive(dir_path_static,dir_path_public)

    print("Generating pages")
    #generate_page("content/index.md","template.html","public/index.html")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

main()