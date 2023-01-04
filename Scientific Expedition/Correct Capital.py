def correct_capital(line: str) -> bool:
    # your code here
    return line == line.lower() or line == line.upper() or line == line.capitalize()


print("Example:")
print(correct_capital("Checkio"))

assert correct_capital("Checkio") == True
assert correct_capital("CheCkio") == False
assert correct_capital("CHECKIO") == True

print("The mission is done! Click 'Check Solution' to earn rewards!") 