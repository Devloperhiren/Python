# Password : Hello World

# Limitations...

# it only support 9 queries
# data loss if execution closed
# no constraints are used

# features

# uses full MySQL style to perform tasks
# Shows table properly with keys and their values
# Shows error by faulty queries like mysql style
"""
1. Database Commands...

    i.   Show Databases;
    ii.  Create Database [database_name];
    iii. Use [Database_Name];
    iv. drop [database_name];

2. Table Commands...

    i. Show tables;
    ii. Create table [table_name] ( [key] [datatype],...);
    iii. drop table [table_name];

3. DML Commands...

    i.  Select * or [keys] from [table_name]; 
    ii. insert into [table_name] values ([values]);
    
    """
import time

start = 0
end = 0
use = ""

def Show_Databases(Database):
    list_of_databases = list(Database)

    print("+--------------------+")
    print("|     Databases      |")
    print("+--------------------+")

    for databases in list_of_databases:
        print(f"|{databases:<10}{"|":>11}")

    print("+--------------------+")
    end = time.time()
    print(f"{len(list_of_databases)} rows in set ({end-start:.1f} sec)")

def Create_Database(Database,name):

    Database[name] = {}
    end = time.time()
    print(f"Query OK, 1 row affected ({end-start:.1f} sec)")


def Drop_Database(Database,name):
    end = time.time()
    print(name)
    list_of_databases = list(Database)
    if(name not in list_of_databases):
        print(f"ERROR 1008 (HY000): Can't drop database {name}; database doesn't exist")
    else:
        del Database[name]
        print(f"Query OK, 1 rows affected ({end-start:.1f} sec)")
    
def Use_database(use):
    list_of_databases = list(Database)

    if(use in list_of_databases):
        print("Database changed")
    else:
        print(f"ERROR 1049 (42000): Unknown database '{use}'")


def show_tables(Database,use):

    if(use == ""):
        print("ERROR 1046 (3D000): No database selected")
    else:
        list_of_tables = list(Database[use])

        print("+-----------------------------+")
        print(f"| Tables in {use:<10}        |")
        print("+-----------------------------+")

        for tables in list_of_tables:
            print(f"|{tables:<25}    {"|"}")
        print("+-----------------------------+")
        end = time.time()
        print(f"{len(list_of_tables)} rows in set ({end-start:.1f} sec)")

def select_default(Database,use,name):
    if(use == ""):
        print("ERROR 1046 (3D000): No database selected")
    else:
        list_of_details = list(Database[use][name])

        

        print("+-------------------+"*len(list_of_details))
        for keys in list_of_details:
            print(f"|{keys:<18} {"|"}",end="")
        print()
        print("+-------------------+"*len(list_of_details))
        list_of_deeper = []
        for index,keys in enumerate(list_of_details):
            list_of_deeper.append(list(Database[use][name][keys]))
        for index in range(len(list(Database[use][name][keys]))):
                for i in range(len(Database[use][name])):
                    print(f"|{list_of_deeper[i][index]:<18} {"|"}",end="")
                print()

        print("+-------------------+"*len(list_of_details))
        end = time.time()
        print(f"{len(list(Database[use][name][keys]))} rows in set ({end-start:.1f} sec)")

def drop_table(Database,use,name):
    if(use == ""):
        print("ERROR 1046 (3D000): No database selected")
    else:
        del Database[use][name]
        end = time.time()
        print(f"Query OK, 0 rows affected ({end-start:.1f} sec)")


def create_table(Database,use,name,keys):
    if(use == ""):
        print("ERROR 1046 (3D000): No database selected")
    else:
        Database[use][name] = {}

        for key in keys:
            Database[use][name][key] = set()
        end = time.time()
        print(f"Query OK, 0 rows affected ({end-start:.1f} sec)")

def insert_into(Database,use,name,values):
    if(use == ""):
        print("ERROR 1046 (3D000): No database selected")
    else:
        keys = list(Database[use][name])

        for index,key in enumerate(keys):
            Database[use][name][key].add(values[index])
        end = time.time()
        print(f"Query OK, 1 row affected ({end-start:.1f} sec)")


Database = {

"Default" : {

"Availabe_Constraints" : 
{
    "Availability" : {"Default","None","Show"},
    "Availability1" : {"Default1","None1","Show1"}
        
 },

"Usage" :{ 
    "What can It do ?" : {"Simple Database related Commands",}
}

},


"Default2" : {

"Availabe_Constraints2" : 
{
    "Availability2" : {"Default2",}
 },

"Usage" :{ 
    "What can It do ?2" : {"Simple Database related Commands2",}
}

}


}

password = input("Enter Password: ")

while(password != "Hello World"):

    if(password != "Hello World"):
        print("ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)\n")
        password = input("Enter Password: ")



while(1):

    query = input("\nmysql> ").split(" ")

    if(query[0].lower() == "show" and query[1].lower() ==  "databases;" and len(query)==2):
        start = time.time()
        Show_Databases(Database)


    elif(query[0].lower() == "create" and query[1].lower() == "database" and query[2].endswith(";") and len(query)==3):
        start = time.time()
        name = str(query[2].replace(";",""))
        Create_Database(Database,name)


    elif(query[0].lower() == "drop" and query[1].lower() == "database" and query[2].endswith(";") and len(query)==3):
        start = time.time()
        name = str(query[2].replace(";",""))
        Drop_Database(Database,name)               

    elif (query[0].lower() == "use" and query[1].endswith(";") and len(query)==2):
        use = str(query[1].replace(";",""))
        Use_database(use)

    elif(query[0].lower() == "show" and query[1].lower() == "tables;" and len(query)==2):
        start = time.time()
        show_tables(Database,use)

    elif(query[0].lower() == "drop" and query[1].lower()=="table" and query[2].endswith(";") and len(query)==3):
        start=time.time()
        name = str(query[2].replace(";",""))
        drop_table(Database,use,name)

    elif(query[0].lower() == "select" and query[1].lower() == "*" and query[2].lower()=="from" and query[3].endswith(";") and len(query) == 4):
        start = time.time()
        name = str(query[3].replace(";",""))
        select_default(Database,use,name)

    elif(query[0].lower()== "create" and query[1].lower() == "table" and query[len(query)-1] == ");"):
        start = time.time()
        print(query[3:len(query)-1])

        name = str(query[2].replace("(",""))
        keys = []
        for i in range(3,len(query)-1,2):
            keys.append(query[i])

        create_table(Database,use,name,keys)
                
    elif(query[0].lower()== "insert" and query[1]=="into" and query[3]== "values(" and query[len(query)-1] == ");"):
        start = time.time()
        name = str(query[2])
        values = []
        for v in range(4,len(query)-1):
            values.append(query[v].replace(",",""))

        insert_into(Database,use,name,values)

    else:
        print("ERROR 1064 (42000): You have an error in your SQL syntax\n")