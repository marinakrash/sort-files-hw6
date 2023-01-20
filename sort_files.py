import os
import shutil

import normalize

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
                directory = os.sep.join([path_directory, images])
                if not os.path.exists(directory): os.makedirs(directory)
                shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                img_files.append(nor_name)
            if type in ['.avi', '.mp4', '.mov', '.mkv']:
                directory = os.sep.join([path_directory, videos])
                if not os.path.exists(directory): os.makedirs(directory)
                shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                video_files.append(nor_name)
            if type in ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']:
                directory = os.sep.join([path_directory, documents])
                if not os.path.exists(directory): os.makedirs(directory)
                shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                doc_files.append(nor_name)
            if type in ['.mp3', '.ogg', '.wav', '.amr']:
                directory = os.sep.join([path_directory, audio])
                if not os.path.exists(directory): os.makedirs(directory)
                shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                music_files.append(nor_name)
            if type in ['.zip', '.gz', '.tar']:
                directory = os.sep.join([path_directory, archives])
                if not os.path.exists(directory): os.makedirs(directory)
                shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                ar_dir = f'{directory}'+f'{os.path.splitext(nor_name)[:-1]}'
                os.makedirs(ar_dir)
                shutil.unpack_archive(path_file, ar_dir)
                arch_files.append(nor_name)
            if type in ['.wenb', '.webm', '.sql', '', '.crdownload'] or type == [] or type is None:
                shutil.move(path_file, (f'{path_directory}' + f'/{nor_name}'))
                unknown_format.append(type)
    print(f'arch_files {arch_files}')
    print(f'doc_files {doc_files}')
    print(f'img_files {img_files}')
    print(f'music_files {music_files}')
    print(f'video_files {video_files}')
    print(f'all_types {all_types}')
    print(f'unknown_format {unknown_format}')
