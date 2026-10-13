
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Servidor(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/api":
            dados = {
                "mensagem": "Ola! Esta mensagem veio do Container 2!"
            }

            resposta = json.dumps(dados).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(resposta)
        else:
            self.send_error(404)


print("Backend iniciado na porta 5000", flush=True)

HTTPServer(("0.0.0.0", 5000), Servidor).serve_forever()
