from typing import List
def average(salary: List[int]) -> float:
    """
    Given an array of unique integers salary where salary[i] is the salary of the employee i.
    Return the average salary of employees excluding the minimum and maximum salary.
    """
    salary.remove(max(salary))
    salary.remove(min(salary))

    total_salary =  sum(salary)
    return total_salary/len(salary)