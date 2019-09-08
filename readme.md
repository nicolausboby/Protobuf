# python proto3

1. protobuf library `pip install protobuf`
2. download and install [protoc](https://github.com/protocolbuffers/protobuf/releases/tag/v3.9.1), unzip, add protoc/bin to environment path
3. compile .proto `protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/AddressBook.proto`