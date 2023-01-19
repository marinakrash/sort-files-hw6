import os
import shutil
import sys

import normalize

path_directory=sys.argv[-1]

def collect_fileinfos(path_directory):
    all_types = []
    arch_files = []
    doc_files = []
    filesurvey = []
    img_files = []
    music_files = []
    video_files = []
    unknown_format = []
    type=''
    content_dir = os.listdir(path_directory)
    if '.DS_Store' in content_dir: content_dir.remove('.DS_Store')
    for filename in content_dir:
        path_file = os.sep.join([path_directory, filename])
        nor_name = normalize.normalize(filename)
        if os.path.isdir(path_file):
            collect_fileinfos(path_file)
            if not os.listdir(path_file):
                os.rmdir(path_file)
        else:
            filesurvey.append((path_directory, filename))
            type = os.path.splitext(filename)[-1]
            all_types.append(type)
            if type in ['.jpeg', '.png', '.jpg', '.svg']:
                directory = '/Users/marina/Desktop/hh/images'
                if not os.path.exists(directory): os.makedirs(directory)
                shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                img_files.append(nor_name)
            if type in ['.avi', '.mp4', '.mov', '.mkv']:
                directory = '/Users/marina/Desktop/hh/videos'
                if not os.path.exists(directory): os.makedirs(directory)
                shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                video_files.append(nor_name)
            if type in ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']:
                directory = '/Users/marina/Desktop/hh/documents'
                if not os.path.exists(directory): os.makedirs(directory)
                shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                doc_files.append(nor_name)
            if type in ['.mp3', '.ogg', '.wav', '.amr']:
                directory = '/Users/marina/Desktop/hh/audio'
                if not os.path.exists(directory): os.makedirs(directory)
                shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                music_files.append(nor_name)
            if type in ['.zip', '.gz', '.tar']:
                directory = '/Users/marina/Desktop/hh/archives'
                if not os.path.exists(directory): os.makedirs(directory)
                shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                ar_dir = f'{directory}'+f'{os.path.splitext(nor_name)[:-1]}'
                os.makedirs(ar_dir)
                shutil.unpack_archive(path_file, ar_dir)
                arch_files.append(nor_name)
            if type in ['.wenb', '.webm', '.sql', '', '.crdownload'] or type == [] or type is None:
                directory = '/Users/marina/Desktop/hh'
                shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                unknown_format.append(type)
    print(f'arch_files {arch_files}')
    print(f'doc_files {doc_files}')
    print(f'img_files {img_files}')
    print(f'music_files {music_files}')
    print(f'video_files {video_files}')
    print(f'all_types {all_types}')
    print(f'unknown_format {unknown_format}')




