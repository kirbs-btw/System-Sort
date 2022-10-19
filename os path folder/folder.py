import os

def main():
    folderNames = os.listdir('H:\Projekte\Projekte')
    for name in folderNames:
        print(name)


if __name__ == '__main__':
    main()