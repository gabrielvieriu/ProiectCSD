
import subprocess

def encrypt_AES(input_file, output_file, key):
    try: 
        cmd=['openssl', 'enc', '-aes-256-cbc', '-in', input_file, '-out', output_file, '-k', key]
        subprocess.run(cmd,check=True)
        print(f"File {input_file} encrypted successfully to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Encryption failed: {e}")
def decrypt_AES(input_file, output_file, key):
    try: 
        cmd=['openssl', 'enc', '-d', '-aes-256-cbc', '-in', input_file, '-out', output_file, '-k', key]
        subprocess.run(cmd,check=True)
        print(f"File {input_file} decrypted successfully to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Decryption failed: {e}")
def generate_RSA_key(private_key_path,public_key_path):
    try:
        cmd=['openssl', 'genrsa', '-out', private_key_path, '1024']
        subprocess.run(cmd,check=True)
        print(f"RSA Private Key generated: {private_key_path}")

        cmd=['openssl', 'rsa', '-in', private_key_path, '-pubout', '-out', public_key_path]
        subprocess.run(cmd,check=True)
        print(f"RSA Public Key generated: {public_key_path}")
    except subprocess.CalledProcessError as e:
        print(f"RSA key generation failed: {e}") 
def encrypt_RSA(input_file,output_file,public_key_path):
    try:
        cmd = ['openssl', 'rsautl', '-encrypt', '-inkey', public_key_path, '-pubin', '-in', input_file, '-out', output_file]
        subprocess.run(cmd, check=True)
        print(f"File {input_file} encrypted with RSA public key to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"RSA encryption failed: {e}")
def decrypt_RSA(input_file,output_file,private_key_path):
    try:
        cmd = ['openssl', 'rsautl', '-decrypt', '-inkey', private_key_path, '-in', input_file, '-out', output_file]
        subprocess.run(cmd, check=True)
        print(f"File {input_file} decrypted with RSA private key to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"RSA decryption failed: {e}")
