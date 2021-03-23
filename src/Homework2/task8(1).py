# Условие:
# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given  scores.
# Store them in a list and find the score of the runner-up.
# Input Format:
# The first line contains n. The second line contains an array A[] of n
# integers each separated by a space.
# Output Format:
# Print the runner-up score.
# Ссылка:
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

amount_of_numbers = int(input())
list_ = input().split()
list_.sort()
list_.reverse()
first_place = list_[0]
for runner_up in list_:
    if runner_up != first_place:
        break
# noinspection PyUnboundLocalVariable
print(runner_up)
