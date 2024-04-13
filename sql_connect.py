import pymysql
from config_sql import host, user, password, db_name


try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:
        # cursor = connection.cursor()

        # create table
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT," \
        #                          " game varchar(32)," \
        #                          " title varchar(32), PRIMARY KEY (id));"
        #     cursor.execute(create_table_query)
        #     print("Table created successfully")

        # insert data
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `matchinfo` (game, title) VALUES ('NBA', 'Яблоки VS Апельсины');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `matchinfo` (game, title) VALUES ('FIFA', 'Бананы VS Чебуреки');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `matchinfo` (game, title) VALUES ('CS', 'Курицы VS Кошки');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `matchinfo` (game, title) VALUES ('Dota', 'Дети VS Тараканы');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Victor', '123456', 'victor@gmail.com');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '112233', 'olegan@mail.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', 'kjlsdhfjsd', 'ole2gan@mail.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '889922', 'olegan3@mail.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # update data
        # with connection.cursor() as cursor:
        #     update_query = "UPDATE `users` SET password = 'xxxXXX' WHERE name = 'Oleg';"
        #     cursor.execute(update_query)
        #     connection.commit()

        # delete data
        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM `users` WHERE id = 5;"
        #     cursor.execute(delete_query)
        #     connection.commit()

        # drop table
        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE `users`;"
        #     cursor.execute(drop_table_query)

        # select all data from table
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `matchinfo`"
            cursor.execute(select_all_rows)
            # cursor.execute("SELECT * FROM `users`")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            # print("#" * 20)

        # rename table
        # with connection.cursor() as cursor:
        #     alter_table_query = "ALTER TABLE users RENAME TO matchinfo"
        #     cursor.execute(alter_table_query)

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)