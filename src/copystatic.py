import os
import shutil

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
