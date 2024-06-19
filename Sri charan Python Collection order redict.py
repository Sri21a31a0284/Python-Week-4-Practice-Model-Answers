if __name__ == "__main__":
    n = int(input())
    supermarket = {}
    order_of_items = []

    for _ in range(n):
        item, _, price = input().rpartition(' ')
        if item not in supermarket:
            order_of_items.append(item)
        supermarket[item] = int(price) + supermarket.get(item, 0)
        
    [print(item, supermarket[item]) for item in order_of_items]
