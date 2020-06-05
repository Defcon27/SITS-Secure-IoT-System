import hashlib

# Message hashing


def hashmsg(message):
    msg = message.encode()
    h = hashlib.new("sha256")
    h.update(msg)
    return h.hexdigest()


# # File hashing

# hasher = hashlib.new("sha256")

# SIZE = 65536
# with open('file.txt', 'r') as f:
#     data = f.read(SIZE).encode()
#     while len(data) > 0:
#         hasher.update(data)
#         data = f.read(SIZE).encode()

# print(hasher.hexdigest())
