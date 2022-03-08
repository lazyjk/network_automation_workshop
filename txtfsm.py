from scrapli import Scrapli
from ntc_templates.parse import parse_output
def main():
    device = {
    'host': '172.20.20.11',
    'auth_username':'admin',
    'auth_password': 'admin',
    'auth_strict_key': False,
    'platform': 'arista_eos'
    }
    with Scrapli(**device) as conn:
        sh_ver = conn.send_command('sh version').result
    print(sh_ver)
    version_parse = parse_output(platform="arista_eos", command='show version', data=sh_ver)
    print (version_parse)
if __name__ == "__main__":
    main()
