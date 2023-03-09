import os



Docker_installation = []
Data_modeling =["What is a Database?",
"Introduction to the Relational Model:​ Entities",
"Exercise: Diagramming",
"Exercise: Relationships",
"Normalization"]

Integrity_Constraints = ["Integrity Constraints & Nullability","Uniqueness",
"Exercise: Relationship Participation",
"Exercise: Relationship Types"]
Tables = ["Database Tables",
"Database Table References"]

main_dir = [Docker_installation, Data_modeling,Integrity_Constraints, Tables]
root_dir = ["week1"]
main_dir_name =['docker_installation','data_modeling','intergrity_contraints','tables']

def creat_floders():
    #creat directory 
    for i in range(0, len(main_dir)):
        for j in range(0, len(main_dir[i])):
            dirname = str(root_dir) + '/' +  str(main_dir_name[i]) +'/' + str(main_dir[i][j])

            try:
                os.makedirs(dirname)
                print("Directory ", dirname, "created")
            except FileExistsError:
                print("Directory ", dirname , "already exists")
            if not os.path.exists(dirname):
                os.makedirs(dirname)
                print("Dirctory ", dirname, "created")
            else:
                print("Directory ", dirname , "already exists")
    

    