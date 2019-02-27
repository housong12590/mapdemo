# from flask import Flask, jsonify, render_template, request
# import json
# import requests
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return render_template('map.html')
#
#
# @app.route('/insight/map/points')
# def insight_map_points():
#     ret = requests.get('http://gongfudou.com/insight/map/points')
#     return jsonify(json.loads(ret.text, encoding='utf8'))
#
#
# # http://gongfudou.com/insight/map/flash
# @app.route('/insight/map/flash')
# def insight_map_flash():
#     ret = requests.get('http://gongfudou.com/insight/map/flash')
#     return jsonify(json.loads(ret.text, encoding='utf8'))
#
#
# # http://gongfudou.com/insight/map/total
# @app.route('/insight/map/total')
# def insight_map_total():
#     ret = requests.get('http://gongfudou.com/insight/map/total')
#     return jsonify(json.loads(ret.text, encoding='utf8'))
#
#
# # http://gongfudou.com/insight/map/info
# @app.route('/insight/map/info')
# def insight_map_info():
#     ret = requests.get('http://gongfudou.com/insight/map/info')
#     return jsonify(json.loads(ret.text, encoding='utf8'))
#
#
# # http://gongfudou.com/insight/map/designs?count=5&last=' + lastDesignID
# @app.route('/insight/map/designs')
# def insight_map_designs():
#     last = request.args.get('last')
#     ret = requests.get('http://gongfudou.com/insight/map/designs?count=5&last=' + last)
#     print(ret.text)
#     return jsonify(json.loads(ret.text, encoding='utf8'))
#
#
# if __name__ == '__main__':
#     app.debug = True
#     app.run(host='0.0.0.0')
