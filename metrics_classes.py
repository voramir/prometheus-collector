from prometheus_client import start_http_server, REGISTRY, Metric
from requests.auth import HTTPDigestAuth
from secrets import zfsuser, zfspass

import json
import requests
import time

def collect(link):
    return json.loads(requests.get(link, verify=False, auth=(zfsuser, zfspass)).content.decode('UTF-8'))


class SingleValueGauge(object):

    def __init__(self, jsondata, metric_name, hostname):
        self.jsondata = jsondata
        self.metric_name = metric_name
        self.hostname = "_".join(hostname.split('.'))

    def collect(self):
        jsondata = collect(self.jsondata)
        metric = Metric(self.metric_name, "{}_{}".format(self.metric_name, self.hostname), 'gauge')
        metric.add_sample(self.metric_name, value=jsondata['data']['data']['value'],
                          labels={ 'host': self.hostname, '{}_subvalue'.format(self.metric_name): 'None',
                          })
        yield metric


class BiDirGauge(object):

    def __init__(self, jsondata, metric_name, hostname, metric_out, metric_in):
        self.jsondata = jsondata
        self.metric_name = metric_name
        self.hostname = "_".join(hostname.split('.'))
        self.metric_in = metric_in
        self.metric_out = metric_out

    def collect(self):
        jsondata = collect(self.jsondata)
        metric = Metric(self.metric_name, '{} {}'.format(self.hostname, self.metric_name), 'gauge')
        if 'data' in jsondata['data']['data']:
            if len(jsondata['data']['data']['data']) == 1:
                if "_".join(jsondata['data']['data']['data'][0]['key'].split(' ')) == self.metric_in:
                    metric.add_sample(self.metric_name, value=0,
                                      labels={
                                              'host': self.hostname,
                                              '{}_subvalue'.format(self.metric_name): self.metric_in
                                              })
                    metric.add_sample(self.metric_name, value=jsondata['data']['data']['data'][0]['value'],
                                      labels={
                                              'host': self.hostname,
                                              '{}_subvalue'.format(self.metric_name): self.metric_out
                                              })
                elif "_".join(jsondata['data']['data']['data'][0]['key'].split(' ')) == self.metric_out:
                    metric.add_sample(self.metric_name, value=jsondata['data']['data']['data'][0]['value'],
                                      labels={
                                              'host': self.hostname,
                                              '{}_subvalue'.format(self.metric_name): self.metric_in
                                              })
                    metric.add_sample(self.metric_name, value=0,
                                      labels={
                                              'host': self.hostname,
                                              '{}_subvalue'.format(self.metric_name): self.metric_out
                                              })
            else:
                metric.add_sample(self.metric_name, value=jsondata['data']['data']['data'][1]['value'],
                                  labels={
                                          'host': self.hostname,
                                          '{}_subvalue'.format(self.metric_name): self.metric_in
                                          })
                metric.add_sample(self.metric_name, value=jsondata['data']['data']['data'][0]['value'],
                                  labels={
                                          'host': self.hostname,
                                          '{}_subvalue'.format(self.metric_name): self.metric_out
                                          })
            metric.add_sample(self.metric_name, value=jsondata['data']['data']['value'],
                              labels={
                                      'host': self.hostname,
                                      '{}_subvalue'.format(self.metric_name): 'total'
                                      })
        else:
            metric.add_sample(self.metric_name, value=0,
                              labels={
                                      'host': self.hostname,
                                      '{}_subvalue'.format(self.metric_name): self.metric_in
                                      })
            metric.add_sample(self.metric_name, value=0,
                              labels={
                                      'host': self.hostname,
                                      '{}_subvalue'.format(self.metric_name): self.metric_out
                                      })
            metric.add_sample(self.metric_name, value=jsondata['data']['data']['value'],
                              labels={
                                      'host': self.hostname,
                                      '{}_subvalue'.format(self.metric_name): 'total'
                                      })
        yield metric


class BucketsGauge(object):
    def __init__(self, jsondata, metric_name, hostname):
        self.jsondata = jsondata
        self.metric_name = metric_name
        self.hostname = "_".join(hostname.split('.'))

    def collect(self):
        jsondata = collect(self.jsondata)
        metric = Metric(self.metric_name, '{} {}'.format(self.hostname, self.metric_name), 'gauge')
        print(jsondata)
        if 'data' in jsondata['data']['data']:
            for y in range(len(jsondata['data']['data']['data'])):
                metric.add_sample(self.metric_name, value=jsondata['data']['data']['data'][y]['value'],
                                  labels={
                                          'host': self.hostname,
                                          '{}_subvalue'.format(self.metric_name): "_".join(jsondata['data']['data']['data'][y]['key'].split(' '))
                                          })
        metric.add_sample(self.metric_name, value=jsondata['data']['data']['value'],
                          labels={
                                  'host': self.hostname,
                                  '{}_subvalue'.format(self.metric_name): 'total'
                                  })
        yield metric

class heatmap101(object):
    def __init__(self, jsondata, metric_name, hostname):
        self.jsondata = jsondata
        self.metric_name = metric_name
        self.hostname = "_".join(hostname.split('.'))

    def collect(self):
        jsondata = collect(self.jsondata)
        metric = Metric(self.metric_name, '{} {}'.format(self.hostname, self.metric_name), 'gauge')
        print(jsondata)
        if 'data' in jsondata['data']['data']:
            for y in range(len(jsondata['data']['data']['data'])):
                try:
                    exists = int((jsondata['data']['data']['data'][x]['key'])
                except ValueError:
                    pass
            for x in range(101):
                if x == exists:
                    metric.add_sample(self.metric_name, value=jsondata['data']['data']['data'][x]['value'],
                                      labels={
                                              'host': self.hostname,
                                              '{}_subvalue'.format(self.metric_name): "_".join(jsondata['data']['data']['data'][x]['key'].split(' '))
                                                })
                else:
                    metric.add_sample(self.metric_name, value="0",
                                      labels={
                                              'host': self.hostname,
                                              '{}_subvalue'.format(self.metric_name): str(x)+"%")
                                                })
        metric.add_sample(self.metric_name, value=jsondata['data']['data']['value'],
                          labels={
                                  'host': self.hostname,
                                  '{}_subvalue'.format(self.metric_name): 'total'
                                  })
        yield metric
