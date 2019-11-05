import geopy
import pandas
from geopy.geocoders import Nominatim

def main():
    io = pandas.read_csv('census.csv', index_col=None, header=0, sep=",")

    def get_latitude(x):
        return x.latitude

    def get_longitude(y):
        return y.longitude

    geolocalizador = Nominatim(timeout=5)

    geolocalizador_columna = io['Area_Name'].apply(geolocalizador.geocode)
    io['latitude'] = geolocalizador_columna.apply(get_latitude)
    io['longitude'] = geolocalizador_columna.apply(get_longitude)
    io.to_csv('geocoding-output.csv')

if __name__ == '__main__':
    main()
