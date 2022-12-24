#!/bin/sh

CHECK_INTERVAL="${CHECK_INTERVAL:-30}"
CHECK_TRIES="${CHECK_TRIES:-3}"
STUN_TIMEOUT="${STUN_TIMEOUT:-5}"
HOLDOFF="${HOLDOFF:-120}"
MYIP="${MYIP:-myip}"

check_internet() {
	for ((i=0; i<"$CHECK_TRIES"; i++)) do
		"$MYIP" -q 1 -t "$STUN_TIMEOUT"s >/dev/null 2>&1 && return 0
	done
	return 1
}

reconnect() {
	"$@"
}

while : ; do
	{
		check_internet && \
		sleep "$CHECK_INTERVAL"
	} || {
		reconnect "$@"
		sleep "$HOLDOFF"
	}
done
