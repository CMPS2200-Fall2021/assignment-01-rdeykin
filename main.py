"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.
import collections


def foo(x):
    if x <= 1:
        return x
    else:
        (ra ,rb) = (foo(x-1), foo(x-2))
        return ra + rb

def longest_run(mylist, key):
    run_length = 0
    lengths = []
    for x in range(0,len(mylist)):
        if run_length >= 0 and mylist[x] == key:
            run_length += 1
        elif run_length >= 0 and mylist != key:
            lengths.append(run_length)
            run_length = 0
    return max(lengths)


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))


def combine_results(resultright, resultleft):
    finalresult = Result(0,0,0,False)
    # max of resultRight.longest, resultLeft.longest,
    if resultright.is_entire_range == False and resultleft.is_entire_range == False:
        finalresult = Result(resultleft.left_size, resultright.right_size, max(resultleft.longest_size,resultright.longest_size,
                                                                               (resultleft.right_size + resultright.left_size)), False)
        return finalresult

    if resultright.is_entire_range == True and resultleft.is_entire_range == True:
        run = resultright.longest_size + resultleft.longest_size
        finalresult = Result(run, run, run, True)
        return finalresult
    if resultright.is_entire_range == False and resultleft.is_entire_range == True:

        finalresult = Result((resultleft.longest_size + resultright.left_size), resultright.right_size,
                             max(resultleft.longest_size, resultright.longest_size,
                                 (resultleft.right_size + resultright.left_size)), False)
        return finalresult
    if resultright.is_entire_range == True and resultleft.is_entire_range == False:
        finalresult = Result(resultleft.left_size, (resultright.longest_size + resultleft.right_size),
                             max(resultleft.longest_size, resultright.longest_size,
                                 (resultleft.right_size + resultright.left_size)), False)
        return finalresult


def longest_run_recursive(mylist, key):

    if len(mylist) == 1:
        if mylist[0] == key:
            result = Result(1, 1, 1, True)
            return result
        else:
            result1 = Result(0, 0, 0, False)
            return result1


    resultleft = longest_run_recursive(mylist[:len(mylist) // 2], key)
    resultright = longest_run_recursive(mylist[len(mylist)//2:],key)
    return combine_results(resultleft,resultright)



## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


