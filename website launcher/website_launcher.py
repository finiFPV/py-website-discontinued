def download_website_files():
    from github import Github
    from os import path, makedirs
    from shutil import rmtree

    repo = Github('***REMOVED***').get_user().get_repo('website')
    branch = 'development'
    contents = repo.get_contents('/Website', ref=branch)
    main_path = '~\\website'
    media_filetypes = ('.png', '.jpeg', '.ico', '.gif')

    def get(contents, sys_path):
        for content in contents:
            if content.type == 'dir':
                new_sys_path = f'{sys_path}\\{content.name}'
                makedirs(new_sys_path)
                new_contents = repo.get_contents(content.path, ref=branch)
                get(new_contents, new_sys_path)
            elif content.name.endswith(media_filetypes):
                for filetype in media_filetypes:
                    if content.name.endswith(filetype):
                        with open(f'{sys_path}\\{content.name}', 'wb') as content_file:
                            content_file.write(content.decoded_content)
            else:
                with open(f'{sys_path}\\{content.name}', 'w') as content_file:
                    content_file.write(content.decoded_content.decode('utf-8'))

    if path.exists(main_path):
        rmtree(main_path)
    makedirs(main_path)

    get(contents, main_path)

if __name__ == '__main__':
    from subprocess import call

    call(['python', '-m', 'pip', 'install', '--upgrade', 'pip'])
    call(['pip', 'install', 'PyGithub'])
    download_website_files()
    call(['pip', 'install', '-r', '~\\website\\requirments.txt'])
    call(['python', '~\\website_code\\Main.py'])