import rebrick
import json
import util

# init rebrick module for general reading
rebrick.init("d34210807df61e1ad97727779d78cad2")

# get set info
response = rebrick.lego.get_set(6608)
# print(json.loads(response.read()))
util.print_json(json.loads(response.read()))
