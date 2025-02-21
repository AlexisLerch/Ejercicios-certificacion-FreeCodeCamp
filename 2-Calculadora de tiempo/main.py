def add_time(start, duration, day=None):
    # Declarar variables.
    start_hours = int(start.split(':')[0])
    start_minutes = int(start.split(':')[1][:2])
    start_meridian = start.split(':')[1][3:]
    
    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1][:2])

    # Convertir a 24hrs.
    if start_meridian == 'PM' and start_hours != 12:
        start_hours += 12
    elif start_meridian == 'AM' and start_hours == 12:
        start_hours = 0

    # Agregar duration horas y minutos
    total_hours = start_hours + duration_hours
    total_minutes = start_minutes + duration_minutes

    # Minutos desbordados arreglar
    if total_minutes >= 60:
        total_hours += 1
        total_minutes %= 60

    # Calcular los dias
    days_later = total_hours // 24
    hours_later = total_hours % 24

    # Convertir a 12hrs.
    #meridian = 'AM'
    if hours_later == 0:
        hours_later = 12
        start_meridian = 'AM'
    elif hours_later < 12:
        start_meridian = 'AM'
    elif hours_later == 12:
        start_meridian = 'PM'
    else:
        hours_later -= 12
        start_meridian = 'PM'

    # Opcional dias de la semana
    if day:
        days_of_the_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        day_index = days_of_the_week.index(day.capitalize())
        end_day_index = (day_index + days_later) % 7 
        end_day = days_of_the_week[end_day_index]
    else:
        end_day = None

    # Formato para return
    formatted_time = f"{hours_later}:{total_minutes:02d} {start_meridian}"
                
    if end_day:
        formatted_time += f", {end_day}"

    # Proximos dias mensaje
    if days_later == 1:
        formatted_time += ' (next day)'
    elif days_later > 1:
        formatted_time += f' ({days_later} days later)'


    print(formatted_time)
                
    return formatted_time
add_time('11:43 PM', '24:20', 'tueSday')
add_time('11:30 AM', '2:32', 'Monday')
add_time('3:00 PM', '3:10')
add_time('10:10 PM', '3:30')
add_time('11:43 AM', '00:20')
add_time('6:30 PM', '205:12')
add_time('11:59 PM', '24:05')
add_time('8:16 PM', '466:02')
add_time('11:59 PM', '24:05', 'Wednesday')
print('______________________________')
