"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
def get_total_sales_for_each_product(sales_stats):
    for item in sales_stats:
        total = 0
        for sold in item['items_sold']:
            total = total + sold          
        print(f"Cуммарное количество продаж  {item['product']}: {total}")
    print('\n')
def get_average_sales_for_each_product(sales_stats):
    for item in sales_stats:
        total = 0
        items = 0
        for sold in item['items_sold']:
            total = total + sold
            items +=1
        average_sales = total / items
        print(f"Cреднее количество продаж {item['product']}: {average_sales}")
    print('\n')
def get_total_sales_for_all_products(sales_stats):
    total = 0
    for item in sales_stats:
        for sold in item['items_sold']:
            total = total + sold    
    print(f"Cуммарное количество продаж всех товаров: {total}")
    print('\n')
def get_average_sales_for_all_products(sales_stats):
    total = 0
    items = 0
    for item in sales_stats:
        for sold in item['items_sold']:
            total = total + sold
            items +=1
        average_sales = total / items       
    print(f"Cреднее количество продаж всех товаров: {average_sales}")
    
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sales_stats =   [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    get_total_sales_for_each_product(sales_stats)
    get_average_sales_for_each_product(sales_stats)
    get_total_sales_for_all_products(sales_stats)
    get_average_sales_for_all_products(sales_stats)

    
if __name__ == "__main__":
    main()

