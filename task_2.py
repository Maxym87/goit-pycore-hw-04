

def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
    except FileNotFoundError:
        print('File not found')