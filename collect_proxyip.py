import socket
import os
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 目标域名列表
domains = [
    'try.cloudflare.com',
    'workers.cloudflare.com',
    'ns.cloudflare.com',
    'cn.cloudflare.com',
    'ct.cloudflare.com',
    'cloudflare.tv'
]

# 删除旧文件（如果存在）
if os.path.exists('proxyip.txt'):
    os.remove('proxyip.txt')

# 解析域名并保存IP
with open('proxyip.txt', 'w') as file:
    for domain in domains:
        try:
            # 获取域名对应的IP
            ip_address = socket.gethostbyname(domain)
            file.write(f'{ip_address}\n')  # 只写入IP
            logging.info(f'成功解析 {domain} -> {ip_address}')
        except socket.gaierror as e:
            logging.error(f'域名解析失败: {domain} - {str(e)}')

logging.info('所有域名解析完成，结果已保存到 proxyip.txt')
