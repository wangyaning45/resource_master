import os
import time


def get_dir_list(cur_path):
    full_dir_list = os.listdir(cur_path)
    non_hidden_dir_list = list(filter(lambda dir: not dir.startswith('.'), full_dir_list))
    return full_dir_list, non_hidden_dir_list


def write_preview(fhandler, level, cur_list, cur_path, max_depth):
    if level == max_depth: return
    file_list = []
    for target in cur_list:
        if not os.path.isdir(cur_path+target+'/'):
            file_list.append(target)
            continue
        if level == 0:
            fhandler.write('## ' + target + '\n\n')
        else:
            fhandler.write('  ' * (level-1) + '* ' + target + '\n\n')
        write_preview(fhandler, level+1, get_dir_list(cur_path+target+'/')[1], cur_path+target+'/', max_depth)

    if level:
        if cur_list == []:
            fhandler.write('\n\n')
        for f in file_list:
            fhandler.write('  ' * (level-1) + '* ' + f + '\n\n')


# Create Readme
def creator(root, max_depth):
    with open(root+'README.md', 'w') as rm:
        rm.write('# README\n')
        rm.write('This is the preview of this repo:\n')
        write_preview(rm, 0, get_dir_list(root)[1], root, max_depth)
        rm.write('---\n\n')
        rm.write(time.strftime("%Y/%m Karl\n\n", time.localtime()))
        rm.write('@Powered by READMEAutoGenerator.\n\n')


if __name__ == '__main__':
    root = input('>> Enter the FULL REAL path of your directory:[./] ')
    max_depth = input('>> Enter the max depth of your directory:[2] ')
    root = './' if root == '' else root
    max_depth = 2 if max_depth == '' else int(max_depth)
    creator(root+'/', max_depth)
    print('Generated!')
    os.startfile(root+'/README.md')
