def time_to_seconds(time_str):
    time_split_list= time_str.split(":")

    hours = int(time_split_list[0])
    minutes = int(time_split_list[1])
    seconds  = int(time_split_list[2])

    total_seconds = hours * 3600 + minutes * 60 + seconds

    return total_seconds

def seconds_to_time(seconds):
    hours = str(seconds // 3600)
    if len(hours) != 2:
        hours = "0" + hours
    seconds = seconds % 3600
    minutes = str(seconds // 60)
    if len(minutes) != 2:
        minutes = "0" + minutes
    seconds = str(seconds % 60)
    if len(seconds) != 2:
        seconds = "0" + seconds
    time = f"{hours}:{minutes}:{seconds}"

    return time

def solution(play_time, adv_time, logs):

    play_seconds = time_to_seconds(play_time)
    play_list = [0] * (play_seconds + 1)
    
    for log in logs:
        start, end = map(time_to_seconds, log.split('-'))
        play_list[start] += 1
        play_list[end] -= 1

    for i in range(1, play_seconds + 1):
        play_list[i] = play_list[i] + play_list[i - 1]
    
    adv_seconds = time_to_seconds(adv_time)
    max_time = sum(play_list[:adv_seconds])
    current_time = max_time
    start_time = 0
    for i in range(1, play_seconds - adv_seconds + 1):
        current_time = play_list[i + adv_seconds - 1] - play_list[i - 1] + current_time 
        if current_time > max_time:
            max_time = current_time
            start_time = i

    answer = seconds_to_time(start_time)
    return answer
