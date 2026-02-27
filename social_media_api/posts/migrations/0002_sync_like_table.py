from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            sql=(
                "CREATE TABLE IF NOT EXISTS posts_like ("
                "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
                "created_at datetime NOT NULL, "
                "post_id bigint NOT NULL REFERENCES posts_post(id) DEFERRABLE INITIALLY DEFERRED, "
                "user_id bigint NOT NULL REFERENCES accounts_user(id) DEFERRABLE INITIALLY DEFERRED"
                ");"
                "CREATE UNIQUE INDEX IF NOT EXISTS posts_like_post_id_user_id_uniq ON posts_like(post_id, user_id);"
                "CREATE INDEX IF NOT EXISTS posts_like_post_id_idx ON posts_like(post_id);"
                "CREATE INDEX IF NOT EXISTS posts_like_user_id_idx ON posts_like(user_id);"
            ),
            reverse_sql="DROP TABLE IF EXISTS posts_like;",
        )
    ]
