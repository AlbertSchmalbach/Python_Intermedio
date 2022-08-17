from ncclient import manager
import xml.dom.minidom
# create a variable object that represents the NETCONF session
m = manager.connect(
         host="sandbox-iosxe-latest-1.cisco.com",
         #host="sandbox-iosxe-recomm-1.cisco.com", 
         port=830,
         username="developer",
         password="C1sco12345",
         hostkey_verify=False
         )
# use the "get_config" method of the NETCONF object
# to get back the current "source" configuration
netconf_reply = m.get_config(source="running")
print(netconf_reply)
input("###### Press Enter to continue to Step 2 ######")
print( xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )
input("###### Press Enter to continue to Step 3 ######")
# limit the output from the NETCONF reply using a NETCONF filter
# in this case, filtering only data defined in 
# the native cisco ios xe yang model
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
# use the "get_config" method of the NETCONF object
# to get back the current "source" configuration
# limiting the output using the filter
netconf_reply = m.get_config(source="running", filter=netconf_filter)
print( xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )
