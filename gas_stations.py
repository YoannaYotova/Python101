def gas_station(distance, tank_size,stations):
	list_gas_stations=[]
	tank_size = tank_size - stations[0]

	for i in range(0, len(stations) - 1):

		if stations[i + 1] - stations[i] < tank_size:
			tank_size -=stations[i + 1] - stations[i]
		else:
			tank_size = 90 - (stations[i + 1] - stations[i])
			list_gas_stations.append(stations[i])
			
	if tank_size < distance - stations[len(stations) - 1]:
		list_gas_stations.append(stations[len(stations) - 1])
		
	return list_gas_stations

def main():
	distance = 390
	tank_size = 80
	stations = [70, 90, 140, 210, 240, 280, 350]
	print(gas_station(distance, tank_size, stations))

if __name__ == '__main__':
	main()
