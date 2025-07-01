import redis

def connection_redis():
    try:
        r = redis.Redis(
            host='redis-16692.c44.us-east-1-2.ec2.redns.redis-cloud.com',
            port=16692,
            decode_responses=True,
            username="default",
            password="eWyontv8eDrKQGh24ybQWamU6ImBBuI8",
        )
        r.ping()
        print('Redis conectado!')
        return r 
    except redis.ConnectionError:
        print('Erro ao conectar ao Redis')
        return None
    except Exception as e:
        print(f'Ocorreu um erro: {e}')  
        return None


