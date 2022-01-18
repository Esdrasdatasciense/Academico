#resultado
vitoria = 0
vitoriacasa = 0
vitoriafora = 0
vitoriaptempo = 0
vitoriastempo = 0
vitoriaptempocasa = 0
vitoriastempocasa = 0
vitoriaptempofora = 0
vitoriastempofora = 0

#resultado2
derrota = 0
derrotacasa = 0
derrotafora = 0
derrotaptempo = 0
derrotastempo = 0
derrotaptempocasa = 0
derrotastempocasa = 0
derrotaptempofora = 0
derrotastempofora = 0

#resultado3
empate = 0
empatecasa = 0
empatefora = 0
empateptempo = 0
empatestempo = 0
empateptempocasa = 0
empatestempocasa = 0
empateptempofora = 0
empatestempofora = 0
escanteiocasa = 0
escanteiofora = 0






#gols feitos em casa e fora
golcasa = 0
golfora = 0
sofricasa = 0
sofrifora = 0

#gols feitos no total
golmarc = 0
golsofri = 0
totaldegols = 0
sofridegols = 0


#fora de casa
golfptempo = 0
golfstempo = 0
sofrifptempo = 0
sofrifstempo = 0
jogofora = 0
escanteiosofricasa = 0
escanteiofora = 0
escanteiosofrifora = 0


#em casa
golptempo = 0
golstempo = 0
sofriptempo = 0
sofristempo = 0
jogocasa = 0
totaldegolsofri = 0


mediastempo = 0
aux1 = 7
otoaux = 0
otoaux2 = 0
auxxx = 0
auxxx2 = 0
jogo = 0


timecasa = str(input("Digite o time a ser analisado: "));


print("\nVamos analisar o time da casa:\n ");
while (aux1 != 0):
    aux2 = str(input("No último jogo o time jogou em casa ou fora?: "));
    if (aux2 == "casa"):
        golmarc = int(input("Quantos gols o time fez?: "));
        totaldegols = totaldegols + golmarc
        golcasa = golcasa + golmarc
        aux3 = int(input("Quantos gols no primeiro tempo?: "));
        golptempo = aux3 + golptempo
        aux4 = int(input("Quantos gols no segundo tempo?: "));
        golstempo = aux4 + golstempo
        golsofri = int(input("Quantos gols o time sofreu?: "));
        sofricasa = golsofri + sofricasa
        totaldegolsofri = totaldegolsofri + golsofri
        if (golmarc > golsofri):
            vitoria = vitoria + 1
            vitoriacasa = vitoriacasa + 1
        elif (golmarc < golsofri):
            derrota = derrota + 1
            derrotacasa = derrotacasa + 1
        else:
            empate = empate + 1
            empatecasa = empatecasa + 1
        
        aux5 = int(input("Quantos gols sofridos no primeito tempo?: "));
        sofriptempo = aux5 + sofriptempo
        if (aux3 > aux5):
            vitoriaptempo = vitoriaptempo + 1
            vitoriaptempocasa = vitoriaptempocasa + 1
        elif (aux3 < aux5):
            derrotaptempo = derrotaptempo + 1
            derrotaptempocasa = derrotaptempocasa + 1
        else:
            empateptempo = empateptempo + 1
            empateptempocasa = empateptempocasa + 1
        aux6 = int(input("Quantos gols sofridos no segundo tempo?: "));
        sofristempo = aux6 + sofristempo
        jogo = jogo + 1
        jogocasa = jogocasa + 1
        if (aux4 > aux6):
                vitoriastempo = vitoriastempo + 1
                vitoriastempocasa = vitoriastempocasa + 1 
        elif (aux4 < aux6):
                derrotastempo = derrotastempo + 1
                derrotastempocasa = derrotastempocasa + 1
        else:
                empatestempo = empatestempo + 1
                empatestempocasa = empatestempocasa + 1
        zzz = str(input("Deseja entrar no mercado escanteio?: "));
        if (zzz == "sim"):
            zzz1 =  int(input("Quantos escanteios teve o time da casa?: "));
            escanteiocasa = escanteiocasa + zzz1
            zzz2 = int(input("Quantos escanteios sofridos teve o time da casa?: "));
            escanteiosofricasa = escanteiosofricasa + zzz2
        else:
            print("OK")
        x = str(input("Deseja analisar outro jogo?: "));
        if (x == "sim"):
            aux1 = aux1 + 1
        else:
            aux1 = 0
    else:
        golmarc = int(input("Quantos gols o time fez?: "));
        golfora = golfora + golmarc
        totaldegols = totaldegols + golmarc
        aux13 = int(input("Quantos gols no primeiro tempo?: "));
        golfptempo = aux13 + golfptempo
        aux14 = int(input("Quantos gols no segundo tempo?: "));
        golfstempo = aux14 + golfstempo
        golsofri = int(input("Quantos gols o time sofreu?: "));
        sofrifora = golsofri + sofrifora
        totaldegolsofri = totaldegolsofri + golsofri
        if (golmarc > golsofri): 
            vitoria = vitoria + 1
            vitoriafora = vitoriafora + 1
        elif (golmarc < golsofri):
            derrota = derrota + 1
            derrotafora = derrotafora + 1
            
        else:
            empate = empate + 1
            empatefora = empatefora + 1
        aux15 = int(input("Quantos gols sofridos no primeito tempo?: "));
        sofrifptempo = aux15 + sofrifptempo
        aux16 = int(input("Quantos gols sofridos no segundo tempo?: "));
        sofrifstempo = aux16 + sofrifstempo
        if (aux13 > aux15):
            vitoriaptempo = vitoriaptempo + 1
            vitoriaptempofora = vitoriaptempofora +1 
        elif (aux13 < aux15):
            derrotaptempo = derrotaptempo + 1
            derrotaptempofora = derrotaptempofora + 1
        else:
            empateptempo = empateptempo + 1
            empateptempofora = empateptempofora + 1
        if (aux14 > aux16):
                vitoriastempo = vitoriastempo + 1
                vitoriastempofora = vitoriastempofora + 1
        elif (aux14 < aux16):
                derrotastempo = derrotastempo + 1
                derrotastempofora = derrotastempofora + 1            
        else:
                empatestempo = empatestempo + 1
                empatestempofora = empatestempofora + 1
        jogo = jogo + 1
        jogofora = jogofora + 1
        yyy= str(input("Deseja entrar no mercado escanteio?: "));
        if (yyy == "sim"):
            yyy1 =  int(input("Quantos escanteios teve o time de fora?: "));
            escanteiofora = escanteiofora + yyy1
            yyy2 = int(input("Quantos escanteios sofridos teve o time de fora?: "));
            escanteiosofrifora = escanteiosofrifora + yyy2
        else:
            print("OK")
        x = str(input("Deseja analisar outro jogo?: "));
        if (x == "sim"):
            aux1 = aux1 + 1
        else:
            aux1 = 0

sofriauxxx2 = sofristempo/jogocasa
auxxx2 = golstempo/jogocasa
otoaux2 = golstempo + golfstempo
sofriotoaux2 = sofrifstempo + sofristempo
mediastempo = otoaux2/jogo
mediasofristempo = sofriotoaux2/jogo
otoaux = golptempo + golfptempo
sofriotoaux = sofrifptempo + sofriptempo
mediaptempo = otoaux/jogo
mediasofriptempo = sofriotoaux/jogo
auxxx = golptempo/jogocasa
sofriauxxx = sofriptempo/jogocasa
mediagolsporjogo = totaldegols/jogo
mediagolsofriporjogo = totaldegolsofri/jogo
mediagolsemcasa = golcasa/jogocasa
mediagolsfora = golfora/jogofora
mediagolsofrifora = sofrifora/jogofora
ototo = golfptempo/jogofora
sofriototo = sofrifptempo/jogofora
ototo2 = golfstempo/jogofora
sofriototo2 = sofrifstempo/jogofora
mediagolsofriemcasa = sofricasa/jogocasa
mediavitoria = vitoria/jogo
mediavitoriacasa = vitoriacasa/jogocasa
mediavitoriafora = vitoriafora/jogofora
mediavitoriaptempo = vitoriaptempo/jogo
mediavitoriastempo = vitoriastempo/jogo
mediavitoriaptempocasa = vitoriaptempocasa/jogocasa
mediavitoriastempocasa = vitoriastempocasa/jogocasa
mediavitoriaptempofora = vitoriaptempofora/jogofora
mediavitoriastempofora = vitoriastempofora/jogofora
mediaderrota = derrota/jogo
mediaderrotacasa = derrotacasa/jogocasa
mediaderrotafora = derrotafora/jogofora
mediaderrotaptempo = derrotaptempo/jogo
mediaderrotastempo = derrotastempo/jogo
mediaderrotaptempocasa = derrotaptempocasa/jogocasa
mediaderrotastempocasa = derrotastempocasa/jogocasa
mediaderrotaptempofora = derrotaptempofora/jogofora
mediaderrotastempofora = derrotastempofora/jogofora

mediaempate = empate/jogo
mediaempatecasa = empatecasa/jogocasa
mediaempatefora = empatefora/jogofora
mediaempateptempo = empateptempo/jogo
mediaempatestempo = empatestempo/jogo
mediaempateptempocasa = empateptempocasa/jogocasa
mediaempatestempocasa = empatestempocasa/jogocasa
mediaempateptempofora = empateptempofora/jogofora
mediaempatestempofora = empatestempofora/jogofora

mediaescanteiocasa = escanteiocasa/jogocasa
mediaescanteiosofricasa = escanteiosofricasa/jogocasa
mediaescanteiofora = escanteiofora/jogofora
mediaescanteiosofrifora = escanteiosofrifora/jogofora

print(("\n=" * 5), "RESULTADO GERAL", ("=" * 20))
print("\nO numero de vitorias é: ", vitoria, " em ", jogo, "jogos")
print("\nO numero de derrotas é: ", derrota, " em ", jogo, "jogos")
print("\nO numero de empates é: ", empate, " em ", jogo, "jogos")
print("\nTotal de gols do ",timecasa, "é: ", totaldegols, "em " , jogo, "jogos")
print("\nTotal de gols SOFRIDOS do ",timecasa, "é: ", totaldegolsofri, "em " , jogo, "jogos")
print(("\n=" * 5), "MEDIA RESULTADO", ("=" * 20))
print("\nA média de vitorias é: ", mediavitoria)
print("\nA média de derrotas é: ", mediaderrota)
print("\nA média de empates é: ", mediaempate)
print("\nA média de gols desse time é: ", mediagolsporjogo,"por jogo")
print("\nA média de gols SOFRIDOS desse time é: ", mediagolsofriporjogo,"por jogo")
print(("\n=" * 5), "RESULTADO EM CASA", ("=" * 20))
print("\nEm casa o time tem: ", vitoriacasa, " vitórias em ", jogocasa, "Jogos")
print("\nEm casa o time tem: ", derrotacasa, " derrotas em ", jogocasa, "Jogos")
print("\nEm casa o time tem: ", empatecasa, " empates em ", jogocasa, "Jogos")
print("\nJogando em casa o time fez", golcasa, "gols em", jogocasa, "jogos")
print("\nJogando em casa o time SOFREU", sofricasa, "gols em", jogocasa, "jogos")
print("\nO time teve: ", escanteiocasa, "Escanteios em: ", jogocasa, " Jogando em casa")
print("\nO time sofreu: ", escanteiosofricasa, "Escanteios em: ", jogocasa, " Jogando em casa")
print(("\n=" * 5), "MEDIA EM CASA", ("=" * 20))
print("\nA média de vitória em casa é: ", mediavitoriacasa)
print("\nA média de derrota em casa é: ", mediaderrotacasa)
print("\nA média de empate em casa é: ", mediaempatecasa)
print("\nA média de gols em casa é: ", mediagolsemcasa, "por jogo")
print("\nA média de gols SOFRIDOS em casa é: ", mediagolsofriemcasa, "por jogo")
print("\nA média de escanteios em casa é: ", mediaescanteiocasa)
print("\nA média de escanteios sofridos em casa é: ", mediaescanteiosofricasa)
print(("\n=" * 5), "RESULTADO FORA DE CASA", ("=" * 20))
print("\nFora de casa o time tem: ", vitoriafora, " em ", jogofora, "Jogos")
print("\nFORA DE casa o time tem: ", derrotafora, " derrotas em ", jogofora, "Jogos")
print("\nFORA DE casa o time tem: ", empatefora, " empates em ", jogofora, "Jogos")
print("\nJogando fora de casa o time fez", golfora, "gols em", jogofora, "jogos")
print("\nJogando fora de casa o time SOFREU", sofrifora, "gols em", jogofora, "jogos")
print("\nO time teve: ", escanteiofora, "Escanteios em: ", jogofora, " Jogando em FORA DE casa")
print("\nO time sofreu: ", escanteiosofrifora, "Escanteios em: ", jogofora, " Jogando FORA DE casa")
print(("\n=" * 5), "MEDIA FORA DE CASA", ("=" * 20))
print("\nA média de vitória FORA de casa é: ", mediavitoriafora)
print("\nA média de derrota FORA DE casa é: ", mediaderrotafora)
print("\nA média de empates FORA DE casa é: ", mediaempatefora)
print("\nA média de gols fora de casa é: ", mediagolsfora, "por jogo")
print("\nA média de gols SOFRIDOS fora de casa é: ", mediagolsofrifora, "por jogo")
print("\nA média de escanteios FORA DE casa é: ", mediaescanteiofora)
print("\nA média de escanteios sofrido FORA DE casa é: ", mediaescanteiosofrifora)
print(("\n=" * 5), "PRIMEIRO TEMPO", ("=" * 20))
print("\nO time ganhou: ", vitoriaptempo, " jogos no primeiro tempo em: ", jogo)
print("\nO time perdeu: ", derrotaptempo, " jogos no primeiro tempo em: ", jogo)
print("\nO time empatou: ", empateptempo, " jogos no primeiro tempo em: ", jogo)
print("\nO time marcou ", otoaux," gols no primeiro tempo em ",jogo, " jogos")
print("\nO time SOFREU ", sofriotoaux," gols no primeiro tempo em ",jogo, " jogos")
print(("\n=" * 5), "PRIMEIRO TEMPO EM CASA", ("=" * 20))
print("\nO numero de vitorias no primeiro tempo EM CASA é: ", vitoriaptempocasa, " em ", jogocasa, "jogos")
print("\nO numero de derrotas no primeiro tempo EM CASA é: ", derrotaptempocasa, " em ", jogocasa, "jogos")
print("\nO numero de empates no primeiro tempo EM CASA é: ", empateptempocasa, " em ", jogocasa, "jogos")
print("\nJogando em CASA o time fez: ", golptempo, " gols no primeiro tempo em ", jogocasa, "Jogos")
print("\nJogando em CASA o time SOFREU: ", sofriptempo, " gols no primeiro tempo em ", jogocasa, "Jogos")
print(("\n=" * 5), "PRIMEIRO TEMPO FORA DE CASA", ("=" * 20))
print("\nO numero de vitorias no primeiro tempo FORA DE CASA é: ", vitoriaptempofora, " em ", jogofora, "jogos")
print("\nO numero de derrotas no primeiro tempo FORA DE CASA é: ", derrotaptempofora, " em ", jogofora, "jogos")
print("\nO numero de empates no primeiro tempo FORA DE CASA é: ", empateptempofora, " em ", jogofora, "jogos")
print("\nJogando FORA DE CASA o time fez: ", golfptempo, " gols no primeiro tempo em ", jogofora, "Jogos")
print("\nJogando FORA DE CASA o time SOFREU: ", sofrifptempo, " gols no primeiro tempo em ", jogofora, "Jogos")
print(("\n=" * 5), "MEDIA PRIMEIRO TEMPO", ("=" * 20))
print("\nA média de vitorias no primeiro tempo é: ", mediavitoriaptempo)
print("\nA média de derrotas no primeiro tempo é: ", mediaderrotaptempo)
print("\nA média de empates no primeiro tempo é: ", mediaempateptempo)
print("\nA média de gols no primeiro tempo é: ", mediaptempo)
print("\nA média de gols SOFRIDOS no primeiro tempo é: ", mediasofriptempo)
print(("\n=" * 5), "MEDIA PRIMEIRO TEMPO EM CASA", ("=" * 20))
print("\nA média de vitorias no primeiro tempo EM CASA é: ", mediavitoriaptempocasa)
print("\nA média de derrota no primeiro tempo EM CASA é: ", mediaderrotaptempocasa)
print("\nA média de empate no primeiro tempo EM CASA é: ", mediaempateptempocasa)
print("\nA media de gols no primeiro tempo jogando em casa é: ", auxxx)
print("\nA media de gols SOFRIDOS no primeiro tempo jogando em casa é: ", sofriauxxx)
print(("\n=" * 5), "MEDIA PRIMEIRO TEMPO FORA DE CASA", ("=" * 20))
print("\nA média de vitorias no prmeiro tempo FORA DE CASA é: ", mediavitoriaptempofora)
print("\nA média de derrotas no prmeiro tempo FORA DE CASA é: ", mediaderrotaptempofora)
print("\nA média de empates no prmeiro tempo FORA DE CASA é: ", mediaempateptempofora)
print("\nA media de gols no primeiro tempo jogando fora de casa é: ", ototo)
print("\nA media de gols SOFRIDOS no primeiro tempo jogando fora de casa é: ", sofriototo)
print(("\n=" * 5), "SEGUNDO TEMPO", ("=" * 20))
print("\nO time ganhou: ", vitoriastempo, " jogos no segundo tempo em: ", jogo)
print("\nO time perdeu: ", derrotastempo, " jogos no segundo tempo em: ", jogo)
print("\nO time empatou: ", empatestempo, " jogos no segundo tempo em: ", jogo)
print("\nO time marcou ", otoaux2, " gols no segundo tempo em ", jogo, " jogos")
print("\nO time SOFREU ", sofriotoaux2, " gols no segundo tempo em ", jogo, " jogos")
print(("\n=" * 5), "SEGUNDO TEMPO EM CASA", ("=" * 20))
print("\nO numero de vitorias no segundo tempo EM CASA é: ", vitoriastempocasa, " em ", jogocasa, "jogos")
print("\nO numero de derrotas no segundo tempo EM CASA é: ", derrotastempocasa, " em ", jogocasa, "jogos")
print("\nO numero de empates no segundo tempo EM CASA é: ",empatestempocasa, " em ", jogocasa, "jogos")
print("\nJogando em CASA o time fez: ", golstempo, " gols no segundo tempo em ", jogocasa, "Jogos")
print("\nJogando em CASA o time SOFREU: ", sofristempo, " gols no segundo tempo em ", jogocasa, "Jogos")
print(("\n=" * 5), "SEGUNDO TEMPO FORA DE CASA", ("=" * 20))
print("\nO numero de vitorias no segundo tempo FORA DE CASA é: ", vitoriastempofora, " em ", jogofora, "jogos")
print("\nO numero de derrotas no segundo tempo FORA DE CASA é: ", derrotastempofora, " em ", jogofora, "jogos")
print("\nO numero de empates no segundo tempo FORA DE CASA é: ", empatestempofora, " em ", jogofora, "jogos")
print("\nJogando FORA DE CASA o time fez: ", golfstempo, " gols no segundo tempo em ", jogofora, "Jogos")
print("\nJogando FORA DE CASA o time SOFREU: ", sofrifstempo, " gols no segundo tempo em ", jogofora, "Jogos")
print(("\n=" * 5), "MEDIA SEGUNDO TEMPO", ("=" * 20))
print("\nA média de vitorias no segundo tempo é: ", mediavitoriastempo)
print("\nA média de derrotas no segundo tempo é: ", mediaderrotastempo)
print("\nA média de empates no segundo tempo é: ", mediaempatestempo)
print("\nA média de gols no segundo tempo é: ", mediastempo)
print("\nA média de gols SOFRIDOS no segundo tempo é: ", mediasofristempo)
print(("\n=" * 5), "MEDIA SEGUNDO TEMPO EM CASA", ("=" * 20))
print("\nA média de vitorias no segundo tempo EM CASA é: ", mediavitoriastempocasa)
print("\nA média de derrotas no segundo tempo EM CASA é: ", mediaderrotastempocasa)
print("\nA média de empates no segundo tempo EM CASA é: ", mediaempatestempocasa)
print("\nA media de gols no segundo tempo jogando em casa é: ", auxxx2)
print("\nA media de gols SOFRIDO no segundo tempo jogando em casa é: ", sofriauxxx2)
print(("\n=" * 5), "MEDIA SEGUNDO TEMPO FORA DE CASA", ("=" * 20))
print("\nA média de vitorias no segundo tempo FORA DE CASA é: ", mediavitoriastempofora)
print("\nA média de derrotas no segundo tempo FORA DE CASA é: ", mediaderrotastempofora)
print("\nA média de empates no segundo tempo FORA DE CASA é: ", mediaempatestempofora)
print("\nA media de gols no segundo tempo jogando fora de casa é: ", ototo2)
print("\nA media de gols SOFRIDOS no segundo tempo jogando fora de casa é: ", sofriototo2)

encerrar = str(input("DIGITE ENTER P ENCERRAR: "))

