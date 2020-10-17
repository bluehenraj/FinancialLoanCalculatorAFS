import os
import Query
import connections

def main():
    yeet = Query.Query("Ryan", "Rosiak", 250, 500, 20, 1000, 75000)

    print(yeet)

    yeet.create_tables()
    yeet.insert_all()
    rows = yeet.select_all(1)
    print(rows)

if __name__ == "__main__":
    main()
