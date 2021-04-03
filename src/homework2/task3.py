text = "abcd if aa aaa aaa aa"
list_chars = text.replace(" ", "")
i = 0
new_str = ""
while i < len(list_chars):
    if i == 0:
        new_str = new_str + list_chars[i]
        i += 1
        continue
    if list_chars[i] in new_str:
        i += 1
        continue
    new_str = new_str + list_chars[i]
    i += 1

print(new_str)
