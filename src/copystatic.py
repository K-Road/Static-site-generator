import os
import shutil
from block_markdown import markdown_to_html_node

def copy_files_recursive(source_dir,target_dir):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    for filename in os.listdir(source_dir):
        from_path = os.path.join(source_dir,filename)
        tar_path = os.path.join(target_dir,filename)
        print(f" * {from_path} > {tar_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path,tar_path)
        else:
            copy_files_recursive(from_path,tar_path)

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
        template_md = file.read()

    from_html = markdown_to_html_node(from_md).to_html()
    title = extract_title(from_md)

    new_html = template_md.replace("{{ Title }}",title)
    new_html = new_html.replace("{{ Content }}",from_html)


    with open(dest_path,"w") as file:
        file.write(new_html)
    
    
    