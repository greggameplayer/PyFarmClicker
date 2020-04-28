import os
import sys
import pickle


def find_data_file(filename):
    """
    utilisé pour trouver le chemin du dossier resources
    :param filename:
    :return:
    """
    if getattr(sys, "frozen", False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
        return os.path.join(datadir, "resources/" + filename)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)
        return os.path.join(datadir, "../resources/" + filename)


def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def read_object(filename):
    with open(filename, 'rb') as input:  # Overwrites any existing file.
        return pickle.load(input)


MainObj = {
    "items": None,
    "saison": None,
    "pactole": None
}
