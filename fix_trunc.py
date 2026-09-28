import os
import glob
import re

workflow_dir = '.github/workflows'
for file_path in glob.glob(os.path.join(workflow_dir, '*.yml')):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if content.endswith('echo \"Push'):
        print(f\"Fixing truncated {file_path}\")
        content += ' failed\"\n          exit 1'
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    elif content.endswith('echo \"'):
        print(f\"Fixing truncated {file_path}\")
        content += '\"\n          exit 1'
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
