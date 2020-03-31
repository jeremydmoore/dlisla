from pathlib import Path

# functions
def delete_dot_files(directory):
    dir_path = Path(directory)
    dot_file_path_list = list(dir_path.glob('**/.*'))
    print(f'Number of dot files before delete: {len(dot_file_path_list)}')
    for dot_file_path in dot_file_path_list:
        dot_file_path.unlink()
    dot_file_path_list = list(dir_path.glob('**/.*'))
    print(f'After delete: {len(dot_file_path_list)}')

def jhove_jp2(directory):
    dir_path = Path(directory)
    print(f'Processing JP2s in {dir_path}')
    # get list of jp2 files & delete all .*.jp2 dot files
    jp2_path_list = sorted(dir_path.glob('**/*.jp2'))
    delete_dot_files(dir_path)
    jp2_path_list = sorted(dir_path.glob('**/*.jp2'))

    # instantiate error dictionary
    error_dict = {}
    for jp2_path in jp2_path_list:
        print(jp2_path.name)
        status = !{jhove} "{str(jp2_path)}" | grep -e 'Status:'
        status = status[0]
        if status == '  Status: Well-Formed and valid':
            continue
        else:
            error_dict.update( {jp2_path.name : status} )

    return error_dict

# variables
root_path = Path('/Users/dlisla/Pictures/athletics-programs/Output')
jhove = f'~/jhove/jhove -m JPEG2000-hul'
