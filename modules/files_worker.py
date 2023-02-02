import os,glob
def make_dir(paths):
    """принимает список путей, проверяет существуют ли папки, если нет, создает их"""
    for path in paths:
        isExist = os.path.exists(path)
        if not isExist:
            try:
                os.makedirs(path)
                print(f"{glob.glob(path)} папка создана в директории запуска программы  ПЕРЕЗАПУСТИТЕ ПРИЛОЖЕНИЕ")
        
            except Exception as e:
                print(f" не удалось создать папки{e}")
        else:
            pass
                


