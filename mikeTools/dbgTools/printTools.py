# ！/usr/bin/env python
# _*_ coding:utf-8 _*_


def print_buf(data):
    if type(data) is not bytes:
        raise TypeError("The input is not a 'bytes' data, please check it!")
    print_no_enter("            0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F\n")
    total_line = len(data) // 16
    remain_bytes = len(data) % 16
    for line_index in range(total_line):
        print_no_enter("%08dh:" % line_index)
        offset = line_index * 16
        for i in range(16):
            # print_no_enter(' ')
            print_no_enter(" %02x" % data[offset + i])
        print_no_enter(" ; ")
        for i in range(16):
            buf = data[offset + i]
            if is_printable_ascii(buf):
                print_no_enter(chr(buf))
            else:
                print_no_enter(".")
        print_no_enter("\n")
    if remain_bytes > 0:
        print_no_enter("%08dh:" % total_line)
        offset = total_line * 16
        for i in range(remain_bytes):
            # print_no_enter(' ')
            print_no_enter(" %02x" % data[offset + i])
        for i in range(16 - remain_bytes):
            print_no_enter("   ")
        print_no_enter(" ; ")
        for i in range(remain_bytes):
            buf = data[offset + i]
            if is_printable_ascii(buf):
                print_no_enter(chr(buf))
            else:
                print_no_enter(".")


def print_no_enter(data):
    print(data, end='', sep='')


def is_printable_ascii(data):
    return (data > 33) and (data < 126)


def main():
    str = "dhfsadfewafvdshtr\xadetyrsgfduteyrhfgdhjfu\x11"
    print_buf(str.encode("utf8"))


if __name__ == "__main__":
    # execute only if run as a script
    main()
