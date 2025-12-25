def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def ft_recursion(days):
        if (days > 1):
            ft_recursion(days - 1)
        print("Day ", days)
    ft_recursion(days)
    print("Harvest time!")
