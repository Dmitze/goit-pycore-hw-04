def get_cats_info(path):
    """
    Ця функція читає файл та повертає список словників з інформацією про котів.
    """
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip() # прибираємо зайві пробіли
                if not line: 
                    continue
                try:
                    cat_id, name, age = line.split(',')
                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_info.append(cat_dict)
                except ValueError:
                    print(f"Попередження: Неправильна структура рядка, пропускаємо: '{line}'")
    
    except FileNotFoundError:
        print(f"Помилка: не вдалося знайти файл за шляхом {path}")
    
    return cats_info
cats_info = get_cats_info("cats_file.txt")
print(cats_info)
