import os


class Path:
    def __init__(self):
        pass

    def root_directory(self):
        # main.py所在的目錄，即根目錄
        script_path = os.path.join(os.path.abspath(__file__))
        # print(script_path)
        package_directory = os.path.dirname(script_path)
        # print(package_directory)
        root_directory = os.path.dirname(package_directory)
        # print(root_directory)
        return root_directory


    def file_path(self, filename, directory='', subdirectory=''):
        root_dir = self.root_directory()

        # 存在文件名和一級目錄
        if directory != '' and subdirectory == '':
            # return 'yes dir no subdir'
            file_path = os.path.join(root_dir,directory,filename)

        # 存在文件名，一級目錄和二級目錄
        elif directory != '' and subdirectory != '':
            # return 'yes dir yes subdir'
            file_path = os.path.join(root_dir, directory, subdirectory, filename)
        elif directory == '' and subdirectory == '':
            # return 'no dir no subdir'
            file_path = os.path.join(root_dir, filename)
            # 其他情況
        else:
            file_path = 'some thing wrong! please check the code'

        return file_path

    def smart_file_path(self, filename):
        '''
        非常推介使用此功能代替file_path()，因為很智能
        :param filename: 用戶輸入的文件名
        :return: 通過文件名在項目更目錄查找該文件並返回絕對路徑
        '''
        root_dir = self.root_directory()
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if file == filename:
                    return os.path.abspath(os.path.join(root, file))

# p = Path()
# root_dir = p.root_directory()
# print(root_dir)

# p = Path()
# root_dir = p.file_path('emoji.png')
# print(root_dir)

# p = Path()
# root_dir = p.smart_file_path('deskt_wechat.py')
# print(root_dir)