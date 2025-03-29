
def total_salary(path):
    try:
        with open(path, 'r',encoding='utf=8') as file:
            salaries = []
            for line in file:
                _, salary = line.strip().split()
                salaries.append(int(salary))
            total = sum(salaries)
            average = total / len(salaries) if salaries else 0

            return  total, average
    except FileNotFoundError:
        print('File not found')
    return 0
    
