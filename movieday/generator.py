import click
import yaml


@click.command()
@click.argument('year', type=int, nargs=1)
def generate(year):

    data = {}

    with open('./data/%d_movies.yml' % year, 'r') as movies_file:
        data['movies'] = yaml.load(movies_file)

    with open('./data/%d_prefs.yml' % year, 'r') as prefs_file:
        data['prefs'] = yaml.load(prefs_file)

    print(data)
