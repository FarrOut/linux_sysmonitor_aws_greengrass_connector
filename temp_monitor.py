# import greengrasssdk
import subprocess

# client = greengrasssdk.client('iot-data')

# publish temperature metric through MQTT topic
def main(thermal_zone = 0):
    filename = '/sys/class/thermal/thermal_zone'+ str(thermal_zone) + '/temp'
    temp = subprocess.Popen(['cat', filename], stdout = subprocess.PIPE)
    print (str(temp.communicate()))
