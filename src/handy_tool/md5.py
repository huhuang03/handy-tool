import hashlib
import argparse


def calculate_file_hash(file_path, use_sha512=False):
    hasher = hashlib.sha512() if use_sha512 else hashlib.sha256()

    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hasher.update(chunk)

    return hasher.hexdigest()


def main():
    parser = argparse.ArgumentParser(description="Calculate SHA256 or SHA512 of a file.")
    parser.add_argument("path", help="Path to the file")
    parser.add_argument("--sha512", action="store_true", help="Use SHA512 instead of SHA256")

    args = parser.parse_args()

    result = calculate_file_hash(args.path, args.sha512)
    print(result)


if __name__ == "__main__":
    main()
