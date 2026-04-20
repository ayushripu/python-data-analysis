company = {
    "Employee" : ["Ram", 'Shyam', "Mohan"],
    "sallary" : [50000, 8526, 9546],
    "client" : {
        "Name" : ["Ayush", "Piyush", "Mohan"],
        "city" : ["Delhi", "Mumbai", "Pune"]
    }
}

print(list(company.keys()))
print(list(company["client"].keys()))