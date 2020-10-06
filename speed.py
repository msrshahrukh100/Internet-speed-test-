import speedtest


def test(iterations):
    download, upload = 0, 0
    for i in range(iterations):
        print("*", end="")
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        download += res["download"]
        upload += res["upload"]
    return download / iterations, res["upload"] / iterations


print("Results - ")
download, upload = test(10)

print('Download: {:.2f} Kb/s\n'.format(download / 1024))
print('Upload: {:.2f} Kb/s\n'.format(upload / 1024))

