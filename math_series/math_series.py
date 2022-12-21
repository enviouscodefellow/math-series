def fibonacci(n, view):
    fib_series_start = [0, 1]
    fib_series_query = [0, 1]
    # fib_series_query = fib_series_start.append(fib_series_start[len()])

    if n < 0:
        print("Please enter a number >= 0.")
        fibonacci(n)
    if n == 0:
        print(f"{n}th number in Fibonacci sequence is 0")
        return 0
    if n == 1:
        print(f"{n}th number in Fibonacci sequence is 1")
        return 1
    if n > 1:
        for i in range(n-1):
            fib_series_query.append((fib_series_query[-1] + fib_series_query[-2]))
        if view == "y":
            # print(fib_series_query)
            for x in fib_series_query:
                print(x)
        return fib_series_query[n]


def lucas(n, view):
    luc_series_query = [2, 1]

    if n < 0:
        print("Please enter a number >= 0.")
        lucas(n)
    if n == 0:
        print(f"{n}th number in Lucas Numbers is 2")
        return 0
    if n == 1:
        print(f"{n}th number in Lucas Numbers is 1")
        return 1
    if n > 1:
        for i in range(n-1):
            luc_series_query.append((luc_series_query[-1] + luc_series_query[-2]))
        if view == "y":
            # print(luc_series_query)
            for x in luc_series_query:
                print(x)
        return luc_series_query[n]


print("""
    Which sequence would you like to find a number in?
    Please enter '0' for Fibonacci Series or '1' for Lucas Numbers.
    """)
sequence = input("> ")
print("""
    Which sequence number would you like to find?
    Please enter an integer >= 0.
    """)
n = input("> ")
print(f"""
    Would you like to view the entire sequence until the {n}th number?
    Please enter 'y' for yes or 'n' for no.
    """)
view = input("> ")
# fibonacci(int(n))
if int(sequence) == 0:
    print(f"""
    The {n}th number in Fibonacci Series is:
    {fibonacci(int(n), view)}
    """)
if int(sequence) == 1:
    print(f"""
    The {n}th number in Lucas Numbers is:
    {lucas(int(n), view)}
    """)