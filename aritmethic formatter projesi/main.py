

from pytest import main # type: ignore

from arithmetic_aranger import arithmetic_arranger

problem1= ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
problem2 = [["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True]

arranged_problems1 = arithmetic_arranger(problem1)
arranged_problems2 = arithmetic_arranger(problem2)

print(arranged_problems1)
print(arranged_problems2)