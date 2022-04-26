from statistics import mean
import pandas as pd
import os
import os.path
from glob import iglob
import time 
import concurrent.futures 
from multiprocessing.pool import ThreadPool as Pool
from threading import Thread
import threading
from concurrent.futures import ProcessPoolExecutor


source =os.path.dirname(os.path.abspath(__file__))+"/archivos/*.csv"
#changing directory
output_dir = os.path.dirname(os.path.abspath(__file__))+"/resultados//"


paths = []
destinpaths = []
for path in iglob(source):
  paths.append(path)
  destinpaths.append(os.path.join(output_dir, os.path.basename(path).replace(".csv", "_out.csv")))

print(source)
print(output_dir)
print(paths)
print(destinpaths)
repetance = [1,2,3,4,5,6,7,8,9,10]
n_hilos_ls = [1,2,4,8]


def reset_out():
  for f in os.listdir(output_dir):
    os.remove(os.path.join(output_dir, f))


#Sequential
def all_files3():
  for path in paths:
      destfilepath = os.path.join(output_dir, os.path.basename(path).replace(".csv", "_out.csv"))
      df = pd.read_csv(path, sep=',',parse_dates=False, header=0, usecols=['Open', 'High', 'low', 'close'])
      line_count = "count," + str(df["Open"].count()) +"," + str(df["High"].count()) +","+ str(df["low"].count())+ ',' +  str(df["close"].count()) + "\n"
      line_mean = "mean," + str(df["Open"].mean()) +"," + str(df["High"].mean()) +","+ str(df["low"].mean())+ ',' +  str(df["close"].mean()) + "\n"
      line_std = "std," + str(df["Open"].std()) +"," + str(df["High"].std()) +","+ str(df["low"].std())+ ',' +  str(df["close"].std()) + "\n"
      line_min = "min," + str(df["Open"].min()) +"," + str(df["High"].min()) +","+ str(df["low"].min())+ ',' +  str(df["close"].min()) + "\n"
      line_max = "max," + str(df["Open"].max()) +"," + str(df["High"].max()) +","+ str(df["low"].max())+ ',' +  str(df["close"].max()) + "\n"
      with open(destfilepath, "w") as f2:
        f2.write(line_count)
        f2.write(line_mean)
        f2.write(line_std)
        f2.write(line_min)
        f2.write(line_max)
t1 = time.perf_counter()
for _ in  repetance:
  all_files3()
t2 = time.perf_counter()
print(f'Sequential Code Took :{t2 - t1} seconds')

for n_hilos in n_hilos_ls:
  t1 = time.perf_counter()
  for _ in  repetance:
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_hilos) as exe:
      exe.submit(all_files3)
  t2 = time.perf_counter()
  print(f'Threaded sequential Code Took :{t2 - t1} seconds. Using {n_hilos} threads')



#Data threaded
def single_file(path):
  destfilepath = os.path.join(output_dir, os.path.basename(path).replace(".csv", "_out.csv"))
  df = pd.read_csv(path, sep=',',parse_dates=False, header=0, usecols=['Open', 'High', 'low', 'close'])
  line_count = "count," + str(df["Open"].count()) +"," + str(df["High"].count()) +","+ str(df["low"].count())+ ',' +  str(df["close"].count()) + "\n"
  line_mean = "mean," + str(df["Open"].mean()) +"," + str(df["High"].mean()) +","+ str(df["low"].mean())+ ',' +  str(df["close"].mean()) + "\n"
  line_std = "std," + str(df["Open"].std()) +"," + str(df["High"].std()) +","+ str(df["low"].std())+ ',' +  str(df["close"].std()) + "\n"
  line_min = "min," + str(df["Open"].min()) +"," + str(df["High"].min()) +","+ str(df["low"].min())+ ',' +  str(df["close"].min()) + "\n"
  line_max = "max," + str(df["Open"].max()) +"," + str(df["High"].max()) +","+ str(df["low"].max())+ ',' +  str(df["close"].max()) + "\n"
  with open(destfilepath, "w") as f2:
    f2.write(line_count)
    f2.write(line_mean)
    f2.write(line_std)
    f2.write(line_min)
    f2.write(line_max)
if __name__ == '__main__':
  for n_hilos in n_hilos_ls:
    t1 = time.perf_counter()
    for _ in  repetance:
      result = []
      with concurrent.futures.ProcessPoolExecutor(max_workers=n_hilos) as exe:
        # Maps the method 'single file' with a list of path.
        result = exe.map(single_file, paths)
    t2 = time.perf_counter()
    print(f'Multi Threaded by data Code Took: {t2 - t1} seconds. Using {n_hilos} threads')




#Task threaded
def count_t():
  for path in paths:
    destfilepath = os.path.join(output_dir, os.path.basename(path).replace(".csv", "_out.csv"))
    df = pd.read_csv(path, sep=',',parse_dates=False, header=0, usecols=['Open', 'High', 'low', 'close'])
    line = "count," + str(df["Open"].count()) +"," + str(df["High"].count()) +","+ str(df["low"].count())+ ',' +  str(df["close"].count()) + "\n"
    with open(destfilepath, "a+") as f2:
      f2.write(line)
def mean():
  for path in paths:
    destfilepath = os.path.join(output_dir, os.path.basename(path).replace(".csv", "_out.csv"))
    df = pd.read_csv(path, sep=',',parse_dates=False, header=0, usecols=['Open', 'High', 'low', 'close'])
    line = "mean," + str(df["Open"].mean()) +"," + str(df["High"].mean()) +","+ str(df["low"].mean())+ ',' +  str(df["close"].mean()) + "\n"
    with open(destfilepath, "a+") as f2:
      f2.write(line)
def std():
  for path in paths:
    destfilepath = os.path.join(output_dir, os.path.basename(path).replace(".csv", "_out.csv"))
    df = pd.read_csv(path, sep=',',parse_dates=False, header=0, usecols=['Open', 'High', 'low', 'close'])
    line = "std," + str(df["Open"].std()) +"," + str(df["High"].std()) +","+ str(df["low"].std())+ ',' +  str(df["close"].std()) + "\n"
    with open(destfilepath, "a+") as f2:
      f2.write(line)
def min():
  for path in paths:
    destfilepath = os.path.join(output_dir, os.path.basename(path).replace(".csv", "_out.csv"))
    df = pd.read_csv(path, sep=',',parse_dates=False, header=0, usecols=['Open', 'High', 'low', 'close'])
    line = "min," + str(df["Open"].min()) +"," + str(df["High"].min()) +","+ str(df["low"].min())+ ',' +  str(df["close"].min()) + "\n"
    with open(destfilepath, "a+") as f2:
      f2.write(line)
def max():
  for path in paths:
    destfilepath = os.path.join(output_dir, os.path.basename(path).replace(".csv", "_out.csv"))
    df = pd.read_csv(path, sep=',',parse_dates=False, header=0, usecols=['Open', 'High', 'low', 'close'])
    line = "max," + str(df["Open"].max()) +"," + str(df["High"].max()) +","+ str(df["low"].max())+ ',' +  str(df["close"].max()) + "\n"
    with open(destfilepath, "a+") as f2:
      f2.write(line)
time_t12 = 0
for n_hilos in n_hilos_ls:

  for _ in  repetance:
    reset_out()
    t1 = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_hilos) as exe:
      # Maps the method 'single file' with a list of path.
      exe.submit(count_t)
      exe.submit(mean)
      exe.submit(std)
      exe.submit(min)
      exe.submit(max)
    t2 = time.perf_counter()
    time_t12 += t2-t1
  print(f'Multi Threaded by task Code Took :{time_t12} seconds. Using {n_hilos} threads')







#Data-task threaded
def single_count(path):
    destfilepath = os.path.join(output_dir, os.path.basename(path).replace(".csv", "_out.csv"))
    df = pd.read_csv(path, sep=',',parse_dates=False, header=0, usecols=['Open', 'High', 'low', 'close'])
    line = "count," + str(df["Open"].count()) +"," + str(df["High"].count()) +","+ str(df["low"].count())+ ',' +  str(df["close"].count()) + "\n"
    with open(destfilepath, "a+") as f2:
      f2.write(line)
def single_mean(path):
    destfilepath = os.path.join(output_dir, os.path.basename(path).replace(".csv", "_out.csv"))
    df = pd.read_csv(path, sep=',',parse_dates=False, header=0, usecols=['Open', 'High', 'low', 'close'])
    line = "mean," + str(df["Open"].mean()) +"," + str(df["High"].mean()) +","+ str(df["low"].mean())+ ',' +  str(df["close"].mean()) + "\n"
    with open(destfilepath, "a+") as f2:
      f2.write(line)
def single_std(path):
    destfilepath = os.path.join(output_dir, os.path.basename(path).replace(".csv", "_out.csv"))
    df = pd.read_csv(path, sep=',',parse_dates=False, header=0, usecols=['Open', 'High', 'low', 'close'])
    line = "std," + str(df["Open"].std()) +"," + str(df["High"].std()) +","+ str(df["low"].std())+ ',' +  str(df["close"].std()) + "\n"
    with open(destfilepath, "a+") as f2:
      f2.write(line)
def single_min(path):
    destfilepath = os.path.join(output_dir, os.path.basename(path).replace(".csv", "_out.csv"))
    df = pd.read_csv(path, sep=',',parse_dates=False, header=0, usecols=['Open', 'High', 'low', 'close'])
    line = "min," + str(df["Open"].min()) +"," + str(df["High"].min()) +","+ str(df["low"].min())+ ',' +  str(df["close"].min()) + "\n"
    with open(destfilepath, "a+") as f2:
        f2.write(line)
def single_max(path):
    destfilepath = os.path.join(output_dir, os.path.basename(path).replace(".csv", "_out.csv"))
    df = pd.read_csv(path, sep=',',parse_dates=False, header=0, usecols=['Open', 'High', 'low', 'close'])
    line = "max," + str(df["Open"].max()) +"," + str(df["High"].max()) +","+ str(df["low"].max())+ ',' +  str(df["close"].max()) + "\n"
    with open(destfilepath, "a+") as f2:
      f2.write(line)
if __name__ == '__main__':
  for n_hilos in n_hilos_ls:

    for _ in  repetance:
      t1 = time.perf_counter()
      reset_out()
      with concurrent.futures.ProcessPoolExecutor(max_workers=n_hilos) as exe:
        # Maps the method 'single file' with a list of path.
        exe.map(single_count, paths)
        exe.map(single_mean, paths)
        exe.map(single_std, paths)
        exe.map(single_min, paths)
        exe.map(single_max, paths)
      t2 = time.perf_counter()
      time_t12 += t2-t1
    print(f'Multi Threaded combination Code Took :{time_t12} seconds. Using {n_hilos} threads')
