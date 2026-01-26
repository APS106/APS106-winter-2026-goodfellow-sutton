import time

def continue_walking(turtle, step_size):
    """
    (turtle, int) --> bool
    Will determine if the turtle can take another step without hitting the wall.

    Example:
        at_wall(turtle)
        >> True
    """
    if turtle.get_state()['points'][-1]['x'] + step_size <= 380:
        return True
    return False


def train_ai_model():

    print('Downloading data from cloud...')
    time.sleep(3)
    print('Download complete.\n')
    print('Prepare data for training...')
    time.sleep(3)
    print('Preprocessing complete.\n')
    print('Training AI model...')
    time.sleep(1)
    print('10% complete...')
    time.sleep(1)
    print('20% complete...')
    time.sleep(1)
    print('30% complete...')
    time.sleep(1)
    print('40% complete...')
    time.sleep(1)
    print('50% complete...')
    time.sleep(1)
    print('60% complete...')
    time.sleep(1)
    print('70% complete...')
    time.sleep(1)
    print('80% complete...')
    time.sleep(1)
    print('90% complete...')
    time.sleep(1)
    print('100% complete...\n')
    print('Uploading final model and results to the cloud...')
    time.sleep(3)
    print('Upload complete.\n')
    print('Training complete.')
