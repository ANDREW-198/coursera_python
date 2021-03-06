import os.path
import csv

class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)



class Truck(CarBase):
    car_type = 'truck'
    def __init__(self, brand, photo_file_name, carrying, body_whl = '0x0x0'):
        super().__init__(brand, photo_file_name, carrying)
        self.body_length, self.body_width, self.body_height = list(map(float, body_whl.split(sep='x')))

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

def get_car_list(csv_filename): #FIX MI
    car_list = []
    list_car_type = ['car', 'truck', 'spec_machine']
    list_photo_type = ['.jpg', '.jpeg', '.png', '.gif']
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if row[0] in list_car_type and len(row[1]) != 0 and os.path.splitext(row[3])[1] in list_photo_type and len(row[5]) != 0:
                    if row[0] == list_car_type[0]: #Truck
                        car_list.append(Car(row[1], row[3], float(row[5]), int(row[2])))

                    elif row[0] == list_car_type[1]: #Truck
                        if len(row[4]) == 0:
                            car_list.append(Truck(row[1], row[3], float(row[5])))
                        else:
                            car_list.append(Truck(row[1], row[3], float(row[5]), row[4]))

                    elif row[0] == list_car_type[2]: #spec_machine
                        if len(row[6]) != 0:
                            car_list.append(SpecMachine(row[1], row[3], float(row[5]), row[6]))
                        else:
                            continue
                    else:
                        print('something wrong')

                else:
                    continue
            except IndexError:
                continue

            except ValueError:
                continue



    return car_list

if __name__ == '__main__':
    print(get_car_list('coursera_week3_cars.csv'))
