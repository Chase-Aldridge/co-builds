#!/usr/bin/env python3
import base64

def main():
    # The string to be encoded
    data = "trWxO1TTBCD7jvQe1iqhg:YmWHDHI2Lyv977vRfJJsdjsw1rfBl"

    # Encode the string in base64. The string is first encoded to bytes using UTF-8.
    encoded_bytes = base64.b64encode(data.encode("utf-8"))

    # Convert the base64 bytes back into a string and print it.
    encoded_str = encoded_bytes.decode("utf-8")
    print(encoded_str)

if __name__ == "__main__":
    main()
