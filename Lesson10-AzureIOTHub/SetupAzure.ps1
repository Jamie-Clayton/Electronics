# Create a Internet of Things (IOT) register to mananage all your sensor devices

# Authenticate to the Microsoft Cloud Internet of Things register.
az login --allow-no-subscriptions
# A web browser popup will be displayed and MFA will be required to authenticate

# Read the list of tenants associated with the credentials 
az account set --subscription "Visual Studio Enterprise (new)"

# Pick a Geographical location for your systems
az account list-locations -o table
# Pick Canberra, Australia = 'australiacentral'

# 1. Create a Resource group to store all the items that are required to manage IOT devices in the cloud.
$location = 'australiacentral'
$resourceGroupName = 'iot-rg'
$rgExists= az group exists -n $resourceGroupName

if ( $rgExists -ne $true)
{
    az group create --name $resourceGroupName --location $location
}

# 2.    Create a virtual network and subnet if one has not already been created.  Microsoft Docs
#   Consider a separate VNet for each resource group. 
#   az network vnet list -output table
$vNetName = 'iot-vnet'
az network vnet create --resource-group $resourceGroupName --name $vNetName --address-prefix 10.0.42.0/24 --subnet-name default --subnet-prefix 10.0.42.0/24

# x is the next available 3rd octet value

# 3.    Create a public IP Address.  Microsoft Docs
$pubIpName = 'iot-ip'
$dnsName = 'iot-devices' # becomes a region specific URL "fqdn": "iot-devices.australiacentral.cloudapp.azure.com"
az network public-ip create --resource-group $resourceGroupName --name $pubIpName --dns-name $dnsName

# 4.    Create a network security group.  Microsoft Docs
$securityGroupName = 'iot-nsg'
az network nsg create --resource-group $resourceGroupName --name $securityGroupName

# 5.    Create a rule to allow SSH to the machine.  Microsoft Docs
az network nsg rule create --resource-group $resourceGroupName --nsg-name $securityGroupName --name allow-ssh --protocol tcp --priority 1000 --destination-port-range 22 --access allow

# 6.    Create a virtual NIC.   Microsoft Docs
$resourceGroupName = 'iot-rg'
$nicName = 'iot-nic'
$pubIpName = 'iot-ip'
$securityGroupName = 'iot-nsg'
$vNetName = 'iot-vnet'
az network nic create --resource-group $resourceGroupName --name $nicName --vnet-name $vNetName --subnet default --public-ip-address $pubIpName --network-security-group $securityGroupName

# 7. Create a Bastion Server to protect your IOT devices
# $bastionName = 'iot-bastion'
# az network bastion create --location $location --name $bastionName --public-ip-address $pubIpName --resource-group $resourceGroupName --vnet-name $vNetName

# 8. Create an IOT Hub
$iotHubName = 'iot-jenasys-hub'
az iot hub create --name $iotHubName --resource-group $resourceGroupName --sku S1 --location $location 