while True:
    try:
        number= int(input('what number brah?\n'))
        print(18/number)
        break
    except ValueError:
        print('brah enter number brah')
    except ZeroDivisionError:
        print('brah dont do that')
    except:
        break
    finally:
        print('cool number brah')