import os

dir = "D:\\Users\\Administrator\\Desktop\\py测试目录"

subdir = os.listdir(dir)

for i in subdir:
    path = os.path.join(dir, i)
    if os.path.isdir(path):
        end_dir = os.listdir(path)
        for i in range(len(end_dir)):
            newname = "haha"
            os.rename(os.path.join(path, end_dir[i]), os.path.join(path, newname))
