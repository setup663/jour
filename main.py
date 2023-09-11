# Открываем первый входной файл и считываем типы событий
with open('in1.txt', 'r', encoding='UTF-8') as file1:
    event_types = {}
    for line in file1:
        code, name = line.strip().split(' ')
        event_types[int(code)] = name

# Открываем второй входной файл и считываем события
with open('in2.txt', 'r', encoding='UTF-8') as file2:
    events = []
    for line in file2:
        code, event_type, name, start_time, duration, status = line.strip().split(' ')
        event = {
            'code': int(code),
            'event_type': int(event_type),
            'name': name,
            'start_time': start_time,
            'duration': int(duration),
            'status': status
        }
        events.append(event)

# Устанавливаем длительность рабочего дня
working_hours = 8

# Открываем выходной файл для записи результатов
with open('out.txt', 'w', encoding='UTF-8') as output_file:
    # Подсчитываем относительную долю загрузки
    total_duration = sum(event['duration'] for event in events)
    relative_load = total_duration / working_hours

    # Записываем результаты в выходной файл
    for event in events:
        event_type_name = event_types[event['event_type']]
        output_file.write(f"{event_type_name} {event['name']} {event['duration']} продолжительность\n")

    output_file.write(f"\nОтносительная доля загрузки рабочего дня: {relative_load} часов\n")

