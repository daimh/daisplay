#!/usr/bin/env python3
#19500101 initial version daimon:/etc/Model/sh
import sys
import argparse
import json, urllib.request

def get_my_stops(my_stop_names):
	stops = json.loads(urllib.request.urlopen('https://mbus.doublemap.com/map/v2/stops', timeout=4).read().decode())
	my_stops = []
	for stop in stops:
		if stop['name'] not in my_stop_names: continue
		my_stops.append(stop)
	if len(my_stops) != len(my_stop_names): raise Exception('ERR-001')
	return my_stops
def get_routes():
	my_routes = {}
	for route in json.loads(urllib.request.urlopen('https://mbus.doublemap.com/map/v2/routes', timeout=4).read().decode()):
		my_routes[route['id']] = route
	return my_routes
def get_stop_route_time(my_stop_names):
	my_stops = get_my_stops(my_stop_names)
	my_routes = get_routes()
	stop_route_time = {}
	for stop in my_stops:
		etas = json.loads(urllib.request.urlopen(f'https://mbus.doublemap.com/map/v2/eta?stop={stop["id"]}', timeout=4).read().decode())
		for eta in etas['etas'].values():
			for bus in eta['etas']:
				stop_route_time.setdefault(stop['name'], {}).setdefault(my_routes[bus['route']]['short_name'], []).append(bus['avg'])
	return stop_route_time
def main():
	stop_route_time = get_stop_route_time([ 'Couzens/BSRB', 'Couzens/Zina Pitcher', 'BSRB'])
	for st in sorted(stop_route_time.keys()):
		print(st)
		for route_time in sorted(stop_route_time.get(st, {}).items()):
			print(route_time)
if __name__ == '__main__': main()
