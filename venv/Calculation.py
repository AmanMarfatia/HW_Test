def calculate_total(state, items):
    tax_rate = 0
    if state == 'DE':
        tax_rate = 0
    elif state == 'NJ':
        tax_rate = 0.066
    elif state == 'PA':
        tax_rate = 0.06

    total = 0
    for item in items:
        if item['type'] == 'Wic Eligible food':
            total += item['price']
        elif item['type'] == 'Clothing':
            if 'fur' in item['name']:
                total += item['price'] * (1 + tax_rate)
            else:
                total += item['price']
        else:
            total += item['price'] * (1 + tax_rate)

    return round(total, 2)