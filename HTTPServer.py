from urllib.parse import urlparse
from http.server import SimpleHTTPRequestHandler, HTTPServer

from scipy import interpolate
import numpy as np
import json
import re


class LCRequestHandler(SimpleHTTPRequestHandler):
    
    def do_GET(self):
        parsedURL = (urlparse(self.path).path + ";" + urlparse(self.path).params)[1:].split("/")
        
        if parsedURL[0] == "api":
            if len(parsedURL) >= 2:
                if parsedURL[1] == "lcin":
                    if len(parsedURL) >= 4:
                        if parsedURL[2].isdigit():
                            time = int(parsedURL[2])
                            if time >= 2 and time <= 30:
                                data = parsedURL[3]
                                if re.match("^(-?\d+\,){4}-?\d+(;(-?\d+\,){4}-?\d+)*$", data):
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
                                        
                                        self.respond(bytes(str(json.dumps(result)), "utf-8"))
                                    except:
                                        self.respond(bytes("Unable to generate the path, please try again.", "utf-8"))
                                else:
                                    self.respond(bytes("Error : Invalid data format.", "utf-8"))
                            else:
                                self.respond(bytes("Error : Travel time must be between 2 and 30 seconds.", "utf-8"))
                        else:
                            self.respond(bytes("Error : Invalid specified time.", "utf-8"))
                    else:
                        self.respond(bytes("Error : Missing argument(s).", "utf-8"))
                else:
                    self.respond(bytes("Error : Invalid argument(s).", "utf-8"))
            else:
                self.respond(bytes("Error : Missing argument(s).", "utf-8"))
        else:
            super().do_GET()
            
    
    def respond(self, response):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(response))
        self.end_headers()
        self.wfile.write(response) 


httpd = HTTPServer(("127.0.0.1", 80), LCRequestHandler)
print("HTTP server started !")
httpd.serve_forever()