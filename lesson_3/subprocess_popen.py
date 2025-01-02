import subprocess


def simple_popen():
    p = subprocess.Popen(['python', 'test_program2.py'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(p.stdout.read())

    return p


if __name__ == '__main__':
    res = simple_popen()

