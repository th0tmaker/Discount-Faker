import os
import time


def search_files(root, pattern, search_prompt='name'):
    """Recursively search for files that match a pattern.

    Args:
        root (str): The directory to start searching from.
        pattern (str): The search pattern to match against file names or extensions.
        search_prompt (str): The search method to use ('name' or 'ext').

    Returns:
        A dictionary containing lists of file paths.

    Method:
        Walk through the directory tree at root using the os.walk() and return 3 values from current directory:
        1. Directory path (dirpath)
        2. list of directory names (dirnames)
        3. list of file names (filenames)
    """
    file_dict = {}
    for dirpath, dirnames, filenames in os.walk(root):
        # for each file in list of file names
        for filename in filenames:
            if search_prompt == 'name' and pattern in filename:
                filepath = os.path.join(dirpath, filename)  # get directory path and file name, save into filepath
                extension = os.path.splitext(filepath)[-1]  # get file extension
                # populate dictionary with key:extension, value: obtained or created list for matches file type
                files = file_dict.setdefault(extension, [])
                files.append(filepath)  # add the file path to the files list inside file_dict
            elif search_prompt == 'ext' and pattern == os.path.splitext(filename)[-1]:
                filepath = os.path.join(dirpath, filename)  # get directory path and file name, save into filepath
                # populate dictionary with key:extension, value: obtained or created list for matches file type
                files = file_dict.setdefault(pattern, [])
                files.append(filepath)  # add the file path to the files list inside file dict

    # return the file_dict dictionary with key=ext, value=list of files paths pair
    return file_dict


# program main loop
def main():
    while True:
        # prompt user for the search method
        search_method = input("Search files by file name pattern or file extension, type (name or ext): ").lower()
        # if search method is NOT either "name" or "ext", repeat prompt
        if search_method not in ("name", "ext"):
            print("Invalid search prompt. Type 'name' or 'ext' into input entry: ")
        else:
            # if search method IS "name"
            if search_method == "name":
                while True:
                    # prompt user for name pattern (full or partialy)
                    name_pattern = input("Search for file name or pattern: ").lower()
                    # if name pattern has 2 or fewer characters, repeat prompt
                    if len(name_pattern) <= 2:
                        print("Searching file name/pattern requires 3 or more input characters: ")
                    # if name has 3 or more characters...
                    else:
                        root_dir = '/' if os.name == 'posix' else 'C:\\'  # root directory to search (Unix or Windows)
                        # run search files function, match and save files with "name pattern" into temp_file_list
                        temp_file_list = search_files(root=root_dir, pattern=name_pattern, search_prompt=search_method)
                        break
                break
            # if search method IS "ext"
            else:
                while True:
                    # prompt user for extension pattern
                    ext_pattern = input("Search for file extension ('.' required, e.g.'.txt'): ").lower()
                    # if ext pattern has 1 or fewer characters, repeat prompt
                    if len(ext_pattern) <= 1:
                        print("Searching file extension requires 2 or more input characters: ")
                    # if ext pattern has 2 or more characters...
                    else:
                        root_dir = '/' if os.name == 'posix' else 'C:\\'  # root directory to search (Unix or Windows)
                        # run search files function, match and save files with "ext pattern" into temp_file_list
                        temp_file_list = search_files(root_dir, ext_pattern, search_prompt=search_method)

                        # sort by most recently accessed and save into temp_file_lists
                        temp_file_list = {k: sorted(v, key=lambda f: os.stat(f).st_atime_ns, reverse=True)
                                          for k, v in temp_file_list.items()}
                        break
                break

    # print results
    for ext, file_list in temp_file_list.items():
        print(f'\nFiles with {"name/pattern" if search_method == "name" else "extension"} "{ext}":')
        for file in sorted(file_list, key=os.path.getatime, reverse=True):
            last_accessed = time.strftime('%d-%m-%Y, %H:%M:%S', time.localtime(os.path.getatime(file)))
            print(f'\t{file}\t(last accessed on {last_accessed})')


# executed only when the script is run directly as a standalone program.
if __name__ == '__main__':
    main()
