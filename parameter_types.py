def func(p1, p2, *args, k, **kwargs):
    print(f"positional-or-keyword:....{p1}, {p2}")
    print(f"var_positional (*args):...{args}")
    print(f"keyword:..................{k}")
    print(f"var_keyword:...............{kwargs}")


func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)
