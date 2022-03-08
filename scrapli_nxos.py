from scrapli import Scrapli
def main():
    device = {'host': '172.20.20.23','auth_username': 'admin','auth_password': 'admin', 'auth_strict_key': False, 'platform': 'cisco_nxos'}
    #conn = Scrapli(**device)
   # print(conn, dir(conn), type(conn))
   # print(conn)
    #conn.open()
    with Scrapli(**device) as conn:
        print(conn.get_prompt())
        print(conn.send_command('sh ver').result)
        cmd_responses = conn.send_commands(['sh ver','sh run','sh int status'])
        for response in cmd_responses:
            print(response)
        return


if __name__ == "__main__":
    main()
