def hash_tag_creator(s):
    if not s:
        raise ValueError("Error: string is empty")

    words = s.split()
    words = [w.capitalize() for w in words]

    hashtag = "#" + "".join(words)
    if len(hashtag) > 140:
        return False

    return hashtag

print(hash_tag_creator("  Hello   World  "))
print(hash_tag_creator(" "))