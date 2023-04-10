from utils import file_operations as fo
from utils import misc as misc


def main():
    path = "./test/webtest.txt"

    urls, err = fo.getUrlsFromFile(path)

    for url in urls:
        print(misc.validateURL(url))


if __name__ == "__main__":
    main()
