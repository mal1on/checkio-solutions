def friendly_number(
    number,
    base=1000,
    decimals=0,
    suffix="",
    powers=["", "k", "M", "G", "T", "P", "E", "Z", "Y"],
):
    """
    Format a number as friendly text, using common suffixes.
    """

    power = 0 
    m_base = base
    while abs(number) >= m_base:
        power += 1
        m_base = base ** power
    power = 0 if abs(number) < base else power - 1
    power = power if len(powers) > power else len(powers) - 1                         
    divided = number / (base**power) if decimals else int(number / base**power)
    result = f'{round(divided, decimals):.{decimals}f}{powers[power]}{suffix}'    
        
    return result



# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert friendly_number(102) == "102", "102"
    assert friendly_number(10240) == "10k", "10k"
    assert friendly_number(12341234, decimals=1) == "12.3M", "12.3M"
    assert friendly_number(12461, decimals=1) == "12.5k", "12.5k"
    assert friendly_number(1024000000, base=1024, suffix="iB") == "976MiB", "976MiB"