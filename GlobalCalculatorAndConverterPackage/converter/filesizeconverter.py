def convert_file_size( units, units_to_convert_to, unformatted_size):
    # units = unformatted_size[-2:]
    absolute_size = int(unformatted_size)

    if units_to_convert_to == 'TB':
        if units == 'Ti':
            return absolute_size
        elif units == 'Gi':
            return absolute_size * 1024
        elif units == 'Mi':
            return absolute_size * 1024 * 1024
    elif units_to_convert_to == 'GB':
        if units == 'Ti':
            return absolute_size / 1024
        elif units == 'Gi':
            return absolute_size
        elif units == 'Mi':
            return absolute_size * 1024
    elif units_to_convert_to == 'MB':
        if units == 'Ti':
            return absolute_size / 1024 / 1024
        elif units == 'Gi':
            return absolute_size / 1024
        elif units == 'Mi':
            return absolute_size 
#unformatted_size (str): size to convert ('1Gi'/'100Mi')
#units_to_convert_to (str): units to convert the size to ( TB/GB/MB) 