import time
import concurrent.futures


def myfunc(name):
    print(f"myfunc started with {name}")
    time.sleep(5)
    print("myfunc ended")


if __name__ == '__main__':
    print("main started")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
        e.map(myfunc, ["foo", "bar", "baz"])
    print("main ended")
