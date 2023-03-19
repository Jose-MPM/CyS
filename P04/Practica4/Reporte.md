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

* Sin embargo intentando obtener más información usando nmap y ejecutando el comando:  
	- sT TCP connect scan
	
```bash
nmap -sV -Pn -sT -p -10000 44.199.201.139
```

* Obtuvimos  los siguiente:	
PORT     STATE SERVICE VERSION
	* 222/tcp  open  ssh     OpenSSH 6.6.1p1 Debian 5 (protocol 2.0)
	* 2200/tcp open  ssh     OpenSSH 6.6.1p1 Debian 5 (protocol 2.0)
	* 2202/tcp open  ssh     OpenSSH 6.6.1p1 Debian 5 (protocol 2.0)
	* **_2220/tcp open  netiq?_**.
	* 2222/tcp open  ssh     OpenSSH 6.6.1p1 Debian 5 (protocol 2.0)
	
* https://www.freecodecamp.org/news/how-to-use-hydra-pentesting-tutorial/
https://www.youtube.com/watch?v=hn32C2-TzME

* Obtendremos más información realizando unas conecciones vía ssh:

	- ssh -p 222 315073120@44.199.201.139 
		- nos permite realizar 3 intentos de contraseña
			- olakhace1
			- esdiverti
			- JOSEMPM12
	- ssh -p 2222 315073120@44.199.201.139 
		- nos permite realizar 3 intentos de contraseña
			- JOSEMANUE
			- josemanue
			- joseyapas
	- ssh -p _2202_ 315073120@44.199.201.139 
		- nos permite realizar 3 intentos de contraseña
			- contraseñ
			- CONTRASEÑ
			- NOPASASTE
	- ssh -p _**2220**_ 315073120@44.199.201.139 
		- No nos permite hacer nada y ahora creo que perdí mi tiempo, porque se queda en el limbo.
	- ssh -p 2222 315073120@44.199.201.139 
		- nos permite realizar 3 intentos de contraseña
			- pasaste12
			- bandera12
			- BANDERASI
 
####  Uso del parámetro _-v_.

* Ejecutando ssh con el párametro *_-v_* sobre uno de los puertos que nos permitían intentar realizar una conección rapido obtuvimos la siguiente información tras poder ingresar nuestra clave:

```bash
ntory@debian11:~$ ssh -v -p 2202 315073120@44.199.201.139 
OpenSSH_8.4p1 Debian-5+deb11u1, OpenSSL 1.1.1n  15 Mar 2022
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files
debug1: /etc/ssh/ssh_config line 21: Applying options for *
debug1: Connecting to 44.199.201.139 [44.199.201.139] port 2202.
debug1: Connection established.
debug1: identity file /home/ntory/.ssh/id_rsa type -1
debug1: identity file /home/ntory/.ssh/id_rsa-cert type -1
debug1: identity file /home/ntory/.ssh/id_dsa type -1
debug1: identity file /home/ntory/.ssh/id_dsa-cert type -1
debug1: identity file /home/ntory/.ssh/id_ecdsa type -1
debug1: identity file /home/ntory/.ssh/id_ecdsa-cert type -1
debug1: identity file /home/ntory/.ssh/id_ecdsa_sk type -1
debug1: identity file /home/ntory/.ssh/id_ecdsa_sk-cert type -1
debug1: identity file /home/ntory/.ssh/id_ed25519 type -1
debug1: identity file /home/ntory/.ssh/id_ed25519-cert type -1
debug1: identity file /home/ntory/.ssh/id_ed25519_sk type -1
debug1: identity file /home/ntory/.ssh/id_ed25519_sk-cert type -1
debug1: identity file /home/ntory/.ssh/id_xmss type -1
debug1: identity file /home/ntory/.ssh/id_xmss-cert type -1
debug1: Local version string SSH-2.0-OpenSSH_8.4p1 Debian-5+deb11u1
debug1: Remote protocol version 2.0, remote software version OpenSSH_6.6.1p1 Debian-5
debug1: match: OpenSSH_6.6.1p1 Debian-5 pat OpenSSH_6.6.1* compat 0x04000002
debug1: Authenticating to 44.199.201.139:2202 as '315073120'
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256@libssh.org
debug1: kex: host key algorithm: rsa-sha2-512
debug1: kex: server->client cipher: aes128-ctr MAC: hmac-sha2-256-etm@openssh.com compression: none
debug1: kex: client->server cipher: aes128-ctr MAC: hmac-sha2-256-etm@openssh.com compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ssh-rsa SHA256:f+L9DhB9m8fs7VoLhofLiCe55Kqe3Lf6vVPo+Ryaq8M
debug1: Host '[44.199.201.139]:2202' is known and matches the RSA host key.
debug1: Found key in /home/ntory/.ssh/known_hosts:4
debug1: rekey out after 4294967296 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey in after 4294967296 blocks
debug1: Will attempt key: /home/ntory/.ssh/id_rsa 
debug1: Will attempt key: /home/ntory/.ssh/id_dsa 
debug1: Will attempt key: /home/ntory/.ssh/id_ecdsa 
debug1: Will attempt key: /home/ntory/.ssh/id_ecdsa_sk 
debug1: Will attempt key: /home/ntory/.ssh/id_ed25519 
debug1: Will attempt key: /home/ntory/.ssh/id_ed25519_sk 
debug1: Will attempt key: /home/ntory/.ssh/id_xmss 
debug1: SSH2_MSG_EXT_INFO received
debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,rsa-sha2-512,rsa-sha2-256,ssh-rsa,ssh-dss>
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: password,publickey
debug1: Next authentication method: publickey
debug1: Trying private key: /home/ntory/.ssh/id_rsa
debug1: Trying private key: /home/ntory/.ssh/id_dsa
debug1: Trying private key: /home/ntory/.ssh/id_ecdsa
debug1: Trying private key: /home/ntory/.ssh/id_ecdsa_sk
debug1: Trying private key: /home/ntory/.ssh/id_ed25519
debug1: Trying private key: /home/ntory/.ssh/id_ed25519_sk
debug1: Trying private key: /home/ntory/.ssh/id_xmss
debug1: Next authentication method: password
315073120@44.199.201.139's password: 
```

* Ejecutando ssh con el párametro *_-v_* sobre el puerto(2220) que NO nos permitían intentar realizar una conección rapido obtuvimos la siguiente información tras poder ingresar nuestra clave:

```bash
PLANTILLA
```

* Por lo que ahora atacaremos los 4 puertos que permiten realizar una conección by ssh.

### Atacar al objetivo: 

Obtener mediante un ataque de diccionario la contraseña correspondiente a su  usuario (utilizando Hydra por ejemplo).

* Primero instalaremos Hydra en nuestra AttackBox con el siguiente comando:
```bash
sudo dnf install hydra -y 
```



sudo dnf install hydra -y
hydra -l usuario -p contraseñaAUsar attackbox2 ssh

hydra -L archivo_de_usuario -p contraseñaAUsar: attackbox2 ssh 

hydra -L archivo_de_usuario -P archivo_con_contraseñaAUsar: attackbox2 ssh 

###  Crear evidencia de haber entrado al sistema

La parte más sencilla, basta que ejecuten $ touch $NumeroDeCuenta para dejar registro que estuvieron ahí.

### Post-explotación.
```bash
PLANTILLA
```
------
📢⌨️ with ❤️ by [Jose-MPM](https://github.com/Jose-MPM) 😊⌨️ and [Kary-GOD](https://github.com/Kary-AG) 😊⌨️🎁