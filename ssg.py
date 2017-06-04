import sys
import json

def tprint(n, msg):
    if msg != "":
        print "    "*n + msg

def analyze(o, level, last_key, array = False):
    if not array:
        tprint(level, last_key + ":")
    level += 1
    if type(o) == dict:
        tprint(level, "type: object")
        if last_key != "schema":
            tprint(level, "description: " + last_key)
        tprint(level, "properties:")
        level += 1
        for key, value in o.items():
            analyze(value, level, key)

    if type(o) == list:
        tprint(level, "type: array")
        tprint(level, "description: " + last_key)
        tprint(level, "items: ")
        analyze(o[0], level, last_key + " item", True)

    if type(o) == int:
        tprint(level, "type: integer")
        tprint(level, "description: " + last_key)

    if type(o) == str:
        tprint(level, "type: string")
        tprint(level, "description: " + last_key)

    if type(o) == float:
        tprint(level, "type: float")
        tprint(level, "description: " + last_key)

obj = json.load(sys.stdin)

analyze(obj, 0, "schema")
