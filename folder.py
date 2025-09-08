import os
def list_fils_in_folders(folder_path):
  try:
    files = os.listdir(folder_path)
    return files,None
  except FileNotFoundError:
    return None,"folder not found"
  except PermissionError:
    return None,"permission Denied"


def main():
    folder_path = input("please provide folder name with space : ").split()
    for folders in folder_path:
        files, error_message = list_fils_in_folders(folders)
        if files:
            print(f"Files in {folders} : ")
            for file in files:
                print(file)
        else:
            print(f"Error accessing {folders} : {error_message}")

if __name__ == "__main__":
    main()
