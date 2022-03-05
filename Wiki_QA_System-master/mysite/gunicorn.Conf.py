workers = 4  # Define the number of processes to be opened for processing requests at the same time, adjusted appropriately according to site traffic
worker_class = "gevent" # Use the gevent library to support asynchronous processing of requests and improve throughput
timeout = 120 # Set the timeout to 120 seconds