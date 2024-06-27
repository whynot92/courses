import sqlite3

class DB:
    def __init__(self):
        db_name = "olxGroups.db"
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY,
            id_group TEXT UNIQUE,
            name_group TEXT DEFAULT "",
            link TEXT,
            key_words TEXT DEFAULT "",
            banned_key_words TEXT DEFAULT "",
            status_active boolean DEFAULT 1
        )''')
        self.conn.commit()

    def add_group_and_link(self, id_group, link):
        try:
            self.cursor.execute('''INSERT INTO groups (
                id_group,
                link
            ) VALUES (
                :id_group,
                :link
            )''', {'id_group': id_group, 'link': link})
            self.conn.commit()
            return True
        except Exception as e:
            return e

    def delete_group(self, id_group):
        self.cursor.execute('''DELETE FROM groups WHERE id_group = :id_group''', {'id_group': id_group})
        self.conn.commit()

    def change_group_name(self, id_group, name_group):
        self.cursor.execute('''UPDATE groups SET name_group = :name_group WHERE id_group = :id_group''', {'name_group': name_group, 'id_group': id_group})
        self.conn.commit()
    
    def change_group_link(self, id_group, link):
        self.cursor.execute('''UPDATE groups SET link = :link WHERE id_group = :id_group''', {'link': link, 'id_group': id_group})
        self.conn.commit()

    def change_group_status(self, id_group, status):
        self.cursor.execute('''UPDATE groups SET status_active = :status_active WHERE id_group = :id_group''', {'status_active': status, 'id_group': id_group})
        self.conn.commit()

    def get_groups(self):
        self.cursor.execute('''SELECT id_group, name_group, link, status_active FROM groups''')
        rows = self.cursor.fetchall()
        
        groups = []
        for row in rows:
            group = {
                "id_group": row[0],
                "name_group": row[1],
                "link": row[2],
                "status_active": row[3]
            }
            groups.append(group)
    
        return groups
    
    def get_group(self, id_group):
        self.cursor.execute('''SELECT * FROM groups WHERE id_group = :id_group''', {'id_group': id_group})
        row = self.cursor.fetchone()
        
        if row:
            group = {}
            for idx, col in enumerate(self.cursor.description):
                group[col[0]] = row[idx]
            return group
        else:
            return None

    def add_group_key_words(self, id_group, key_words):
        '''
        key_word = "one_key two_key three_key"
        '''
        self.cursor.execute("SELECT key_words FROM groups WHERE id_group = ?", (id_group,))
        old_key_word = self.cursor.fetchone()[0]
        for key_word in key_words.split():
            if key_word not in old_key_word:
                old_key_word += " "+key_word
        self.cursor.execute('''UPDATE groups SET key_words = ? WHERE id_group = ?''', (old_key_word,id_group))
        self.conn.commit()

    def remove_group_key_words(self, id_group, del_key_words):
        '''
        key_word = "one_key two_key three_key"
        '''
        self.cursor.execute("SELECT key_words FROM groups WHERE id_group = ?", (id_group,))
        key_words = self.cursor.fetchone()[0].split()
        for key_word in del_key_words.split():
            if key_word in key_words:
                key_words.remove(key_word)
        self.cursor.execute('''UPDATE groups SET key_words = ? WHERE id_group = ?''', (" ".join(key_words),id_group))
        self.conn.commit()

    def add_group_banned_key_words(self, id_group, banned_key_words):
        '''
        key_word = "one_key two_key three_key"
        '''
        self.cursor.execute("SELECT banned_key_words FROM groups WHERE id_group = ?", (id_group,))
        old_banned_key_word = self.cursor.fetchone()[0]
        for key_word in banned_key_words.split():
            if key_word not in old_banned_key_word:
                old_banned_key_word += " "+key_word
        self.cursor.execute('''UPDATE groups SET banned_key_words = ? WHERE id_group = ?''', (old_banned_key_word,id_group))
        self.conn.commit()

    def remove_group_banned_key_words(self, id_group, del_banned_key_words):
        '''
        key_word = "one_key two_key three_key"
        '''
        self.cursor.execute("SELECT banned_key_words FROM groups WHERE id_group = ?", (id_group,))
        banned_key_words = self.cursor.fetchone()[0].split()
        for key_word in del_banned_key_words.split():
            if key_word in banned_key_words:
                banned_key_words.remove(key_word)
        self.cursor.execute('''UPDATE groups SET banned_key_words = ? WHERE id_group = ?''', (" ".join(banned_key_words),id_group))
        self.conn.commit()

    def get_key_words(self, id_group):
        self.cursor.execute('''SELECT key_words FROM groups WHERE id_group = :id_group''', {'id_group': id_group})
        row = self.cursor.fetchone()
        
        if row:
            return row[0]
        else:
            return None
    
    def get_banned_key_words(self, id_group):
        self.cursor.execute('''SELECT banned_key_words FROM groups WHERE id_group = :id_group''', {'id_group': id_group})
        row = self.cursor.fetchone()
        
        if row:
            return row[0]
        else:
            return None
    
    def close_connection(self):
        self.conn.close()
