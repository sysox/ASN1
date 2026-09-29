import base64

########################################################################################################
########################################## TASK 1 ######################################################
########################################################################################################
#Task 1: PEM vs DER
#  Read PEM as lines, strip armor (lines: ...BEGIN..., ...END...),  decode to bytes and compare with DER
print("\nTask 1")
def compare_der_pem(path_pem, path_der):
    with open(path_pem) as file:
        bytes_pem = b''

    with open(path_der, mode='rb') as file:
        bytes_der = b''
    if (bytes_pem == bytes_der):
        print("Data correctly converted to DER (bytes) - Well done!")
    else:
        print("PEM does not correspond to DER")


compare_der_pem(path_pem='', path_der='')

########################################################################################################
########################################## TASK 2 ######################################################
########################################################################################################
# Implement length(data_bytes, offset) which takes:
# data_bytes: bytes of the der file
# offset:


types_verbose = \
{
 0x02:'INTEGER',
 0x03:'BIT STRING',
 0x04:'OCTET STRING',
 0x05:'NULL',
 0x06:'OBJECT',
 0x13:'PRINTABLESTRING',
 0x14:'T61STRING',
 0x17:'UTCTIME',
 0x30:'SEQUENCE',
 0x31:'SET'
 }

def tag(data_bytes, offset):
    ID = data_bytes[offset]
    if ID in types_verbose:
        return types_verbose[ID], offset + 1
    else:
        return ID, offset + 1

def length(data_bytes, offset):
    return length, offset # returns length and new offset


def value(data_bytes, offset,  length):
    return data_bytes[offset: offset + length], offset + length

def tlv(data_bytes, offset, depth=0):
    offset_backup = offset  # position where tlv starts
    t, offset = tag(data_bytes, offset)
    l, offset = length(data_bytes, offset)

    if (t in ['SEQUENCE', 'SET']) or not(t in types_verbose.values()):
        print('\t' * depth, f'offset={offset_backup}, tag={t}, length={l}')
        sequence_end = offset + l
        while (offset < sequence_end):
            offset = tlv(data_bytes, offset, depth + 1)

    else:
        v, offset = value(data_bytes, offset, l)
        print('\t' * depth, f'offset={offset_backup}, tag={t}, length={l}')
    return offset

bytes_der = open('data/.........', 'rb').read()
tlv(bytes_der, 0, depth=0)