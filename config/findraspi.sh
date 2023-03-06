#
#

if [ $# -eq 0 ]; then
  VERBOSE=false
elif [ $# -eq 1 ] && [ $1="-v" ]; then
  VERBOSE=true
else
  echo Usage: bash raspi.sh OR bash raspi.sh -v
  exit 1
fi

IP_ADDR=`hostname | xargs host | awk 'NF>1{print $NF}'`
if "${VERBOSE}"; then
  echo IP Address: $IP_ADDR
fi

SUBNET_ADDR=`echo $IP_ADDR | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.'`
if "${VERBOSE}"; then
  echo Subnet Address: $SUBNET_ADDR
fi

echo ${SUBNET_ADDR}{1..254} | xargs -P256 -n1 ping -s1 -c1 -W1 | grep ttl

if "${VERBOSE}"; then
  echo IP scanning done.
fi

MAC1="28:CD:C1|B8:27:EB|DC:A6:32|E4:5F:01|E4:5F:1"
MAC2="28-CD-C1|B8-27-EB|DC-A6-32|E4-5F-01|E4-5F-1"
MAC3="28CD.C1|B827.EB|DCA6.32|E45F.01"
MAC="${MAC1}|${MAC2}|${MAC3}"
if "${VERBOSE}"; then
  echo $MAC
fi
echo --- Found Raspi devices ---

arp -a | grep -i -E "${MAC}"
