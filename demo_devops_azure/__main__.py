import sys

from demo_devops_azure.demo_devops_azure import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
    print("testing pre-commit")
