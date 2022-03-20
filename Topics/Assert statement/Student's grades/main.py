def grades(x):
    x = x.upper()  # capitalize argument
    assert x in 'ABCDF'
    return f'You have got {x}'
