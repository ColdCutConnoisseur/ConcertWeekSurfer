"""Various helper functions"""




def price_cleanup(raw_price: str) -> float:
    # Remove '$' char
    no_sign = str(raw_price).replace('$', '')

    as_float = float(no_sign)

    return as_float
