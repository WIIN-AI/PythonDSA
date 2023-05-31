
def hello_world(count=0):
    """
    This is sample recursion call
    : ensure the BASE Condition
    : ensure the return
    :return:
    """
    if count == 500:  # Base Case
        return        # return condition
    print("Hello World from recursion", count)
    hello_world(count +1) # passing parameters


# hello_world()


def run_fn(n):
    if n==0 : return

    print("UL",n)
    run_fn(n-1)
    print("Final Call ...")


# run_fn(100-1)


def run_fn_lr(n,var1=None):
    if n==0 : return

    print("UL",n,var1)
    run_fn_lr(n-1,var1="left")
    run_fn_lr(n-1,var1="right")



run_fn_lr(11)