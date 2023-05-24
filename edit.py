import sqlite3 as sq
import bcrypt
from registration import checkPassword, hash_password

def changeInfo(username, password, new_password = None, birthday = None, gender = None, email = None, phone = None):
    if checkPassword(username, password):
        conn = sq.connect('database/project.db')
        cursor = conn.cursor()
        hashed = hash_password(new_password)
        if new_password not None:
            cursor.execute("UPDATE USERINFO SET password = ? WHERE username = ?",(hashed, username))
            # ?안에는 각각 hashed와 username이 들어간다
        if phone not None:
            cursor.execute("UPDATE USERINFO SET phone = ? WHERE username = ?",(phone, username))
        if gender not None:
            cursor.execute("UPDATE USERINFO SET gender = ? WHERE username = ?",(gender, username))
        if birthday not None:
            cursor.execute("UPDATE USERINFO SET birthday = ? WHERE username = ?",(birthday, username))
        if email not None:
            cursor.execute("UPDATE USERINFO SET email = ? WHERE username = ?",(email, username))
        conn.commit()
        conn.close()
        return True
    else:
        return False

changePassword("theman", "theman0000", "theman0001")
