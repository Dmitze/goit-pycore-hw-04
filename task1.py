def total_salary(path):
    try:
        # відкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    # розділяємо рядок і беремо тільки зарплату
                    name, salary_str = line.strip().split(',')
                    salaries.append(float(salary_str))
                except ValueError:
                    print(f"Попередження: Некоректний формат даних у рядку, пропускаємо: {line.strip()}")
                    continue

        if not salaries:
            return 0, 0

        total_sum = sum(salaries)
        average_salary = total_sum / len(salaries)

        return total_sum, average_salary

    except FileNotFoundError:
        print(f"Помилка: файл за шляхом '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка при обробці файлу: {e}")
        return 0, 0

# для перевірки
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {int(average)}")