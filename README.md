tombstones
==========

Python script to retrieve line info from an android tombstone using ndk-stack and addr2line

run:

$ python tombstones.py [args]

args:
  -h, --help            show this help message and exit
  -n NDK, --ndk=NDK     NDK ROOT
  -t TOMB, --tomb=TOMB  tombstone file
  -s SYM, --sym=SYM     SYM ROOT
  -o OBFILE, --obfile=OBFILE
                        obfile file (.so)
  -g TARGET, --target=TARGET
                        target architecture
  -a ADDR2LINE, --addr2line=ADDR2LINE
                        addr2line path

