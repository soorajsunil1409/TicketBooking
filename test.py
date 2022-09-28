import random as r

start = "Delhi"
end = "Bangalore"

for i in range(10):
    flight_no = r.randint(100000, 999999)
    flight_name = r.choice(("Air India", "Indigo"))
    flight_start_time = r.randint(0, 23)
    flight_end_time = flight_start_time + r.randint(1, 6)
    flight_start_time = str(flight_start_time) + ":00"
    flight_end_time = str(flight_end_time) + ":00"
    flight_cost = r.randint(8000, 20000)

    print(flight_no, flight_name, flight_start_time, flight_end_time, flight_cost)

