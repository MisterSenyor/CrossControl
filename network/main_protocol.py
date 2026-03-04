HEADER_SIZES = {
    "src": 32,
    "dst": 32,
    "proto": 16,
}
TERMINATOR = b"\x00\xff\x00\xffEND\xff\x00\xff\x00"
HEADER_SIZE_TOTAL = sum(HEADER_SIZES.values())


def decode_padded_field(raw_bytes):
    return raw_bytes.rstrip(b"\x00").decode("utf-8")

def parse_header(header_bytes):
    offset = 0

    src = decode_padded_field(
        header_bytes[offset:offset + HEADER_SIZES["src"]]
    )
    offset += HEADER_SIZES["src"]

    dst = decode_padded_field(
        header_bytes[offset:offset + HEADER_SIZES["dst"]]
    )
    offset += HEADER_SIZES["dst"]

    prot = decode_padded_field(
        header_bytes[offset:offset + HEADER_SIZES["proto"]]
    )

    return src, dst, prot