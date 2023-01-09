# exercise 6.1.4 from unit 6
'''
You received a secret message from a friend who wants to transfer you some item.

Help me decode this in b64 (first encode to UTF-8 for bytes):

CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAuLS0tW1t
fX11dLS0tLS4KICAgICAgICAgICAgICA7LS0tLS0tLS0tLS0tLS58ICA
gICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgICAgICAgIHx8ICA
gLi0tW1tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAgICAgICAgICAg
fHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgICAgfCAgICAgICAgICAgICB
8fCAgfCAgICAgICAgICAgfHwKICAgICAgICAgICAgICB8X19fX19fX19fX19f
X3wvICB8ICAgICAgICAgICB8fAogICAgICAgICAgICAgICAgICAgICAgICA
gICAgICAgIHxfX19fX19fX19fX3wvCgo=

'''
import base64

def main():
    encoded_message = "CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAuLS0tW1tfX11dLS0tLS4KICAgICAgICAgICAgICA7LS0tLS0tLS0tLS0tLS58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgICAgICAgIHx8ICAgLi0tW1tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAgICAgICAgICAgfHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgICAgfCAgICAgICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgICAgICAgICAgICB8X19fX19fX19fX19fX3wvICB8ICAgICAgICAgICB8fAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19fX19fX19fX3wvCgo="

    def decode_message(encoded_message):
        # First, decode the message from base64
        decoded_bytes = base64.b64decode(encoded_message)
        # Then, decode the bytes from UTF-8
        decoded_message = decoded_bytes.decode('utf-8')
        return decoded_message

    decoded_message = decode_message(encoded_message)
    print(decoded_message)

if __name__ == '__main__':
    main()
    
# Answer: Suitcase
