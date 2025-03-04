def arithmetic_arranger(problems, show_answers=False):
    
    # İşlem Sayısı En Fazla 5 Olması Durumu
    if len(problems) > 5:
        return 'Error: Too many problems.'
    

        aranged_problems =" "
        birinci_satir = " "
        ikinci_satir = " "
        kisacizgi_satiri = " "
        soru_satiri = " "
        

    for problem in problems:
        parts=problem.split()
        operand1, operators, operand2 = parts

    # Fonksiyonda "+" veya "-" operatörü yoksa

        if operators not in ["+", "-"]:
            return  "Hata: '+' veya '-' operatörü olmalıdır."
    # Fonksiyonda Sadece Rakamlar Yoksa
        if not operand1.isdigit() or not operand2.isdigit():
            return 'Hata: Sayılar yalnızca rakam içermelidir.'
        
    # Fonksiyon en fazla 4 hane yoksa

        if len(operand1) > 4 or len(operand2) > 4:
            return 'Hata: Sayılar dört haneden fazla olamaz.'


        width= max(len(operand1), len(operand2)) +2
        aranged_problems["birinci_satir"] += operand1.rust(width) + " "  # type: ignore
        aranged_problems["ikinci_satir"] += operand2.rust(width-2) + " "  # type: ignore
        aranged_problems["kisacizgi_satiri"] += "-" * width + " "  # type: ignore
        if show_answers:
            if operators == "+":
                answer = str(int(operand1)) + str(int(operand2))
            else:
                answer = str(int(operand1)) - str(int(operand2))
            aranged_problems["soru_satiri"] += answer_rjust(width) + " " # type: ignore

            aranged_output = aranged_problems["birinci_satir"].rstrip() + "\n" # type: ignore
            aranged_output = aranged_problems["ikinci_satir"].rstrip() + "\n" # type: ignore
            aranged_output = aranged_problems["kisacizgi_satiri"].rstrip() # type: ignore

            if show_answers:
                arranged_output += "\n" + aranged_problems["soru_satiri"].rstrip() # type: ignore

    return aranged_problems # type: ignore
