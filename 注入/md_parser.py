import base64
import random
import time



if __name__ == '__main__':

    with open('SQL注入/SQL注入漏洞.md', 'r') as f:
        while True:
            line = f.readline()
            if line.startswith('![图片](data:image/png;base64,'):
                base_img = line.replace('![图片](data:image/png;base64,', '')
                base_img = base_img.rstrip(')\n')
                path = 'SQL注入/media/'
                output_file = str(time.time_ns()) + str(random.randint(100, 999)) + ".png"
                path = path + output_file
                with open(path, 'wb') as s:
                    s.write(base64.decodebytes(bytes(base_img, encoding='utf-8')))
                line = '<img src="'+path + '" alt="' + path + '" style="zoom:50%;" align="left"/>'
                with open('SQL注入/SQL注入.md', 'a') as n:
                    n.write(line)
            elif line:
                with open('SQL注入/SQL注入.md', 'a') as n:
                    n.write(line)
            else:
                break