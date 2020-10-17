import os
import Query
import connections

def main():
    yeet = Query.Query("Ryan", "Rosiak", 500, 3025851206, 24, 35, 10000, 5000, 700, 20)

    print(yeet)

    yeet.create_tables()
    yeet.insert_all()
    rows = yeet.select_all(1)
    print(rows)

if __name__ == "__main__":
    main()
