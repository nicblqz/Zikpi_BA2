# IN : numéro de la note [1,60]
# Prend le numéro de la note et lui associe un voltage qui va de 1 à 5
# OUT : nom de la note associé au numéro de la note

def Note(num_note):
    Lettre_note = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    octave = int((num_note*5)/60 + 0.99)
    lettre = num_note % 12

    return Lettre_note[lettre - 1] + str(octave)



for i in range(1,61,1) :
    print(Note(i))
    

class Gamme :
    
    def __init__(self, num_gam) :
        
        if num_gam == 1 :
            self.name = "Chromatique"
        elif num_gam == 2 :
            self.name = "Majeur"
        elif num_gam == 3 :
            self.name = "Mineur"
            
    def chiffretonum(SEQ) :  
        dico_note,num = {}, 1
    
        for pas in SEQ.keys() :
            chiffre_note = SEQ[pas]["note"]
            num_note = int(chiffre_note*60/4096 + 0.99)
            dico_note["note{}".format(num)] = num_note
            num +=1
        
        return dico_note

    def transformation_affichage(dico_note) :
        
        if self.name == "Chromatique" :
            for note in dico_note.keys() :
                Lettre_note = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
                octave = int((dico_note[note]*5)/60 + 0.99)
                lettre = dico_note[note] % 12
                dico_note[note] = Lettre_note[lettre - 1] + str(octave)
                
        elif self.name == "Majeur" :
            for note in dico_note.keys() :
                Lettre_note = ["C", "D", "E", "F", "G", "A", "B"]
                octave = int((dico_note[note]*5)/60 + 0.99)
                lettre = dico_note[note] % 7
                dico_note[note] = Lettre_note[lettre - 1] + str(octave)
                
        elif self.name == "Mineur" :
            for note in dico_note.keys() :
                Lettre_note = ["C", "D", "D#", "F", "G", "G#", "A#"]
                octave = int((dico_note[note]*5)/60 + 0.99)
                lettre = dico_note[note] % 7
                dico_note[note] = Lettre_note[lettre - 1] + str(octave)
                
        return dico_note
            
        

