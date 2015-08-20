def format_duration(seconds):
	"""This function takes and arbitrary amount of seconds and returns an
		easy to read string. i.e. 3 hours, 15 minutes and 4 seconds"""
    if seconds <= 0:
        return "now"
        
    years = seconds /(60 * 60 * 24 * 365)
    days = (seconds % (60 * 60 * 24 * 365)) / (60 * 60 * 24)
    hours = ((seconds % (60 * 60 * 24 * 365)) % (60 * 60 * 24)) / (60 * 60)
    minutes = (((seconds % (60 * 60 * 24 * 365)) % (60 * 60 * 24)) % (60 * 60)) / (60)
    seconds = (((seconds % (60 * 60 * 24 * 365)) % (60 * 60 * 24)) % (60 * 60)) % (60)
    
    y_string = format_string("year", years)
    d_string = format_string("day", days)
    h_string = format_string("hour", hours)
    m_string = format_string("minute", minutes)
    s_string = format_string("second", seconds)
    
    item_count = 0
    t_list = [y_string, d_string, h_string, m_string, s_string]
    s_list = []
    for i in range(0, len(t_list)):
        if t_list[i] != "":
            s_list.append(t_list[i])
    
    out_str = ""
    if len(s_list) == 1:
        out_str = "".join(s_list)
    elif len(s_list) == 2:
        out_str = " and ".join(s_list)
    else:
        out_str = ", ".join(s_list[:len(s_list)-1])+ " and {}".format(s_list[len(s_list) - 1])
    return out_str
    
def format_string(name, value):
    if value == 0:
        string = ""
    elif value == 1:
        string = "1 {}".format(name)
    else:
        string = "{} {}s".format(value, name)
    return string