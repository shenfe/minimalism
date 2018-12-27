# coding: utf8

import json

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple


def run(fn, host='127.0.0.1', port=4000, debug=False, autoreload=False, batch=False):

    @Request.application
    def application(request):

        req_data = json.loads(request.data)

        if debug:
            print 'request data:', req_data

        if (not batch) and isinstance(req_data, list):
            res_data = [fn(item) for item in req_data]
        else:
            res_data = fn(req_data)

        if debug:
            print 'response data:', res_data

        return Response(json.dumps(res_data), status=200, mimetype='application/json')

    return run_simple(host, port, application, use_debugger=debug, use_reloader=autoreload)


if __name__ == '__main__':

    def process(req_data):
        return {'code': 0, 'message': 'success'}

    run(process)
