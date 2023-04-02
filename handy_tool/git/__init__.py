import argparse
# what do you think the merged_rm shot

# clean_branch is too long? Can argparse tab complete?


def main():
    parser = argparse.ArgumentParser(description="git util")
    subparsers = parser.add_subparsers(dest='sub_command')

    # do some boring thing
    subparsers.add_parser('del_merged', help='delete merged branch')
    # subparsers.add_parser('c', help='clean the cmake cache files.')

    args = parser.parse_args()
