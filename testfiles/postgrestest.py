import os
import Query
import connections

def main():
    yeet = Query.Query("Ryan", "Rosiak", 9000, 9000, 500, 1, 3025551206, 105, 120, 15, 85, 156, 900, 800,
                       56, 500, 550, 235, 110, 300)

    print(yeet)

    yeet.create_tables()
    yeet.insert_all()
    rows = yeet.select_all(1)
    print(rows)

if __name__ == "__main__":
    main()
