def sortcat(n, *args):
    args = list(args)
    args = map(str, args)
    args.sort(key=len)
    args.reverse()
    if (n == -1):
        return "".join(args)
    else:
        return "".join(args[:n])
