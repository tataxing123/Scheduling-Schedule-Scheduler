def scale_to_unit_float(num):
    '''' scaled to the form x.xxxx '''
    # Calculate the scaling factor to represent num in x.xxx format
    magnitude = len(str(abs(num)).split('.')[0])
    scale_factor = 10 ** (magnitude - 1)  # Calculate the scale factor dynamically
    scaled_num = num / scale_factor
    return scaled_num

def weighted_sort(t):
    priority_weight = 3
    deadline_weight = 4
    
    normalized_priority = t.priority.value/5        # normalized by max priority 
    normalized_remaining_time = scale_to_unit_float(t.time_remaing_to_deadline())

    priority_score = t.priority.value * priority_weight
    deadline_score = -t.time_remaining_to_deadline() * deadline_weight
    return priority_score + deadline_score

def sum_func_opt_both(t):
    priority_weight = 1
    time_remaining_weight = -1
    normalized_priority = t.priority.value/5        # normalized by max priority 
    normalized_time_remaining = t.time_remaining_to_deadline() / (15*4*24) # normalized by (1 day) # could change to max deadline
    combined_score = (normalized_time_remaining + time_remaining_weight)/(normalized_priority + priority_weight)  
    print(combined_score)
    return combined_score

def sum_func_opt_deadline(t):
    priority_weight = 1
    time_remaining_weight = 5 # deadline weight
    normalized_priority = t.priority.value/5        # normalized by max priority 
    normalized_time_remaining = t.time_remaining_to_deadline() / (15*4*24) # normalized by (1 day) # could change to max deadline
    combined_score = (normalized_time_remaining + time_remaining_weight)/(normalized_priority + priority_weight)  
    print(combined_score)
    return combined_score

def sum_func_opt_priotity(t):
    priority_weight = 5 
    time_remaining_weight = 1
    normalized_priority = t.priority.value/5        # normalized by max priority 
    normalized_time_remaining = t.time_remaining_to_deadline() / (15*4*24) # normalized by (1 day) # could change to max deadline
    combined_score = (normalized_time_remaining + time_remaining_weight)/(normalized_priority + priority_weight)  
    print(combined_score)
    return combined_score


#product_func = lambda x: x.priority.value *  x.time_remaining_to_deadline()
#sum_func_opt_deadline = lambda x: -(2*x.time_remaining_to_deadline()/x.priority.value)
#sum_func_opt_priotity = lambda x: -(0.5*x.time_remaining_to_deadline()/x.priority.value)
#sum_func_opt_both     = lambda x: -(x.time_remaining_to_deadline()/x.priority.value)