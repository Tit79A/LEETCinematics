from flask import Flask

from scipy import interpolate
import numpy as np
import json
import re

app = Flask(__name__)

@app.route('/api/', defaults={'path': ''}, methods=['GET'])
@app.route('/api/<path:path>', methods=['GET'])
def apiGET(path):
    parsedURL = path.split("/")
    if len(parsedURL) >= 1:
        if parsedURL[0] == "lcin":
            if len(parsedURL) >= 3:
                if parsedURL[1].isdigit():
                    time = int(parsedURL[1])
                    if time >= 2 and time <= 30:
                        data = parsedURL[2]
                        if re.match("^((\,?-?\d+){5};?)*$", data):
                            try:
                                x, y, z, yaw, pitch = ([] for i in range(5))
            
                                for pos in data.split(";"):
                                    x[len(x):] ,y[len(y):], z[len(z):], yaw[len(yaw):], pitch[len(pitch):] = map(list, zip(tuple(map(int, pos.split(",")))))
            
                                yaw = np.rad2deg(np.unwrap(np.deg2rad(yaw)))
            
                                tck, u = interpolate.splprep([x, y, z], s = 2)
                                x, y, z = interpolate.splev(np.linspace(0, 1, time * 20), tck)
            
                                tck, u = interpolate.splprep([yaw, pitch], s = 2)
                                yaw, pitch = interpolate.splev(np.linspace(0, 1, time * 20), tck)
            
                                result = np.around(np.array((x, y, z, yaw, pitch)).T, decimals = 2).tolist()
                                
                                return str(json.dumps(result))
                            except:
                                return "Unable to generate the path, please try again."
                        else:
                            return "Error : Invalid data format."
                    else:
                        return "Error : Travel time must be between 2 and 30 seconds."
                else:
                    return "Error : Invalid specified time."
            else:
                return "Error : Missing argument(s)."
        else:
            return "Error : Invalid argument(s)."
    else:
        return "Error : Missing argument(s)."