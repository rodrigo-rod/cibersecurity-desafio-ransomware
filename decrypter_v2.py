from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def decrypt_file(file_path, key):
  """
  Descriptografa um arquivo criptografado usando AES-256 em modo CBC.

  Args:
    file_path: Caminho para o arquivo criptografado.
    key: Chave de criptografia de 32 bytes.
  """

  with open(file_path, 'rb') as f:
    # Lê o IV e o texto cifrado do arquivo
    iv = f.read(16)  # Supondo um IV de 16 bytes
    ciphertext = f.read()

  # Cria um objeto de cifra AES
  cipher = AES.new(key, AES.MODE_CBC, iv)

  # Descriptografa o texto cifrado
  plaintext = cipher.decrypt(ciphertext)

  # Remove o preenchimento
  plaintext = unpad(plaintext, AES.block_size, style='pkcs7') 

  # Salva os dados descriptografados em um novo arquivo
  decrypted_file_path = file_path[:-4]  # Remove a extensão ".enc"
  with open(decrypted_file_path, 'wb') as f:
    f.write(plaintext)

# Exemplo de uso
key = b'my_32_byte_secret_key'  # Substitua pela sua chave real
encrypted_file_path = 'teste.txt.enc' 

decrypt_file(encrypted_file_path, key)
