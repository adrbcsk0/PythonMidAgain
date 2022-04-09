# colorList = ["red", "orange", "green", "violet", "blue", "yellow"]
#
# def newColorList(colorList, n):
#     print (colorList[:n])
#     newList = []
#
#     for i in range(n):
#         newList.append(colorList[n])
#         newColorList(colorList, 3)
#
#
#
# newColorList(colorList, 3)

# zadanie 2

txt = """Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką 
prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. 
W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. 
Rządzi w niej prawo dżungli."""


#rozwiązanie z kursu

print(txt[txt.index('(')+1:txt.index(')')])