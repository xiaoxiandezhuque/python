import os

result = []


def get_all(cwd):
    get_dir = os.listdir(cwd)
    for i in get_dir:
        sub_dir = os.path.join(cwd, i)
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            ax = os.path.basename(sub_dir)
            result.append(ax)
            print(len(result))


print(os.getcwd())
# get_all("E:")
