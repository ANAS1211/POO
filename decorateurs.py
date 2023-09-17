def do_that_task():
    print("Executing that task")
    p = do_that_task
    p()
def vi_editor():
    print("Basic tool, all is in my head!")
    
def pycham_ide():
    print("Advanced tools, focusing on business code")

def do_coding(tool):
    print("do coding with...")
    tool() #ici on mentionne que l'argument "tool" 
    #doit être sous forme de fonction
#On crée une fonction qui a comme argument une autre fonction
    
print(do_coding(vi_editor))
print(do_coding(pycham_ide))

#Rappel à propos des fonctions (suite)
#Une fonction peut retourner une fonction 
#(qui en plus pourra être crée à la volée)

def get_inner_function():
    def inner_function():
        print("Executing an inner function")
        return
    return (inner_function)
# invoke get_inner_function, result will be accessible via p
p= get_inner_function()
#invoke p function 
print(p())

#décorateurs vue coté utilisateur:

# def do_decorate_function(f):
#     def g():
#         print("Start wrapping function")
#         f()
#         print("End wrapping function")
#         return #retour vide de la fonction g
#     return g
# d= do_decorate_function(do_that_task)
# d()
# print(d())

#décorateurs vue coté développeur:
#version explicite
def do_compute(p1,p2,p3):
    print("Running a tricky software with parameters {}, {}, {}".format(p1,p2,p3))
    return
#decoration de la fonction do_compute:
 #créer la fonction de décoration avec comme argument la fonction à décorer
 #et ses arguments 
def do_decorate(f,*args):
    def g(*args):
        print("Prepare env. to run new "
"version with parameters {}".format(args))
        f(*args)
        print("restore environnement after run")
        return
    return g

@do_decorate
def do_compute(p1, p2, p3):
    print("Running a smarter version of software ")
    return
print(do_compute(1,2,3))

    

        

