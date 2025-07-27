from Crypto.Cipher import AES

from Crypto.Util.Padding import pad, unpad

import hashlib

import random
import os


def encrypt_flag(shared_secret: int, plaintext=str):

    # Derive AES key from shared secret

    sha256 = hashlib.sha256()

    sha256.update(str(shared_secret).encode('ascii'))

    key = sha256.digest()[:16]

    # Encrypt flag

    iv = os.urandom(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    ciphertext = cipher.encrypt(pad(plaintext, 16))

    # Prepare data to send

    data = {}

    data['iv'] = iv.hex()

    data['encrypted_flag'] = ciphertext.hex()

    return data


def is_pkcs7_padded(message):

    padding = message[-message[-1]:]

    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):

    # Derive AES key from shared secret

    sha256 = hashlib.sha256()

    sha256.update(str(shared_secret).encode('ascii'))

    key = sha256.digest()[:16]

    # Decrypt flag

    ciphertext = bytes.fromhex(ciphertext)

    iv = bytes.fromhex(iv)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    plaintext = cipher.decrypt(ciphertext)


    if is_pkcs7_padded(plaintext):

        return unpad(plaintext, 16).decode('ascii')

    else:

        return plaintext.decode('ascii')


p = 0x9b56e5a15a05efc1d8cc19203c8d130ddc76bca2b95cd522f86240fa1e04d740a2ac406783345c52461f43a99dc299dcd518f9362b184d3875e592cd5db1945d1648801d133f66e7b77a759a0d9fd0f65e0f7cd1fb58d8b80bce0750184f832233ecd06ac4554508bf94081bdeaac0920e43a7a0885df66d60eafed7e04d6410435838803190ecee539e4a4f66a157e158ac879095faa5ea9dca27051101d0e2c614a5b9dfb2dbc4315869747432faa9b559601cdfc0fbf446205414e05cfa1cec8be05410a7c60975f5b24a4a6062081475b10e599e94b676a54863aca8095df040e2315eb85fc5405715aa7f6e222badfc35a05b75a849af6e1efb551a559574044e470096c62d8a6a67d46be69a225da3906558ebc28040c2c3480f4097aa9dffa58a5ae21a78fc284276d701a94e0b375b0d993990f98eacdf8c12d77593ce738d691dd0b3fc6783a85b85b121f43f3fbe4c9e5e18a55de1a3cdff44c9ad36e7b40fa9f9876545cd66a25b9f307c1aed9b65112b8ca3afb800c592fd3708753068047bd6813726aaf18426e589d122e263e1c1ee080cd0d81c8c861139bf98fb2132c56ce970f4f253f01cac54b042cff8c87a5637c7e06d7755c0011291a7ecec98f1d8d823e2d03ff785a0969105984e1672714870e7ebeed1bf87e7517106f1dd18e947aba0050730685f3d8e4a6bff67b8ac547e22391579ff

g = 0x2

flag = b'crypto{???...???}'


prec = p.bit_length()


a = int(random.getrandbits(prec))

a &= 2**(prec-1) - 1

a |= 2**(prec-2)

A = 0xacc08cfc620bc08ff97da4250716b6acdaeac988a3ec3b416c3d31801f92b7c394e8af4a7c2eb9d3c9141981c14fe826c2249c35ef9dac3c4d3f87613ce3e8e5c2bfe9099334e0082494a74895f4a513f523fc7495e3e1c237cffb0af2952295d3b18832d820c834f841122fca92bd0293f9d6cfacdf2985b2736bb6c48f6b4aceded4f50f693a83d70eee8024d039836667e6e0006b4756801a0176dd16872532288b26042f8e10d1d4973447fa3545d39e59efa3162568874cd01ea77497bd98b37220fd5d1a761680de7a1502c35ca6e9b339541f62de02fee2af68d68afa65a94a180ba5a5635619d8d9e34d6abdd60992838c0e0e49acc26e8b1b1163c0b62a3f1c611e88bcf43b4b43960338a3ec378e601c2a3dfbd6bee0d8c5f3c636146357260aec5936c75e4c4d303464dc9e15d15ffae0b0bba08e2f0c64a8a41ca70f7ebaafea35115803931e9e0e93360391f6d2ec7f739722be776956166d824fc52cf044d2f6be596d1319b09bb8994e139dde21ff1bbc7e2284a881dd43b5616f0d726fd982e2f6597aa7d45cae6fa30a531aec2320868e1131d9e64d6e54d58ee1fb6720a8828d58c30bb87b0f46625bec584d6354071e1d2fe09fc6ada403a4a8ca14548e2c63bb0a9ec5d7fc321b3985856d17b0b8498e545fcfa85ee3e7154982103136e79d829ddd4d51d0c86d1225cf6b09546787bebe0b7

print(f"Alice sends public A: {hex(A)}")


b = int(random.getrandbits(prec))

b &= 2**(prec-1) - 1

b |= 2**(prec-2)

B = 0x8c1eb587b0c5808666b22a627dad9ceb3eede9dc69768c668fe4a0479ffb92e53653aac087289d57019691439bd7349e0bdb5bd4d0287d1d6f7605ca652fc41fc6a0f1b22ad185a85b6ca2c6a4d02779abeb9ee42ae36b836e5b59690cec6b6663ac316fdf5365d0ff52190a55e6dd814d1958e6044e17a6050f74b8f3ed1d23cff5f55a73b3e64812b632d37cb8ea3ba2703150e1586eb30e20459bf2058e68f4939d7155e57c499cae1f28b65485f72579f1560c2a97279dc78ee3281cbdcd5f4e34bc76f3b7ccffab74a9d1616294454c34b31572ed95bfdffcb87adfa42f3bdd71bc38c0c75931cfa66d5d0c6406cff716a50cf3b0eb7bddfd60f35b44bc66d6cf5da518acc7bfcae1499eaa71a5343f3787f808bb1255848939015d50a00ae6f872e4511f6b70f2a5a906d0bf420f5834cfd0a073bada43e9056ace9fd5e3253cb6135407f8e6e474b8645613ce69769912bf76c2738ff387974613a5599b5aba911feb8c838fe3b2fd2be6755ea5b3546f6202380bdb2549dfa754e6e1bedbcb51532c8b8e244a3fa531fedcf134f7b1f34002c74e6f88cdfa6e6d58031ddb5f92a17f4cfc7df59406ca2bdac1e16b7d6365d3eaa4508c69ddbb363e3ea32957e71725c11e9b8c0aae699dcd942c99d70515aebdc78f6a2e92be135163f12987881a8c1f57663f80896f611cc94e416b3bdd0b50e6c2c885c2ce

print(f"Bob sends public B: {hex(B)}")


CS_Alice = pow(B,a,p); CS_Bob = pow(A,b,p)


print(f"Same common secrets? {CS_Alice == CS_Bob}")


ct = encrypt_flag(CS_Alice, flag)

print(ct)