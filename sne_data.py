file_name = 'SCPUnion2_mu_vs_z.txt'
with open(file_name, 'rb') as fptr:
    data = []
    for line in iter(lambda: fptr.readline(), ''):
        if '#' not in line:
            data.append(
                map(lambda x: float(x), line.split()[-3:])
            )
redshift, magnitude, mag_error = zip(*data)