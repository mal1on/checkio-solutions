def long_pressed(text: str, typed: str) -> bool:
    # your code here
    result = True if text != typed else False
    count = 0
    for char in typed:
        if char == text[count]:
            result == True
            if count + 1 <= len(text) - 1:
                if text[count] == text[count + 1]:
                    count += 1
        elif count == len(text) - 1:
            return False
        elif char == text[count + 1]:
            count += 1
            result == True
        else:
            return False
    return result


print("Example:")
print(long_pressed("alex", "aaleex"))

assert long_pressed("alex", "aaleex") == True
assert long_pressed("welcome to checkio", "weeeelcome to cccheckio") == True
assert long_pressed("there is an error here",
                    "there is an errorrr hereaa") == False
assert long_pressed("hi, my name is...", "hi, my name is...") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
