dict_ = {elem: elem**3 for elem in range(1, 21)}
for key, value in dict_.items():
    print("{key} : {value}".format(key=key, value=value), end=" | ")
