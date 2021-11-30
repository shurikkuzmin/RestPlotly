import time
import subprocess
def follow(file, sleep_sec=0.1):
    """ Yield each line from a file as they are written.
    `sleep_sec` is the time to sleep after empty reads. """
    line = ''
    while True:
        tmp = file.readline()
        if tmp is not None:
            line += tmp
            if line.endswith("\n"):
                subprocess.Popen(["curl",'"http://127.0.0.1:5000"'], shell=True)
                #-H "Content-Type: application/json" -d "{""Curve"":{""x"":[1,2],""y"":[3,4]}}" -X POST')
                yield line
                line = ''
        elif sleep_sec:
            time.sleep(sleep_sec)


if __name__ == '__main__':
    with open("data.log", 'r') as file:
        for line in follow(file):
            print(line, end=' ')
