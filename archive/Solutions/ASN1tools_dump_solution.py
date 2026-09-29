#Tasks: Based on exampe usage of asn1tools,
# 0. Look at asn1tools example usage: https://asn1tools.readthedocs.io/en/latest/#example-usage
# 1. Find corresponding grammar for RSA keys - (see page 44 in RFC 3447 https://www.rfc-editor.org/rfc/rfc3447.txt).
# 2. create .asn1 file for public and private keys
# 3. compile and decode RSA private key (DER)
# 4. compile and decode RSA public key (DER)
# 5. verify values of public and private keys -
#       verify: N = p * q,
#       find d: d = e^{-1} (mod (p-1)*(q-1))
#       verify e: d mod p-1 is equal to value extracted from private key
#       verify e: d mod q-1 is equal to value extracted from private key

import asn1tools
encoded_bytes = open('data/RSA_2048_priv.der', 'rb').read()

rsa = asn1tools.compile_files("RSA_pub_solution.asn")
encoded_bytes = open('data/RSA_2048_priv.der', 'rb').read()
rsa_priv = rsa.decode('RSAPrivateKey', encoded_bytes)
print(rsa_priv)
N = rsa_priv['modulus']
p = rsa_priv['prime1']
q = rsa_priv['prime2']
print(N == p * q)