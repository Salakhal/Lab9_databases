import click
from db import get_conn

@click.group()
def cli():
    pass

@cli.command()
@click.argument("titre")
def add_course(titre):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO COURS (titre, credits) VALUES (%s, %s)",
        (titre, 3)
    )
    conn.commit()
    click.echo(f"Cours '{titre}' ajouté.")
    conn.close()

@cli.command()
def list_courses():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, titre, credits FROM COURS")
    for row in cur.fetchall():
        click.echo(row)
    conn.close()

@cli.command()
@click.argument("id")
def delete_course(id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM COURS WHERE id=%s", (id,))
    conn.commit()
    click.echo("Cours supprimé.")
    conn.close()

if __name__ == "__main__":
    cli()

