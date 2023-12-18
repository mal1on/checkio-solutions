def unique_emails(emails: list[str]) -> int:

    return len(set([''.join([l for l in mail.split('@')[0] if l != '.']).split('+')[0] for mail in emails]))


print("Example:")
print(unique_emails(["alex@checkio.org", "mike@google.com", "lili@apple.com"]))

assert unique_emails(
    ["alex@checkio.org", "mike@google.com", "lili@apple.com"]) == 3
assert (
    unique_emails(
        ["mi.ke@google.com", "alex@checkio.org",
            "mike@google.com", "lili@apple.com"]
    )
    == 3
)
assert (
    unique_emails(
        [
            "alex+home@checkio.org",
            "lili+work@apple.com",
            "alex@checkio.org",
            "lili@apple.com",
        ]
    )
    == 2
)
assert (
    unique_emails(
        [
            "l.ili+work@apple.com",
            "a.lex@checkio.org",
            "alex+home@checkio.org",
            "lili+work@apple.com",
            "alex@checkio.org",
            "lili@apple.com",
        ]
    )
    == 2
)
assert unique_emails(
    ["Alex@checkIO.org", "alex@checkio.org", "alex@check.io.org"]) == 2
assert unique_emails([]) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")
