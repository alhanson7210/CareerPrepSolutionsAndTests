from flask import Flask

app = Flask(__name__)

known_hsv_map = None

def setup():
  global known_hsv_map 
  known_hsv_map = dict()
  known_hsv_map["000000"] = 'Black'
  known_hsv_map["FFFFFF"] = 'White'
  known_hsv_map["FFC0CB"] = 'Pink'
  known_hsv_map["FFA500"] = 'Orange'
  known_hsv_map["FFFF00"] = 'Yellow'
  known_hsv_map["FF0000"] = 'Red'
  known_hsv_map["800080"] = 'Purple'
  known_hsv_map["A52A2A"] = 'Brown'
  known_hsv_map["0000FF"] = 'Blue'
  known_hsv_map["808080"] = 'Grey'
  known_hsv_map["008000"] = 'Green'

def color(color):
  if color in known_hsv_map:
    return known_hsv_map[color]
  else:
    keys = list(known_hsv_map.keys())
    hx = int(color, 16)
    known_map = list(
      map(lambda x: 
        abs(int(x, 16) - hx)
      ,  keys))
    mn = 0
    for idx, value in enumerate(known_map):
      if value < known_map[mn]:
        mn = idx
    return known_hsv_map[keys[mn]]

def home():
  return "CareerPrepSolutionsAndTests: Programming problems and unit testing for these given problems in python[mainly] (test \'/color/hex_value\' to get back the closest color)"

app.add_url_rule('/', '/', home)
app.add_url_rule('/color/<color>', 'color', color)

setup()

app.run(host='0.0.0.0', port=8080)