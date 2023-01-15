def fibonacci(n, view="n"):
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


def lucas(n, view="n"):
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

def sum_series(n, first_num=0, second_num=1):
    """
    This function takes one required parameter and two optional parameters.
    The required parameter n determines which element in the series to print.
    The two optional parameters first_num and second_num have default values of 0 and 1 respectively, 
    and determine the first two values for the series to be produced.
    If no optional parameters are given, the function will produce numbers from the Fibonacci series. 
    If the optional arguments 2 and 1 are given, the function will produce values from the Lucas numbers.
    Other values for the optional parameters will produce other series.
    """
    if first_num == 0 and second_num == 1:
        return fibonacci(n)
    elif first_num == 2 and second_num == 1:
        return lucas(n)
    else:
        series = [first_num, second_num]
        if n < 0:
            print("Please enter a number >= 0.")
            return None
        if n == 0:
            return first_num
        if n == 1:
            return second_num
        if n > 1:
            for i in range(n-1):
                series.append(series[-1] + series[-2])
            return series[n]


# print("""
#     Which sequence would you like to find a number in?
#     Please enter '0' for Fibonacci Series or '1' for Lucas Numbers.
#     """)
# sequence = input("> ")
# print("""
#     Which sequence number would you like to find?
#     Please enter an integer >= 0.
#     """)
# n = input("> ")
# print(f"""
#     Would you like to view the entire sequence until the {n}th number?
#     Please enter 'y' for yes or 'n' for no.
#     """)
# view = input("> ")
# # fibonacci(int(n))
# if int(sequence) == 0:
#     print(f"""
#     The {n}th number in Fibonacci Series is:
#     {fibonacci(int(n), view)}
#     """)
# if int(sequence) == 1:
#     print(f"""
#     The {n}th number in Lucas Numbers is:
#     {lucas(int(n), view)}
#     """)

print(sum_series(5))
print(sum_series(5,2,1))
print(sum_series(5,0,1))
print(sum_series(5, 5, 1))