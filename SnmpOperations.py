from pysnmp import hlapi
from pysnmp.hlapi import *

def get(target, oids, credentials, port = 161, engine = SnmpEngine(), context=ContextData()):
    handler = getCmd(engine, CommunityData(credentials), UdpTransportTarget((target, port)), context, *construct_object_types(oids))
    return fetch(handler, 1) [0]

def construct_object_types(list_of_oids):
    object_types = []

    for oid in list_of_oids:
        object_types.append(hlapi.ObjectType(hlapi.ObjectIdentity(oid)))

    return object_types

def fetch(handler, count):
    result = []
    for i in range(count):
        try:
            error_indication, error_status, error_index, var_binds = next(handler)
            if not error_indication and not error_status:
                items = {}
                for var_bind in var_binds:
                    items[str(var_bind[0])] = cast(var_bind[1])
                result.append(items)
            else:
                raise RuntimeError("got SNMP error: {0}" .format(error_indication))
        except StopIteration:
            break
    return result


def cast(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return float(value)
        except (ValueError, TypeError):
            try:
                return str(value)
            except (ValueError, TypeError):
                pass
    return value


def getsingleoid(ip, oid, community, ifscan = False):
    handler= getCmd(SnmpEngine(), CommunityData(community), UdpTransportTarget((ip, 161)), ContextData(), ObjectType(ObjectIdentity(oid)))

    errorIndication, errorStatus, errorIndex, varBinds = next(handler)
    
    if errorIndication:
        pass
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        if ifscan:
            for varBind in varBinds:
                print(ip + ": " + varBind[1])
        else:
            return varBinds

result = getsingleoid('192.168.122.121', '1.3.6.1.2.1.1.1.0', 'public')
if result:
    for varBind in result:
        print(' = '.join([x.prettyPrint() for x in varBind]))
else:
    print('No result')

def getsingleoid_v3(ip, oid, user, auth_key, priv_key, auth_protocol, priv_protocol, ifscan=False):
    handler = getCmd(
        SnmpEngine(),
        UsmUserData(user, authKey=auth_key, privKey=priv_key, authProtocol=auth_protocol, privProtocol=priv_protocol),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(handler)

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        if ifscan:
            for varBind in varBinds:
                print(ip + ": " + varBind[1])  # Prints the value if scanning the network
        else:
            return varBinds

# result3 = getsingleoid_v3('192.168.122.121', '1.3.6.1.2.1.1.1.0', 'demo', 'temp_password', 'temp_password', 'usmHMACMD5AuthProtocol', 'usmDESPrivProtocol')
# if result3:
#     for varBind in result3:
#         print(' = '.join([x.prettyPrint() for x in varBind]))
# else:
#     print('No result')


ip = '192.168.122.121'
oid = '1.3.6.1.2.1.1.1.0'  # Example OID for sysDescr
user = 'bootstrap'
auth_key = 'temp_password'
priv_key = 'temp_password'
auth_protocol = usmHMACMD5AuthProtocol
priv_protocol = usmDESPrivProtocol

result2 = getsingleoid_v3(ip, oid, user, auth_key, priv_key, auth_protocol, priv_protocol)
if result2:
    for varBind in result2:
        print(' = '.join([x.prettyPrint() for x in varBind]))
