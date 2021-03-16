note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

#Question4

#a)

def moyenne_eleve1(liste):
  moyenne = [ item[2]  for item in liste if  item[0]=="eleve1"] 
  moyenne1 = sum(moyenne)/len(moyenne)
  return moyenne1    

print(moyenne_eleve1(notes))

#b)

def moyenne_eleve1(liste):
  moyenne = [ item[2]  for item in liste if  item[0]=="eleve1" and item[1]=="math" ] 
  moyenne1 = sum(moyenne)/len(moyenne)
  return moyenne1    

print(moyenne_eleve1(notes))

#c) permet de choisir la moyenne de se que l'on veut, exemple la moyenne des éléve en maths
#def moyenne_tuples(liste):
  #moyenne = [ item[2]  for item in liste if  item[0]==  input("choisir l'eleve1 ou eleve2 :") and item[1]== input("choisir la matiere , eco, math ou physique :") ] 
  #moyenne1 = sum(moyenne)/len(moyenne)
 # return moyenne1    

#print(moyenne_tuples(notes))



class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('eleve :', self.eleve, 'matiere :', self.matiere, 'note :', self.valeur)


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)


#Question5

note1 = Note('eleve1', 'math', 13)
note2 = Note('eleve1', 'physique', 15)
note3 = Note('eleve1', 'math', 13)
note4 = Note('eleve1', 'eco', 12)
note5 = Note('eleve1', 'eco', 13)
note6 = Note('eleve1', 'math', 12)
note7 = Note('eleve2', 'math', 13)
note8 = Note('eleve2', 'math', 14)

