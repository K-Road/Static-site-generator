import os
from pathlib import Path
from block_markdown import markdown_to_html_node

def extract_title(markdown):
    if not markdown.startswith("# "):
        raise ValueError("Invalid markwup: No H1")
    lines = markdown.split("\n")
    return lines[0][2:]

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        from_md = file.read()
    
    with open(template_path,"r") as file:
        template = file.read()

    from_html = markdown_to_html_node(from_md).to_html()
    title = extract_title(from_md)

    template = template.replace("{{ Title }}",title)
    template = template.replace("{{ Content }}",from_html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path,exist_ok=True)

    with open(dest_path,"w") as file:
        file.write(template)
    
def generate_pages_recursive(dir_path_content, template_path, dir_path_public):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content,filename)
        to_path = os.path.join(dir_path_public,filename)
        if os.path.isfile(from_path):
            to_path = Path(to_path).with_suffix(".html")
            generate_page(from_path,template_path,to_path)
        else:
            generate_pages_recursive(from_path,template_path,to_path)