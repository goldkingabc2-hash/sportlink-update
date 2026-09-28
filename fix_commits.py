import os
import glob
import re

workflow_dir = '.github/workflows'
for file_path in glob.glob(os.path.join(workflow_dir, '*.yml')):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    
    # Remove git diff quiet checks that exit
    new_content = re.sub(r'[ \t]*if git diff.*?quiet.*?then.*?exit 0.*?fi\n', '', new_content, flags=re.DOTALL)
    
    # Remove step conditionals that skip on no changes
    new_content = re.sub(r'[ \t]*if:\s*steps\.check_changes\.outputs\.has_changes == \'true\'\n', '\n', new_content)
    
    # ensure commits always happen by allowing empty
    new_content = new_content.replace('git commit -m', 'date > .last_check\n          git add .last_check\n          git commit --allow-empty -m')

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
