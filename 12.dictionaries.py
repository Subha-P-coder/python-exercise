# paired data
# fast lookup -- if i pass keys it return a values
# it can't access duplicate

trip ={
    'trip_id':'UB12345',
    'pick up':'dindigul',
    'drop':['coimbatore','trichy','chennai','banglore'],
    'fare': 1000.00,
    'driver':'Ravi',
    'status':'completed',
    'trip_id':'UB123456'
}

print(trip)
print(trip["status"]) # if i pass keys it will return value
# print(trip["dindigul"]) # if i pass values it will throw error

print(trip.keys())
print(trip.values())

trip.update({"car_model":"suzuki"})
print(trip)

trip.update({"car_model": "hyundai"})
print(trip)

trip.pop("status")
print(trip)
trip.update({"status":"completed"})
print(trip)

print(trip["drop"][1])

for location in trip['drop']:
    print(location)


trips ={
   'UB001' : {'trip_id':"UB001",'pick up':'dindigul','drop':'coimbatore','fare':1000},
   'UB002' : {'trip_id':"UB002",'pick up':'chennai','drop':'trichy','fare':2000},
   'UB003' : {'trip_id':"UB003",'pick up':'banglore','drop':'karur','fare':3000},
}

print("UB001 fare:",trips['UB001']["fare"])

for trip_id, details in trips.items():
    print(trip_id)
    print(details['pick up'],"-->",details['drop'])

trips1 = [
    {'trip_id':"UB001",'pick up':'dindigul','drop':'coimbatore','fare':1000},
    {'trip_id':"UB002",'pick up':'chennai','drop':'trichy','fare':2000},
    {'trip_id':"UB003",'pick up':'banglore','drop':'karur','fare':3000},
]

for trip in trips1:
    print(trip['trip_id'])
    print(trip['fare'])
    print(trip['pick up'],"to",trip['drop'])