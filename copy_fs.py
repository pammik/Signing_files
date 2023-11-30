import shutil
import os

def copy_files(source_folder, destination_folder):
    try:
        print('asd')
        # Создаем папку назначения, если её нет
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Получаем список файлов в исходной папке
        files = os.listdir(source_folder)

        for file in files:
            print('asd2')
            # Полные пути к исходному и целевому файлам
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)

            # Копируем файл
            shutil.copy2(source_path, destination_path)

        print(f"Files copied from {source_folder} to {destination_folder}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Укажите пути к вашим папкам
    print('asd3')
    #source_folder_path = "D:\git\Personal\Signing_files\Download"
    #destination_folder_path = "D:\git\Personal\Signing_files\Download\\test"
    source_folder_path = "F:\git\Signing_files\Download"
    destination_folder_path = "F:\git\Signing_files\Download\\test"
    copy_files(source_folder_path, destination_folder_path)