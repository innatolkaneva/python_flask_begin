import subprocess
#args = shlex.split(command_line) так можно разбить команду для субпроцесса
#stderr=subprocess.STDOUT перенаправление потока в вывод

def run_program():
    res = subprocess.run(['python', 'test_programm.py'], input=b'some input\nanother input')
    print(res)

if __name__ == '__main__':
    run_program()