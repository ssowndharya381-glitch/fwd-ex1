from http.server import HTTPServer, BaseHTTPRequestHandler
content ="""
<!DOCTYPE html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TCP/IP Protocol Suite</title>
</head>
<body>
    <h1>TCP/IP Protocol Suite Protocols</h1>
    <ul>
        <li>*Application Layer:*
            <ul>
                <li>HTTP (Hypertext Transfer Protocol)</li>
                <li>FTP (File Transfer Protocol)</li>
                <li>SMTP (Simple Mail Transfer Protocol)</li>
                <li>DNS (Domain Name System)</li>
                <li>SNMP (Simple Network Management Protocol)</li>
            </ul>
        </li>
        <li>*Transport Layer:*
            <ul>
                <li>TCP (Transmission Control Protocol)</li>
                <li>UDP (User Datagram Protocol)</li>
            </ul>
        </li>
        <li>*Internet Layer:*
            <ul>
                <li>IP (Internet Protocol)</li>
                <li>ICMP (Internet Control Message Protocol)</li>
                <li>ARP (Address Resolution Protocol)</li>
            </ul>
        </li>
        <li>*Network Access Layer:*
            <ul>
                <li>Ethernet</li>
                <li>Wi-Fi (IEEE 802.11)</li>
            </ul>
        </li>
    </ul>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()