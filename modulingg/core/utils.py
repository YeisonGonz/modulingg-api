from modulingg.controllers.autoload import Autoloader
def only_modules(): 
    autoloader = Autoloader()
    all_content = autoloader.search_modules()
    modules = []
    for content in all_content:
        split_content = content[0].split('.')
        modules.append(split_content[0]) # I've spent 40 minutes looking for the bug to realize that this is the shit I'm missing.
        
    return modules

def only_manifest():
    autoloader = Autoloader()
    all_content = autoloader.search_modules()
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