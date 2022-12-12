import pandas as pd

def get_experience(arg):

    exclude_list = ['лет', 'года', 'год']
    experience_list = arg.split(' ')
    
    if len(experience_list)>4:
        return int(experience_list[2]) * 12 + int(experience_list[4])
    
    if experience_list[3] in exclude_list:
        return int(experience_list[2]) * 12
    
    return int(experience_list[2]) 


if __name__ == '__main__':
    experience_col = pd.Series([
        'Опыт работы 8 лет 3 месяца',
        'Опыт работы 3 года 5 месяцев',
        'Опыт работы 1 год 9 месяцев',
        'Опыт работы 3 месяца',
        'Опыт работы 6 лет'
        ])
    experience_month = experience_col.apply(get_experience)
    print(experience_month)

    