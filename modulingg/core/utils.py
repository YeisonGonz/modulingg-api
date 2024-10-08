
from modulingg.controllers.autoload import search_modules


def only_modules():
    all_content = search_modules()
    modules = []
    for content in all_content:
        split_content = content[0].split('.')
        modules.append(split_content[1])
        
    return modules



def only_manifest():
    all_content = search_modules()
    manifest = []
    for content in all_content:
        manifest.append(content[1])
        
    return manifest


def print_manifest(manifest):
    print(f"\nModule 📦")
    print(f"    Name: {manifest.name}")
    print(f"    Short Name: {manifest.short_name}")
    print(f"    Description: {manifest.description}")
    print(f"    Author: {manifest.author}")
    print(f"    Version: {manifest.version}")