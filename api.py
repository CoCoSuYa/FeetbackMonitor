import mysql.connector

connection = mysql.connector.connect(
    host="43.139.138.117",
    user="admin",
    password="admin",
    database="feetback_record_db"
)
cursor = connection.cursor()


def check_user(username, password):
    """
        检查用户名和用户密码是否匹配
    :param username:
    :param password:
    """
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchall()

    if not result:  # 如果结果列表为空
        return False
    else:
        return True


print(check_user("admin", "admin"))
