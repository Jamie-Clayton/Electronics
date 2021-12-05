# Add devices to an Azure IOT Hub (device register);
# Based on https://forums.raspberrypi.com/viewtopic.php?t=231481

# Authenticate to the Microsoft Cloud Internet of Things register.
az login --allow-no-subscriptions
# A web browser popup will be displayed and MFA will be required to authenticate

# Read the list of tenants associated with the credentials 
az account set --subscription "Visual Studio Enterprise (new)"

# Install IOT specific commandlines prior to registering devices.
az config set extension.use_dynamic_install=yes_without_prompt

# 1. Register a Device (And get the security details required to add your device)
$iotHubName = 'iot-jenasys-hub'
$deviceName = 'Workshop-42-Weather'

# Use IoT Edge devices to perform compute and analytics tasks on data before it's sent to the cloud
az iot hub device-identity create --hub-name $iotHubName --device-id $deviceName  --edge-enabled

$iotHubName = 'iot-jenasys-hub'
$deviceName = 'Workshop-42-AirQuality'
# Use devices that just send raw data.
az iot hub device-identity create --hub-name $iotHubName --device-id $deviceName
