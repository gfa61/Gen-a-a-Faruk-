def arithmetic_arranger(problems, show_answers=False):
    
    # İşlem Sayısı En Fazla 5 Olması Durumu
    if len(problems) > 5:
        return 'Error: Too many problems.'
    

        aranged_problems =" "
        first_line = " "
        second_line = " "
        dash_line = " "
        answer_line = " "
        

    for problem in problems:
        parts=problem.split()
        operand1, operators, operand2 = parts

    # Fonksiyonda "+" veya "-" operatörü yoksa

        if operators not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
    # Fonksiyonda Sadece Rakamlar Yoksa
        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'
        
    # Fonksiyon en fazla 4 hane yoksa

        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width= max(len(operand1), len(operand2)) +2
        aranged_problems["First_line"] += operand1.rust(width) + " "  # type: ignore
        aranged_problems["Second_line"] += operand2.rust(width-2) + " "  # type: ignore
        aranged_problems[dash_line] += "-" * width + " "  # type: ignore
        if show_answers:
            if operators == "+":
                answer = str(int(operand1)) + str(int(operand2))
            else:
                answer = str(int(operand1)) - str(int(operand2))
            aranged_problems["answer_line"] += answer_rjust(width) + " " # type: ignore

            aranged_output = aranged_problems["first_line"].rstrip() + "\n" # type: ignore
            aranged_output = aranged_problems["second_line"].rstrip() + "\n" # type: ignore
            aranged_output = aranged_problems["dash_line"].rstrip() # type: ignore

            if show_answers:
                arranged_output += "\n" + aranged_problems["answer_line"].rstrip() # type: ignore

    return aranged_problems # type: ignore