

def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                parts = line.split(',')

                if len(parts) == 3:
                    cat_id, name, age = parts
                    cat_info = {'id' : cat_id, 'name' : name, 'age' : age}
    except FileNotFoundError:
        print('File not found')