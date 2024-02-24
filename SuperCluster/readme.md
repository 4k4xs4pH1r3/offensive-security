## Creating a supercluster

### Tested with mpirun (Open MPI) 5.0.2 in MacOS, Kali Linux, and ArchLinux

https://docs.open-mpi.org/en/main/getting-help.html

https://www-lb.open-mpi.org/software/ompi/

https://github.com/open-mpi/ompi

A tool that crawls through networks and systems, analyzing their vulnerabilities and identifying potential attack vectors. It also suggests the use of data analytics to generate actionable insights and recommendations for improving security.

Clear! In short, he set out to create an all-in-one solution for the automation of IT security, from vulnerability scanning to reporting and creating JIRA tickets. The solution would be based on popular security tools such as Metasploit, Nmap, Shodan, Maltego, Burp Suite, among others, and would use techniques such as port scanning, vulnerability search, vulnerability exploitation, reporting and generation. of JIRA tickets.

To implement the solution, a CI/CD pipeline would be used and deployed to GitHub using a supercluster. Crawling and fuzzing techniques would be used to expand the scope of the solution through the detection of vulnerabilities in different operating systems and IoT devices.

The creation of a sales model for this solution was proposed, and a simulation of costs and benefits was carried out to determine the feasibility of the project. Although the initial cost could be high due to the need to hire developers and information security experts, it is expected that the solution would generate income in the long term by being sold as a service to different companies and organizations.

In general, the proposed solution aims to increase the efficiency of computer security through automation, which would allow companies to detect and fix vulnerabilities more quickly.

With just some devices might be a bit challenging, as supercomputers generally require a large number of high-performance computing nodes with specialized hardware and networking infrastructure. However, it is possible to create a small cluster with the available resources.

Here are the basic steps to create a simple cluster using 5 devices:

1. Choose a suitable operating system: You need to choose an operating system that is suitable for cluster computing, such as Linux. You may need to install the operating system on all five devices.

2. Install required software: Install the necessary software packages for cluster computing, such as OpenMPI or MPICH. These packages allow you to write and execute parallel code across multiple nodes.

3. Configure the network: You need to configure the network settings for each device to be able to communicate with each other. You can connect them using a network switch or a router. Alternatively, you can use Wi-Fi if all devices support it.

4. Set up SSH: Secure Shell (SSH) is a network protocol that allows you to access and control one computer from another over a secure channel. You need to set up SSH on each device to enable remote access and control.

5. Configure the cluster: Configure the cluster by creating a file that contains the IP addresses of each device and the number of processors available on each device. You can use the MPI tool to launch and run parallel jobs across the cluster.

6. Test the cluster: Test the cluster by running some simple parallel applications, such as calculating the value of pi or matrix multiplication.

It is important to note that creating a supercluster with just 5 devices will not be as powerful as a real supercomputer. However, it can still provide you with a good learning experience in parallel computing and cluster management.


Steps to create a small cluster using multiple devices:

7. Configure the cluster: Configure the cluster by creating a hostfile that contains the IP addresses of each device and the number of processors available on each device. Type the following command to create a hostfile:

   ```
   nano hostfile
   ```

   Then, add the IP addresses of each device and the number of processors available on each device, like this:

   ```
   192.168.1.1 slots=2
   192.168.1.2 slots=2
   192.168.1.3 slots=1
   192.168.1.4 slots=1
   192.168.1.5 slots=1
   ```

8. Test the cluster: Test the cluster by running some simple parallel applications, such as calculating the value of pi with python. For example, type the following command to calculate the value of pi using 4 and also all the available processors:

   ```
   clear && nano pi_value.py
   ```
```
from mpi4py import MPI
import os
import subprocess

def pi_leibniz(n):
    result = 0.0
    for i in range(n):
        if i % 2 == 0:
            result += 4.0 / (2 * i + 1)
        else:
            result -= 4.0 / (2 * i + 1)
    return result

try:
    # Guess MPI_HOME by finding the location of mpirun
    mpi_location = subprocess.check_output(['which', 'mpirun'], universal_newlines=True).strip()
    mpi_home = os.path.dirname(os.path.dirname(mpi_location))

    # Print MPI_HOME for debugging
    print(f"MPI_HOME: {mpi_home}")

    # Set MPI environment variables
    os.environ['PATH'] = f"{mpi_home}/bin:{os.environ.get('PATH', '')}"
    os.environ['LD_LIBRARY_PATH'] = f"{mpi_home}/lib:{os.environ.get('LD_LIBRARY_PATH', '')}"

    # Print paths for debugging
    print(f"PATH: {os.environ['PATH']}")
    print(f"LD_LIBRARY_PATH: {os.environ['LD_LIBRARY_PATH']}")

    # Check if the MPI_HOME path is correct
    if not os.path.exists(os.path.join(mpi_home, 'bin', 'mpirun')):
        raise FileNotFoundError(f"mpirun not found in {mpi_home}/bin. Check MPI installation.")

    # Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    # Debugging output to see the rank of each process
    print(f"Process {rank}: MPI Initialized")

    # Calculate pi with 10000 terms
    pi_approx = pi_leibniz(10000)

    # Debugging output to see the rank and the result from each process
    print(f"Process {rank}: Pi approximation (Leibniz, 10000 terms): {pi_approx:.10f}")

except Exception as e:
    # Print the exception and traceback for detailed debugging
    import traceback
    print(f"An error occurred: {e}")
    traceback.print_exc()

finally:
    # Finalize MPI
    MPI.Finalize()
```

   ```
   clear && chmod +x pi_value.py && python3 -m pip install --upgrade pip && pip install mpi4py 
   ```
   ```
   mpirun -v --hostfile hostfile -np 4 python ./pi_value.py
   ```
   ```
   mpirun -v --hostfile hostfile --mca btl tcp,self -x DISPLAY=localhost:0 python ./pi_value.py
   ```
   ```
   mpirun -v --use-hwthread-cpus python ./pi_value.py
   ```

You can also compile and run your own parallel applications using OpenMPI.

You can also test locally in Linux or MacOS by running
   ```
mpirun -v -np 4 python ./pi_value.py 
   ```

That's it! You have now created a small cluster using 5 devices with Linux.
