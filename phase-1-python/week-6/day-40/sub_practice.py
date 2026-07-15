import subprocess

def run(host_ip):
    commands=["ping","-c","3",host_ip]
    try:
        result=subprocess.run(commands,text=True,timeout=5,capture_output=True)

        if result.returncode==0:
            print("executed successfully")
            print("payload:")
            print(result.stdout)
        else:
            print("error occur while execution")
            print("error deatils")
            print(result.stderr)
    except subprocess.TimeoutExpired:
        print("error time out occured")
    except FileNotFoundError:
        print("error: file does not found")