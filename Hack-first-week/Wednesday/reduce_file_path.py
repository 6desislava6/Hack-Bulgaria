def reduce_file_path(path):

    path = path.replace('//', '/')
    while (path.find('/..') != -1):
        index = path.find('/..')
        path = path[:index] + path[index + 3:]
        starting_index = index
        while (path[starting_index - 1] != '/'):
            starting_index -= 1
        starting_index -= 1
        path = path[:starting_index]+path[index:]
    while path[-1] == '/' and len(path) != 1:
        path = path[:-1]
    path = path.replace('./', '')
    print(path)

reduce_file_path("/srv/Pythonu/../uu")
reduce_file_path("/")
reduce_file_path("/srv/../")
reduce_file_path("/srv/www/htdocs/wtf/")
reduce_file_path("/etc//wtf/")
reduce_file_path("//////////////")
reduce_file_path("/../")