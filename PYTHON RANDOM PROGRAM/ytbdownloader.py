from pytube import YouTube
link=input("enter the link")
youtube_1=YouTube(link)


videos =youtube_1.streams.all()
vid =list(enumerate(videos))
for i in vid:
    print(i)
strm=int(input("enter index: "))
videos[strm].download()
print("downloaded successfully ")

#https://www.youtube.com/watch?v=CgkZ7MvWUAA&pp=ygUIYnJvIGNvZGU%3D
