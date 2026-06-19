#!/usr/bin/env python

import pandas as pd
import yaml
import os

from pylindas.pycube import Cube

BASEDIR = os.path.dirname(__file__)
DATAFILE = os.path.join(BASEDIR, "data.csv")
CONFIGFILE = os.path.join(BASEDIR, "description.yml")
OUTFILE = os.path.join(BASEDIR, "cube.ttl")

mock_df = pd.read_csv(DATAFILE)

with open(CONFIGFILE) as file:
    config = yaml.safe_load(file)

cube = Cube(dataframe=mock_df, cube_yaml=config, environment="TEST", local=True)
cube.prepare_data()
cube.write_cube(opendataswiss=True)
cube.write_observations()
cube.write_shape()
cube.serialize(OUTFILE)

print(cube)
