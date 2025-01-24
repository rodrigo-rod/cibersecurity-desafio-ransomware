# Criptografia de arquivos emulando um ransomware

### Objetivos

- Com intuito didático, iremos criar dois códigos em Python para criptografar e descriptografar um arquivo baseado em uma chave previamente estabelecida utilizando criptografia AES.
  
### Procedimentos

#### Criptografia:

- o codigo contido no arquivo ``` encrypter_v2.py ``` irá ler o conteudo do arquivo alvo ```teste.txt```
- o conteudo do arquivo será criptografado usando a chave fornecida
- o conteudo já criptografado será salvo em um novo arquivo chamado ```teste.txt.enc```
- arquivo ```teste.txt```é deletado

#### Descriptografia:

- o codigo contido no arquivo ``` dencrypter_v2.py ``` irá ler o conteudo do arquivo alvo ```teste.txt.enc```
- o conteudo do arquivo será decriptografado usando a mesma chave fornecida anteriormente
- o conteudo já descriptografado será salvo em um novo arquivo chamado ```teste.txt```
- arquivo ```teste.txt.enc```é deletado

