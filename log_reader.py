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
                numbers = line[:-1].split(" ")
                print(numbers)
                print("String=",f"{{\"Curve\":{{\"x\":{numbers[0]},\"y\":{numbers[1]}}}}}")
                p = subprocess.Popen(["curl","http://127.0.0.1:5000","-H","Content-Type: application/json",
                                      "-d",f"{{\"Curve\":{{\"x\":[{numbers[0]}],\"y\":[{numbers[1]}]}}}}","-X","POST"], shell=True)
                
                p.wait()
                yield line
                line = ''
        elif sleep_sec:
            time.sleep(sleep_sec)


if __name__ == '__main__':
    with open("data.log", 'r') as file:
        for line in follow(file):
            print(line, end=' ')
