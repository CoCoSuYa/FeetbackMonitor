import mysql.connector


def save_to_database(username, password):
    # 连接到远程数据库
    connection = mysql.connector.connect(
        host="43.139.138.117",
        user="admin",
        password="admin",
        database="feetback_record_db"
    )

    cursor = connection.cursor()

    # 插入数据。此处是示例，生产环境不应明文存储密码
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    # 从命令行获取用户名和密码
    username = input("Enter username: ")
    password = input("Enter password: ")
    print(username, password)
    save_to_database(username, password)
    print("User saved to database.")
