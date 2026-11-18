from http.server import HTTPServer, SimpleHTTPRequestHandler


def add(a, b):
    return a + b


if __name__ == "__main__":
    print("**************************************************", flush=True)
    print("                SERVICERUNNING                    ", flush=True)
    print("**************************************************", flush=True)
    print("Starting server on port 8000...", flush=True)
    server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
    
