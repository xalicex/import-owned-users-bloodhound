# -*- coding: utf-8 -*-

from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://127.0.0.1:7687", auth=("neo4j", "PutYourPasswordHere"))
mydomain = "mydomain.local"
print("Let's import\n")
with driver.session() as session:
    filepath = './owned.txt'
    with open(filepath) as fp:
        account = fp.readline()
        while account:
            the_query = "MATCH (n) WHERE (n.name = \"{}@{}\") SET n.owned = true".format(account.strip().upper(), mydomain.upper())
            print(the_query)
            graph = session.run(the_query)
            account = fp.readline()
print("Import finished\n")
driver.close()
