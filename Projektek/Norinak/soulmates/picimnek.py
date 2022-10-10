from time import time


class norinak:
    def soulmate():
        import time

        par1 = ["Szebelédi Zoltán", "Palkó Nóra"]
        par2 = ["Horváth Szonja", "Pannuzo Aida"]
        par3 = ["Zoli", "Nóri"]
        
        parok = [par1, par2, par3]
        time.sleep(3)
        print("Halóóó figylesz?")
        time.sleep(3)
        print("De akkor figyelj!!!!!")
        time.sleep(3)

        if input("Figyelsz?: ") == "igen":
            print("------------------------------------------------------")
            time.sleep(2)
            print("Akkor sziaa most leteszteljük hogy soulmate-e kettő ember!!!")
            time.sleep(2)
            print("------------------------------------------------------")
            time.sleep(2)
            x = input("Kérem az első ember nevét: ")
            y = input("Kérem a második ember nevét: ")
            print("Számítások elkezdése...")
            time.sleep(2)
            print("------------------------------------------------------")
            time.sleep(1)

            for par in parok:
                if x == par[0] or x == par[1]:
                    if y == par[0] or y == par[1]:
                        print("Ti soulmate-ek vagytok!!!!")
                        exit()
            
            print("Sajnos nem vagytok soulmate-ek!")
        else:
            print("Akkor kabbe")