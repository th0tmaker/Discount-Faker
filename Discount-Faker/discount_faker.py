import copy

article_list = [
    {"item": "jeans", "category": "pants", "price": 45},
    {"item": "sweatshirt", "category": "shirts", "price": 30},
    {"item": "boots", "category": "shoes", "price": 85},
    {"item": "cargo", "category": "pants", "price": 50},
    {"item": "t-shirt", "category": "shirts", "price": 20},
    {"item": "sandals", "category": "shoes", "price": 35},
    {"item": "slacks", "category": "pants", "price": 80},
    {"item": "suit", "category": "shirts", "price": 130},
    {"item": "dress shoes", "category": "shoes", "price": 110},
    {"item": "shorts", "category": "pants", "price": 40},
    {"item": "vest", "category": "shirts", "price": 20},
    {"item": "flip-flops", "category": "shoes", "price": 10},
]


def increase_price_by_percentage(clothing, category, percentage):
    for i in clothing:
        if i["category"] == category:
            i["price"] += i["price"] * (percentage / 100)


def display_price_increase(article_lst, new_article_lst):
    for a in range(len(article_lst)):
        article_old = article_lst[a]
        article_new = (new_article_lst[a])
        old_price = article_old["price"]
        new_price = article_new["price"]
        # if new price is whole num, convert to int
        if int(new_price) == round(new_price):
            new_price = int(new_price)
        # if not, stay float and round num to one decimal point
        else:
            new_price = round(new_price, 1)
        print(f"{article_old['item']} ({article_old['category']}):"
              f" [${old_price}] <= ~~${new_price}~~")


category_input = input("Enter category of clothing(pants/shirts/shoes): ")
percentage_input = int(input("Enter the percentage of price increase: "))
new_article_list = copy.deepcopy(article_list)

increase_price_by_percentage(new_article_list, category_input, percentage_input)
display_price_increase(article_list, new_article_list)
