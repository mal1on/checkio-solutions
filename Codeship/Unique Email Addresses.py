def unique_emails(emails: list[str]) -> int:

    return len(set([''.join([l for l in mail.split('@')[0] if l != '.']).split('+')[0] for mail in emails]))


unique_emails(["alex@checkio.org", "mike@google.com", "lili@apple.com"])
unique_emails(["mi.ke@google.com", "alex@checkio.org",
               "mike@google.com", "lili@apple.com"])
unique_emails(["alex+home@checkio.org", "lili+work@apple.com",
               "alex@checkio.org", "lili@apple.com", ])
