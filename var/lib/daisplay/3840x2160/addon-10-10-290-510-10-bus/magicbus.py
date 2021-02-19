#!/usr/bin/env python3
#19500101 initial version daimon:/etc/Model/sh
import sys
import argparse
import json, urllib.request, time
import magicbus_key

def get_stop_route_time(my_stops):
	stop_route_time = {}
	for stop_id, stop_name in my_stops.items():
		now = int(time.time())
		link = f'https://mbus.ltp.umich.edu/bustime/api/v3/getpredictions?locale=en&stpid={stop_id}&top=4&key={magicbus_key.key}&format=json&xtime={now}'
		prds = json.loads(urllib.request.urlopen(link, timeout=4).read().decode())
		for bus in prds['bustime-response']['prd']:
			waittime = bus['prdctdn']
			if waittime == 'DUE': continue
			stop_route_time.setdefault(stop_name, {}).setdefault(bus['rt'], []).append(int(waittime))
	return stop_route_time
def main():
	stop_route_time = get_stop_route_time(['M305', 'M307'])
	for st in sorted(stop_route_time.keys()):
		print(st)
		for route_time in sorted(stop_route_time.get(st, {}).items()):
			print(route_time)
if __name__ == '__main__': main()
