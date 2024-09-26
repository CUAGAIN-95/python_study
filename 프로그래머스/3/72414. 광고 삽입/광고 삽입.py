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
    if play_time == adv_time:
        return "00:00:00"
    
    play_seconds = time_to_seconds(play_time)
    adv_seconds = time_to_seconds(adv_time)

    # Create an array to count viewers for each second
    viewer_count = [0] * (play_seconds + 1)

    # Process logs to populate the viewer_count
    for log in logs:
        start, end = map(time_to_seconds, log.split("-"))
        viewer_count[start] += 1
        if end <= play_seconds:  # Prevent index out of bounds
            viewer_count[end] -= 1

    # Calculate the cumulative sum of viewers
    for i in range(1, play_seconds + 1):
        viewer_count[i] += viewer_count[i - 1]

    # Sliding window to find the best start time for the advertisement
    max_viewers = sum(viewer_count[:adv_seconds])
    max_start_time = 0
    current_viewers = max_viewers

    for start_time in range(1, play_seconds - adv_seconds + 1):
        current_viewers += viewer_count[start_time + adv_seconds - 1] - viewer_count[start_time - 1]
        
        if current_viewers > max_viewers:
            max_viewers = current_viewers
            max_start_time = start_time
        elif current_viewers == max_viewers and start_time < max_start_time:
            max_start_time = start_time
    
    return seconds_to_time(max_start_time)
    
