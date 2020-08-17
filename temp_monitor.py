import greengrasssdk
import subprocess

client = greengrasssdk.client('iot-data')

# publish temperature metric through MQTT topic
def publish(thermal_zone = 0):
    filename = '/sys/class/thermal/thermal_zone'+ str(thermal_zone) + '/temp'
    temp = subprocess.check_output(['cat', filename])
    client.publish(topic='metric/temp', payload=temp)    
    print (temp)
