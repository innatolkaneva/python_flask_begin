import sys


def main():
    print('To stdout')
    print('To stderr', file=sys.stderr)
    user_input = input()
    print(f'User input {user_input}')


if __name__ == '__main__':
    main()