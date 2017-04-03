def health_index(age, apples, cigarettes):
    result = (100 - age) + (apples * 2) - cigarettes * 0.5
    print result


alex_stats = [23, 12, 5]
health_index(*alex_stats)
