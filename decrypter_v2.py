from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_file(file_path, key):
  """
  Criptografa um arquivo usando AES-256 em modo CBC.

  Args:
    file_path: Caminho para o arquivo a ser criptografado.
    key: Chave de criptografia de 32 bytes.
  """

  with open(file_path, 'rb') as f:
    plaintext = f.read()

  # Preenche o texto simples para ser um múltiplo do tamanho do bloco
  padded_plaintext = pad(plaintext, AES.block_size, style='pkcs7')

  # Cria um objeto de cifra AES
  cipher = AES.new(key, AES.MODE_CBC)

  # Criptografa o texto simples preenchido
  ciphertext = cipher.encrypt(padded_plaintext)

  # Salva os dados criptografados em um novo arquivo
  encrypted_file_path = file_path + ".enc"
  with open(encrypted_file_path, 'wb') as f:
    f.write(cipher.iv + ciphertext)

  # Remove o arquivo original
  os.remove(file_path)

# Exemplo de uso
key = b'your_32_byte_secret_key'  # Substitua pela sua chave real
file_path = 'teste.txt' 

encrypt_file(file_path, key)
