#!/usr/bin/env python3
#19500101 initial version daimon:/etc/Model/sh
import sys
import argparse
import json, urllib.request, time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

stops = {
	'1153' : 'Glen/Catherine OB',
	'1216' : 'Couzens/BSRB',
	'1831' : 'BSRB',
}
def get_stop_route_time(my_stops):
	stop_route_time = {}
	now = datetime.now()
	for stop_id, stop_name in my_stops.items():
		stop = json.loads(urllib.request.urlopen(f'https://www.theride.org/api/ServiceData?method=predictionsforstop&stpid={stop_id}&_={int(time.time())}', timeout=4).read().decode())
		prds = stop['bustime-response'].get('prd', [])
		if type(prds) is dict: prds = [prds]
		for prd in prds:
			diff = int( (datetime.strptime(prd['prdtm'], '%Y%m%d %H:%M') - now).total_seconds() / 60 )
			if diff < 0 or diff > 300: continue
			stop_route_time.setdefault(stop_name, {}).setdefault(prd['rt']+'-'+prd['rtdir'], []).append(diff)
	return stop_route_time
def main():
	stop_route_time = get_stop_route_time(stops)
	for st in sorted(stop_route_time.keys()):
		print(st)
		for route_time in sorted(stop_route_time.get(st, {}).items()):
			print(route_time)
if __name__ == '__main__': main()
