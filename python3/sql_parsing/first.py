from mo_sql_parsing import parse
import sqlglot
import pprint
import json

insert_queries = {
    "simple": [
        "INSERT INTO users (id, name, email) VALUES (1, 'Alice', 'alice@example.com');",
        (
            "INSERT INTO users (id, name, email) VALUES "
            "(2, 'Bob', 'bob@example.com'), "
            "(3, 'Charlie', 'charlie@example.com');"
        )
    ],
    "medium": [
        (
            "INSERT INTO archived_users (id, name, email) "
            "SELECT id, name, email FROM users WHERE last_login < '2024-01-01';"
        ),
        (
            "INSERT INTO products (product_id, name, price, stock, description) "
            "VALUES (101, 'Pen', 1.50, DEFAULT, NULL);"
        )
    ],
    "complex": [
        # (
        #     "INSERT INTO users (id, name, email) "
        #     "VALUES (1, 'Alice Updated', 'alice_new@example.com') "
        #     "ON CONFLICT (id) DO UPDATE SET "
        #     "name = EXCLUDED.name, email = EXCLUDED.email;"
        # ),
        """WITH new_customer AS (INSERT INTO customers (name) VALUES ('Alice') RETURNING id) INSERT INTO orders (customer_id, product_id) SELECT id, 42 FROM new_customer;"""
          

    ]
}

file = open("sql_parsed.txt", 'w')
for x, y in insert_queries.items():

    
    for sql in y:

        expression = sqlglot.parse_one(sql, read='postgres')
        ast_like = expression.dump()

        file.write(json.dumps(ast_like, indent=1))
        file.write('\n\n')
        print("*"*50)
        pprint.pprint(ast_like)
        print("*"*50)


        # parsed = parse(sql)
        # print(parsed)
file.close()