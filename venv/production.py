from typing import List

TAX_RATES = {
    'NJ': 0.066,
    'DE': 0.00,
    'PA': 0.06
}


def calculate_total(state: str, records: List[dict]) -> float:
    total = 0.0
    for record in records:
        item_name = record['item_name']
        item_price = record['item_price']
        item_type = record['item_type']
        taxable = True

        if item_type == 'Wic Eligible food':
            taxable = False
        elif item_type == 'Clothing':
            if 'fur' not in item_name.lower() and (state == 'NJ' or state == 'PA'):
                taxable = False

        if taxable:
            if state in TAX_RATES:
                total += item_price * (1 + TAX_RATES[state])
            else:
                total += item_price

    return round(total, 2)
