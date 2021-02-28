def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """Print a centered string, with ** on either side

    :param text: The string to print.
    If the string is *, it will print a row of asterisks,
    it prints an empty line in the middle and also two asterisks surround each centered string on both sides.
    :param screen_width: The maximum width space to print the string within -includes the four asterisks-.
    :raises ValueError: If the string is too long for the specified width.
    """
    if len(text) > screen_width - 4:
        raise ValueError(f"String {text} is longer than the specified width {screen_width}", 60)

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*")
banner_text("Always look at the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
print()
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")
