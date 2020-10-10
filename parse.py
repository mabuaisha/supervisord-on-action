import argparse
import socket
import xmlrpc.client as xmlrpclib
import http.client as httplib


class UnixSocketHTTPConnection(httplib.HTTPConnection):
    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(self.host)


class UnixSocketTransport(xmlrpclib.Transport, object):
    def __init__(self, path):
        super(UnixSocketTransport, self).__init__()
        self._path = path

    def make_connection(self, host):
        return UnixSocketHTTPConnection(self._path)


def _control_process(name, action):
    server = xmlrpclib.Server(
        'http://',
        transport=UnixSocketTransport("/tmp/supervisor.sock"))
    action_obj = getattr(
        server.supervisor,
        '{action}Process'.format(action=action)
    )
    result = action_obj(name)
    if result:
        print('{action} {process} executed successfully'
              ''.format(action=action, process=name))
        return
    raise SystemError('Something went wrong')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Simple arg parser for supervisor command'
    )
    parser.add_argument(
        '-a',
        action='store',
        dest='action',
        help='Store action value',
        required=True
    )
    parser.add_argument(
        '-p',
        action='store',
        dest='process_name',
        help='Store process name',
        required=True
    )
    results = parser.parse_args()
    _control_process(results.process_name, results.action)
