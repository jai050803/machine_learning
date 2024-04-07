#import necessary libraries
import numpy as np
import pandas as pd
from flask import flask, request, jsonify, render_template
import pickle

app = flask(__name__)