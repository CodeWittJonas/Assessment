# Testing

This test suite is meant to help while doing the assignments. With it, you can test your code against the test cases defined in the `*_test.py` files and get feedback before uploading your solutions.



In order to run the test, the test files need to be in the same folder as your code.

Afterwards,  in a shell go to the folder with your code and the tests and run:

```bash
python3 task_N_test.py -b -v
```

It should only take a second for you to get a report on how many test cases passed and, if any did not, which ones failed.



We will use these tests, along with others, in grading your solution!

## Pass

If all tests pass you should see a similar message as this (note that the number of test cases provided is different for each test file):



```bash
test_100_is_not_prime (__main__.Task4Test)
100 is not prime ... ok
test_13_is_prime (__main__.Task4Test)
13 is prime ... ok
test_3_is_prime (__main__.Task4Test)
3 is prime ... ok
test_4_is_not_prime (__main__.Task4Test)
4 is not prime ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK

```



## Fail

In case any test fail, you will be notified with a message similar to this:

```bash
test_100_is_not_prime (__main__.Task4Test)
100 is not prime ... ok
test_13_is_prime (__main__.Task4Test)
13 is prime ... ok
test_3_is_prime (__main__.Task4Test)
3 is prime ... FAIL
test_4_is_not_prime (__main__.Task4Test)
4 is not prime ... FAIL

======================================================================
FAIL: test_3_is_prime (__main__.Task4Test)
3 is prime
----------------------------------------------------------------------
Traceback (most recent call last):
  File "task_4_test.py", line 36, in test_3_is_prime
    self.assertEqual(exercise.is_prime, False, "'is_prime' value seems wrong")
AssertionError: True != False : 'is_prime' value seems wrong

======================================================================
FAIL: test_4_is_not_prime (__main__.Task4Test)
4 is not prime
----------------------------------------------------------------------
Traceback (most recent call last):
  File "task_4_test.py", line 44, in test_4_is_not_prime
    self.assertEqual(exercise.is_prime, True, "'is_prime' value seems wrong")
AssertionError: False != True : 'is_prime' value seems wrong

----------------------------------------------------------------------
Ran 4 tests in 0.003s

FAILED (failures=2)

```