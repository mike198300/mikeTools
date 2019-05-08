import mikeTools.dbgTools.printTools as print_tool


def main():
    str = "dhfsadfewafvdshtr\xadetyrsgfduteyrhfgdhjfu\x11"
    print_tool.print_buf(str.encode("utf8"))


if __name__ == "__main__":
    # execute only if run as a script
    main()



