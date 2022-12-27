def download_website_files(branch):
    from github import Github
    from os import path, makedirs
    from shutil import rmtree
    from os import getcwd

    repo = Github('***REMOVED***').get_user().get_repo('website')
    contents = repo.get_contents('/Website', ref=branch)
    main_path = f'{getcwd()}/website'
    media_filetypes = ('.png', '.jpeg', '.ico', '.gif')

    def get(contents, sys_path):
        for content in contents:
            if content.type == 'dir':
                new_sys_path = f'{sys_path}/{content.name}'
                makedirs(new_sys_path)
                new_contents = repo.get_contents(content.path, ref=branch)
                get(new_contents, new_sys_path)
            elif content.name.endswith(media_filetypes):
                for filetype in media_filetypes:
                    if content.name.endswith(filetype):
                        with open(f'{sys_path}/{content.name}', 'wb') as content_file:
                            content_file.write(content.decoded_content)
            else:
                with open(f'{sys_path}/{content.name}', 'w') as content_file:
                    content_file.write(content.decoded_content.decode('utf-8'))

    if path.exists(main_path):
        rmtree(main_path)
    makedirs(main_path)

    get(contents, main_path)

if __name__ == '__main__':
    from subprocess import call
    from os import getcwd
    from shutil import copy2
    from os import rename, remove

    branch = 'master' # default 'master'
    ssl = False       # default False

    call(['python3', '-m', 'pip', 'install', '--upgrade', 'pip'])
    call(['pip', 'install', 'PyGithub'])
    download_website_files(branch)
    call(['pip', 'install', '-r', f'{getcwd()}/website/configs/requirments.txt'])
    if ssl:
        confg_file = 'nginx.conf'
    else:
        confg_file = 'nginx_http.conf'
    copy2(f'{getcwd()}/website/configs/{confg_file}', f'{getcwd()}')
    if not ssl:
        rename(f'{getcwd()}/nginx_http.conf', f'{getcwd()}/nginx.conf')
    copy2(f'{getcwd()}/nginx.conf', f'{getcwd()}/other')#/etc/nginx/nginx.conf')
    remove(f'{getcwd()}/nginx.conf')
    call(['systemctl', 'reload', 'nginx'])
    call(['python3', f'{getcwd()}/website/Main.py'])