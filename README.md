# PV181 – ASN.1 and public-key formats

## Start

Double-click the launcher for your system. The first start creates a Python environment
and installs the packages from `requirements.txt`, which takes a few minutes.

| System  | Launcher                                                  |
|---------|-----------------------------------------------------------|
| Windows | `start_jupyter.cmd`                                       |
| macOS   | `start_jupyter.command`                                   |
| Linux   | `./start_jupyter.sh`                                      |

Add `lab` to start JupyterLab instead of the classic Notebook, e.g. `./start_jupyter.sh lab`.

The notebooks run `openssl` commands. Linux and macOS have OpenSSL already; on Windows the
launcher uses the copy that comes with [Git for Windows](https://git-scm.com/download/win).

## Notebooks

Work through them in order.

1. `01_encodings.ipynb` – integers, bytes, hex, base64, byte order
2. `02_openssl_keys.ipynb` – generating RSA/EC keys, PEM vs DER, inspecting them with `openssl asn1parse` (creates the key files for 03–06)
3. `03_der_parsing.ipynb` – a manual tag-length-value parser, then the `asn1` library
4. `04_asn1tools_rsa_math.ipynb` – an ASN.1 grammar (`RSA_pub.asn`) gives names to the RSA values; checking the RSA mathematics
5. `05_rsa_from_scratch.ipynb` – square-and-multiply; RSA encryption/decryption and CRT with the key from 02, cross-checked with OpenSSL
6. `06_ec_from_scratch.ipynb` – point addition and double-and-add on P-256; public key, ECDH and ECDSA with the key from 02, cross-checked with OpenSSL

Solutions are in `solutions/` (`*_solution.ipynb`, run with outputs; `RSA_pub.asn` is the completed grammar).

## Working on aisa

Run the OpenSSL commands from notebook 02 on `aisa.fi.muni.cz` (without the leading `!`),
then copy the keys to your machine from PowerShell or a terminal in the `notebooks` folder:

```
scp "xlogin@aisa.fi.muni.cz:pv181/*.pem" "xlogin@aisa.fi.muni.cz:pv181/*.der" .
```
