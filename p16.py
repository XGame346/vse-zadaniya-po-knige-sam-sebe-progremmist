best_music={"Wildways":
            ["Sarah", "Puzzle", "Страх", "Эхо"],
            "Таймсквер":
            ["У бога много времени","В темноте","Мел"],
            "Eminem":
            ["Not afraid","Venom","Rap God"],
            "Мумий троль":
            "Башня"}
n=input("Введите группу")
if n in best_music:
    fabest_music={"Wildways":
            ["Sarah", "Puzzle", "Страх", "Эхо"],
            "Таймсквер":
            ["У бога много времени","В темноте","Мел"],
            "Eminem":
            ["Not afraid","Venom","Rap God"],
            "Мумий троль":
            "Башня"}
n=input("Введите группу")
if n in best_music:
    fact = best_music[n]
    print(fact)
else:
    print("Попробуйте ещё раз")
