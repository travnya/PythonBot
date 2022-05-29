import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute('INSERT INTO `users` (`user_id`) VALUES (?)', (user_id,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def set_name(self, user_id, user_name):
        with self.connection:
            return self.cursor.execute('UPDATE `users` SET `user_name` = ? WHERE `user_id` = ?', (user_name, user_id,))

    def set_surname(self, user_id, user_surname):
        with self.connection:
            return self.cursor.execute('UPDATE `users` SET `user_surname` = ? WHERE `user_id` = ?', (user_surname, user_id,))

    def set_patronymic(self, user_id, user_patronymic):
        with self.connection:
            return self.cursor.execute('UPDATE `users` SET `user_patronymic` = ? WHERE `user_id` = ?', (user_patronymic, user_id,))

    def set_phone_number(self, user_id, user_phone_number):
        with self.connection:
            return self.cursor.execute('UPDATE `users` SET `user_phone_number` = ? WHERE `user_id` = ?', (user_phone_number, user_id,))


    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT `user_signup` FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def get_phone_number(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT `user_phone_number` FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            for row in result:
                phonenumber = str(row[0])
            return phonenumber

    def set_signup(self, user_id, user_signup):
        with self.connection:
            return self.cursor.execute('UPDATE `users` SET `user_signup` = ? WHERE `user_id` = ?', (user_signup, user_id,))

    def get_name(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT `user_name` FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            for row in result:
                name = str(row[0])
            return name

    def get_surname(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT `user_surname` FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            for row in result:
                surname = str(row[0])
            return surname