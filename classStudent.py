#Define una clase con un atributo de calse cuyo valor sea undergraduate
#Con las siguientes variables de instancia name,ID,GPA,major, en instancia dos objetos
class student:
    level="undergraduate"

    def __init__(self,name,ID,GPA,major):
        self.name=name
        self.ID=ID
        self.GPA=GPA
        self.major=major

    #Añade un método que muestre todos los datos del objeto
    def display(self):
        return(self.name,self.ID,self.GPA,self.major)

s1=student('Jack',90076,3.4,'CS')
s2=student('Nora',90067,3.6,'Architecture')

#Edita el valor de GPA en s1
s1.GPA=3.5
#Añade una varuable de instancia llamada num_courses
setattr(s1,"num_courses",5)
setattr(s2,"num_courses",6)
#Muestra los valores de las variables
print(s1.display(),s1.num_courses)
print(s2.display(),s2.num_courses)