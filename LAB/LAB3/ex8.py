data = "2023-04-24 09:03:32.744178"
print(data)
get_year  = lambda x: x.split(" ")[0].split("-")[0]
get_month = lambda x: x.split(" ")[0].split("-")[1]
get_day   = lambda x: x.split(" ")[0].split("-")[2]
get_time  = lambda x: x.split(" ")[1]
print(get_year(data))
print(get_month(data))
print(get_day(data))
print(get_time(data))