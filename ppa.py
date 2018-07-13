from app import app
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--debug', dest='debug', action='store_true')

app.run(debug=parser.parse_args().debug)