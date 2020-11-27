import sys

queue = []
result = []


def process_packet(buffer_size, packet):
    global queue, result

    while queue and queue[0][1] <= packet[0]:
        t = queue.pop(0)
        result[t[2]] = t[0]

    if len(queue) >= buffer_size:
        result[packet[2]] = -1
        return

    if queue:
        prev = queue[-1]
        packet[0] = prev[1]
    packet[1] = packet[0] + packet[1]
    queue.append(packet)


def process_queue_tail():
    global queue, result
    while queue:
        t = queue.pop(0)
        result[t[2]] = t[0]


def main():
    global result
    f = open(sys.argv[1], "r")
    reader = (tuple(map(int, line.split())) for line in f.readlines())
    buffer_size, packets_count = next(reader)

    if packets_count == 0:
        return

    result = [0] * packets_count
    for i in range(0, packets_count):
        process_packet(buffer_size, list(next(reader)) + [i])
    process_queue_tail()

    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
