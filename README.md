tombstones
==========

Python script to retrieve line info from an android tombstone using ndk-stack and addr2line

<pre>
run:

  $ python tombstones.py [args]

Options:
  -h, --help            show this help message and exit
  -n NDK, --ndk=NDK     NDK ROOT path to your NDK installation
  -t TOMB, --tomb=TOMB  path to the tombstone file
  -s SYM, --sym=SYM     SYM ROOT: path to sym file root dir (where the obfile
                        lies)
  -o OBFILE, --obfile=OBFILE
                        object file name (e.g. .so containing debug symbols)
  -g TARGET, --target=TARGET
                        android target architecture (armeabi armeabi-v7a ...)
  -a ADDR2LINE, --addr2line=ADDR2LINE
                        addr2line path w/o NDK path
  -v, --verbose         verbose output

</pre>
