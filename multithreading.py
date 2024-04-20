import multiprocessing, threading, numpy as np, os, sys, time, threading, multiprocessing, random as r

numberOfCores = multiprocessing.cpu_count()
print ("Num of cores are: ", numberOfCores)

startTime = time.time()






def matrix_multiply(matrix, constant_matrix, result, index):

    # Check if matrices are compatible for multiplication
    if len(matrix[0]) != len(constant_matrix):
        raise ValueError("Matrices are not compatible for multiplication.")

    # Initialize result matrix with zeros
    temp = [[0 for _ in range(len(constant_matrix[0]))] for _ in range(len(matrix))]

    # Perform matrix multiplication
    for i in range(len(matrix)):
        for j in range(len(constant_matrix[0])):
            for k in range(len(constant_matrix)):
                temp[i][j] += matrix[i][k] * constant_matrix[k][j]

    result[index] = temp

matrices = [np.random.rand(100, 100) for _ in range(100)]
constant_matrix = np.random.rand(100, 100)

# Result array to store the multiplication results
results = [None] * 100

# Number of threads
num_threads = 4


activeThreads = threading.activeCount()
print ("Num of threads: ",activeThreads)



for i in range(100):

    # This Creates a sing thread
    t = threading.Thread(target=matrix_multiply, args=(matrices[i], constant_matrix, results, i))
    t.start() # This starts the execution of the thread

    print("Multiplying matrix %d"%(i+1))

    # Wait until the number of active threads becomes less than or equal to the specified number
    while True:
        if threading.active_count() - activeThreads < num_threads:
            break
        time.sleep(1)

    
cmd = 'Sample task'


time.sleep(1)
# Waiting to finish all Threads
while True:
    if threading.activeCount() == activeThreads:
        break
    else:
        print ("    Thread still running (left %d)..."%(threading.activeCount() - activeThreads))
        time.sleep(1)
  
print(" All Thread ends")
  
print(" Thread ends")
print("Total Time %f sec" % (round( time.time() - startTime,4)))