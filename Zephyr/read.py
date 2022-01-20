
"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_streams


def main():
    # first resolve an EEG stream on the lab network
    print("looking for an EEG stream...")
    streams = resolve_streams()
    header = []
    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])
    info = inlet.info()
    ch = info.desc().child("channels").child("channel")
    for k in range(info.channel_count()):
        #print("  " + ch.child_value("label"))
        header.append(ch.child_value("label"))
        ch = ch.next_sibling()
    print(header)
    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        sample, timestamp = inlet.pull_sample()
        print(timestamp, sample)


if __name__ == '__main__':
    main()