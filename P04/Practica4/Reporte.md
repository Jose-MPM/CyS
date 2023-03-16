# Práctica 4 - SSH multiverse

Azpeitia García Karyme Ivette

Pedro Méndez Jose Manuel 

## Procedimiento.

### Escanear el objetivo

Primero realizaremos un escaneo de puertos para encontrar y recopilar información sobre los puertos están activos escuchando by SSH, apoyandonos de nmap ejecutando este comando:

```bash
nmap 44.199.201.139 -sV -Pn -sT
```

| ![](img/nmapOut.png)
|:----------------------:|
| Imagen sobre la que trabajamos utilizando la herramienta: _Exif.tools_.

* Podemos observar que el servidor tiene los puertos abiertos para SSH abiertos:
	* 222/tcp  open  ssh     OpenSSH 6.6.1p1 Debian 5 (protocol 2.0)
	* 2200/tcp open  ssh     OpenSSH 6.6.1p1 Debian 5 (protocol 2.0)
	* 2222/tcp open  ssh     OpenSSH 6.6.1p1 Debian 5 (protocol 2.0)

* Con shodan obtenemos que esta abierto el puerto 2200 y obtuvimos esta información.

```bash
OpenSSH6.6.1p1 Debian 5

SSH-2.0-OpenSSH_6.6.1p1 Debian-5
Key type: ssh-rsa
Key: AAAAB3NzaC1yc2EAAAADAQABAAABgQC4Iwij+KzpsW0v4w+7uIK4JUNv2guRNymYobgYXT5I1a2F
s3LQHPqy1MPxdgcL2NJJuQAVJv7ei4L2d9BRzn1MK10+Sf1iAidrGuCOJa+iY1ktxrynoePj/WOL
C2nR7roninmLQeUH8nUM6wYvb9qFaiEVH0LDtmoM0KdAiqq/Mndvaa5EcwYfmQ/CAUtg2y4n6Zyw
QjNLTtMljO8uM2wF5KJ9ucREhatb2M4YvvtQr07eKnGXwBKI03GYZMNHRcdLm8DxmDog+Ba4Gt9g
dpl/xQYPWqg130Dd24XPI/XPTCD41alelCCSNmL/4X5M2MAdTyll4d7Uc39owV13HELhh3ByyPmp
mr/ve3CCu3an1dYfvdU90JAv3PZoVQn3qCGxXFQghJs9VOPiiIxoeXxvAJCjInNt2xn/Ui47Vbwl
Y81ZXTXCKub/QI7/e8dbUqO8t4FyjfVMmGW0b65uRoBpRWl5gyV9ZtGTQPM+yfBS40fyuJ5rDQt/
48glIcHVnNE=
Fingerprint: ed:77:90:77:07:7e:17:39:b6:77:98:60:d0:0c:ef:c1

Kex Algorithms:
	curve25519-sha256@libssh.org
	ecdh-sha2-nistp256
	ecdh-sha2-nistp384
	ecdh-sha2-nistp521
	diffie-hellman-group16-sha512
	diffie-hellman-group-exchange-sha256
	diffie-hellman-group14-sha256
	diffie-hellman-group-exchange-sha1
	diffie-hellman-group14-sha1
	diffie-hellman-group1-sha1

Server Host Key Algorithms:
	rsa-sha2-512
	rsa-sha2-256
	ssh-rsa

Encryption Algorithms:
	aes128-ctr
	aes192-ctr
	aes256-ctr
	aes128-cbc
	aes192-cbc
	aes256-cbc
	3des-cbc

MAC Algorithms:
	hmac-sha2-256
	hmac-sha2-512
	hmac-sha2-256-etm@openssh.com
	hmac-sha2-512-etm@openssh.com
	hmac-sha1
	hmac-md5
	hmac-sha1-96
	hmac-md5-96

Compression Algorithms:
	none
```

### Atacar al objetivo: 

Obtener mediante un ataque de diccionario la contraseña correspondiente a su  usuario (utilizando Hydra por ejemplo).

* Primero instalaremos Hydra en nuestra AttackBox con el siguiente comando:
```bash
sudo dnf install hydra -y
```
###  Crear evidencia de haber entrado al sistema

La parte más sencilla, basta que ejecuten $ touch $NumeroDeCuenta para dejar registro que estuvieron ahí.

### Post-explotación.

------
📢⌨️ with ❤️ by [Jose-MPM](https://github.com/Jose-MPM) 😊⌨️ and [Kary-GOD](https://github.com/Kary-AG) 😊⌨️🎁