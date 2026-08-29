#!/usr/bin/bash
# Run wayland compositor (KWin) and set WAYLAND_DISPLAY env variable

set -x

cat > $HOME/.xsessionrc <<'EOF'
export DESKTOP_SESSION=plasmawayland
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_TYPE=wayland
EOF

#kwriteconfig6 --file kscreenlockerrc --group Daemon --key Autolock false
#kwriteconfig6 --file kscreenlockerrc --group Daemon --key LockOnResume false
#kwriteconfig6 --file kscreenlockerrc --group Daemon --key Timeout 3600

if test -z "$DBUS_SESSION_BUS_ADDRESS" ; then
    eval `dbus-launch --sh-syntax`
fi

kwriteconfig6 --file kwalletrc --group "org.freedesktop.secrets" --key "apiEnabled" 2
kwriteconfig6 --file kwalletrc --group Wallet --key "Default Wallet" "kdewallet"
kwriteconfig6 --file kwalletrc --group Wallet --key "Enabled" true
kwalletd6 &
export KWALLETD_PID=$!
sleep 1

if [ -z "$XDG_RUNTIME_DIR" ]; then
  export XDG_RUNTIME_DIR=$HOME
fi

export WAYLAND_DISPLAY=firefox-pgo-wayland-0
if [ -S "$XDG_RUNTIME_DIR/$WAYLAND_DISPLAY" ]; then
  rm -f $XDG_RUNTIME_DIR/$WAYLAND_DISPLAY
  rm -f $XDG_RUNTIME_DIR/$WAYLAND_DISPLAY.lock
fi

echo "Launch kwin_wayland for $WAYLAND_DISPLAY"
kwin_wayland \
    --virtual \
    --width 1920 --height 1080 \
    --no-lockscreen \
    --socket=$WAYLAND_DISPLAY \
    & KWIN_PID=$!
export KWIN_PID
echo "KWin PID $KWIN_PID"

echo "Waiting for kwin_wayland to start..."
sleep 5
retry_count=0
max_retries=5
until [ $retry_count -gt $max_retries ]; do
  if [ -S "$XDG_RUNTIME_DIR/$WAYLAND_DISPLAY" ]; then
    retry_count=$(($max_retries + 1))
  else
    retry_count=$(($retry_count + 1))
    echo "Waiting for KWin, retry: $retry_count"
    sleep 2
  fi
done

if [ ! -S "$XDG_RUNTIME_DIR/$WAYLAND_DISPLAY" ]; then
  echo "KWin failed to start!"
  exit 1
fi

echo "KWin is running, $XDG_RUNTIME_DIR/$WAYLAND_DISPLAY is here."
