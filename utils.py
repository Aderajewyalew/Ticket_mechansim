import  time
def time_counter(times):
    for t in range(0,times):
        time.sleep(1)
        print(f"00:00:0{t}")