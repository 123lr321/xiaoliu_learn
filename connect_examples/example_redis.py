import redis


def main():
    client = redis.Redis(host='192.168.200.130', port=6379,
                         password='liu0325')
    client.hset('liurun:friend:3', "name", 'wangleihan')
    client.hset('liurun:friend:3','age','25')
    print(client.hget('liurun:friend:3','name').decode())


if __name__ == "__main__":
    main()
