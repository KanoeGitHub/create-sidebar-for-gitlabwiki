import os

# Add directories, extensions, and file names that you do not want displayed in the sidebar.
IGNORE_LIST = [".git", "create_sidebar.py","README.md", \
               "_sidebar.md", "images", "githooks"]

# Initialize indentation (2 spaces ← 4 spaces will cause display errors)
SPACES = "  "
# Gets the current directory.
CURRENT_DIRECTORY = os.getcwd()
# Path of view_all_pages
ALL_PAGES = "<gitlab-repository-url>/-/wikis/pages"

def paths_sorted(paths):
    paths = sorted(paths, key=lambda x: (int(x.split(".")[0]) if x.split(".")[0].isdigit() else float('-1'), x))    
    return paths
  
def get_all_files_and_directories(path, depth):
    SPACES_tmp = SPACES*depth    
    file_list = os.listdir(path) 
    file_list = paths_sorted(file_list)
    for f in file_list:
        if f in IGNORE_LIST:
            continue
        if os.path.isdir(path+"/"+f):
            writepath=(path+"/"+f)
            writepath=writepath.replace(CURRENT_DIRECTORY, '.')
            ## If the depth is 0, add "<details><summary>" before the folder name for folding in html.
            if depth==0:
                print(f'{SPACES_tmp}<details><summary> {f} </summary>')
                sidebar.write(f'{SPACES_tmp}<details><summary> {f} </summary>'+ "\n\n")
            else:
                print(f'{SPACES_tmp}* [{f}]({writepath})')
                #sidebar.write(f'{SPACES_tmp}* [{f}]({writepath})'+ "\n")
                sidebar.write(f'{SPACES_tmp}* 【{f}】'+ "\n")
            get_all_files_and_directories(path+"/"+f, depth+1)
            ## If the depth is 0, add "</details>" after the folder name for folding in html.
            if depth==0:
                print(f'{SPACES_tmp}</details>')
                sidebar.write(f'{SPACES_tmp}</details>'+ "\n\n")
        elif f.split(".")[-1] == "md":
            writepath=(path+"/"+f.split(".")[0])
            writepath=writepath.replace(CURRENT_DIRECTORY, '.')
            print(f'{SPACES_tmp}* [{f.split(".")[0]}]({writepath})')
            sidebar.write(f'{SPACES_tmp}* [{f.split(".")[0]}]({writepath})'+ "\n")

if __name__ == '__main__':
    sidebar = open("_sidebar.md", 'w', encoding="utf-8")
    get_all_files_and_directories(CURRENT_DIRECTORY, 0)
    ## Add ALL_PAGES.
    sidebar.write("\n" + f'##### 【[View All Pages]({ALL_PAGES})】'+ "\n")
    sidebar.close()
