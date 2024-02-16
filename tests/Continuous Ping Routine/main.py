import ping3, time


urls_to_ping = ['https://painelconstru.com.br','www.painelconstru.com.br', 'comprador.painelconstru.com.br', 'fornecedor.painelconstru.com.br', 'api2.painelconstru.com.br']

def perform_ping_test(url=str):
    try:
        round_trip_time = ping3.ping(dest_addr=url, unit='ms')
        
        if round_trip_time is not False:
            print(f'\n\033[0;33mSuccessfully pinged \033[0;0m{url}. The Round-Trip Time was: {round_trip_time} ms')
        else:
            print(f'\n\033[0;31mThe ping made to {url} failed!\033[0;0m')
    except Exception as e:
        print(f'\nError occurred while pinging {url}: {str(e)}.')


if __name__ == '__main__':
    '''Running a continuous process'''
    while True:
        for url in urls_to_ping:
            perform_ping_test(url=url)
        '''which reruns every 30 seconds'''
        time.sleep(10)
        print('\n-------------------------------------------------------------------------------------------------')