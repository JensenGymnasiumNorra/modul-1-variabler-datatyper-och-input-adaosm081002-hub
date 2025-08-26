"""  
Gör ett program som frågar användaren efter namn och ålder.
Programmet ska sedan skriva ut enligt nedan.
Räkna med att man går i pension vid 67 års ålder.

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Hej och välkommen till mitt program (Hampus). Du har (39) år kvar till pension.
"""

namn=input("namn: ")
ålder = 16
pension= 67 - ålder
print(f"hej och välkommen till mitt program {namn}. Du har {pension} år kvar till pension")