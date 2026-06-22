# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           niri
Version:        26.04
Release:        %autorelease
Summary:        Scrollable-tiling Wayland compositor
License:        GPL-3.0-or-later
URL:            https://niri-wm.github.io/niri/
VCS:            git:https://github.com/niri-wm/niri.git
#!RemoteAsset:  sha256:134c602d8e0d53413a52d6cd58f9ce7e79a07d03288ee0a51ba1abd5db1b1ad9
Source0:        https://github.com/niri-wm/niri/archive/refs/tags/v%{version}.tar.gz
#!RemoteAsset:  sha256:2df0f01fd83ee01dc2fcd5976ac0004334b03ef567f467b6c511f11fc1c8a7b9
Source1:        https://github.com/Smithay/smithay/archive/ff5fa7df392cecfba049ffed55cdaa4e98a8e7ef/smithay-ff5fa7df392cecfba049ffed55cdaa4e98a8e7ef.tar.gz
BuildSystem:    rust

# Use the packaged Smithay sources for offline builds and keep them outside the niri workspace.
Patch2000:      2000-fix-git-dep.patch

BuildOption(build):  --features default

BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig
BuildRequires:  bash-completion
BuildRequires:  clang
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  crate(accesskit-0.21/default) >= 0.21.1
BuildRequires:  crate(diff-0.1) >= 0.1
BuildRequires:  crate(insta-1/console) >= 1.0
BuildRequires:  crate(schemars-1/schemars-derive) >= 1.2
BuildRequires:  crate(approx-0.5) >= 0.5
BuildRequires:  crate(proptest-1/default) >= 1.11
BuildRequires:  crate(rayon-1) >= 1.12
BuildRequires:  crate(xshell-0.2) >= 0.2.7
BuildRequires:  crate(proptest-derive-0.8/boxed-union) >= 0.8
BuildRequires:  crate(calloop-wayland-source-0.4) >= 0.4
BuildRequires:  crate(pretty-assertions-1) >= 1.0
BuildRequires:  crate(accesskit-unix-0.17/default) >= 0.17.2
BuildRequires:  crate(aliasable-0.1/default) >= 0.1.3
BuildRequires:  crate(anyhow-1/default) >= 1.0.102
BuildRequires:  crate(appendlist-1/default) >= 1.4.0
BuildRequires:  crate(arrayvec-0.7/default) >= 0.7.6
BuildRequires:  crate(async-channel-2/default) >= 2.5.0
BuildRequires:  crate(async-io-2/default) >= 2.6.0
BuildRequires:  crate(atomic-0.6/default) >= 0.6.1
BuildRequires:  crate(atomic-float-1/default) >= 1.1.0
BuildRequires:  crate(bitflags-2/default) >= 2.13.0
BuildRequires:  crate(bytemuck-1/default) >= 1.25.0
BuildRequires:  crate(bytemuck-1/derive) >= 1.25.0
BuildRequires:  crate(calloop-0.14/default) >= 0.14.4
BuildRequires:  crate(calloop-0.14/executor) >= 0.14.4
BuildRequires:  crate(calloop-0.14/futures-io) >= 0.14.4
BuildRequires:  crate(calloop-0.14/signals) >= 0.14.4
BuildRequires:  crate(cc-1/default) >= 1.2.63
BuildRequires:  crate(cgmath-0.18/default) >= 0.18.0
BuildRequires:  crate(clap-4/default) >= 4.6.1
BuildRequires:  crate(clap-4/derive) >= 4.6.1
BuildRequires:  crate(clap-4/string) >= 4.6.1
BuildRequires:  crate(clap-complete-4/default) >= 4.6.3
BuildRequires:  crate(clap-complete-nushell-4/default) >= 4.6.0
BuildRequires:  crate(csscolorparser-0.8/default) >= 0.8.3
BuildRequires:  crate(cursor-icon-1/default) >= 1.2.0
BuildRequires:  crate(directories-6/default) >= 6.0.0
BuildRequires:  crate(downcast-rs-1/default) >= 1.2.1
BuildRequires:  crate(drm-0.14/default) >= 0.14.1
BuildRequires:  crate(drm-ffi-0.9/default) >= 0.9.1
BuildRequires:  crate(drm-fourcc-2/default) >= 2.2.0
BuildRequires:  crate(errno-0.3/default) >= 0.3.14
BuildRequires:  crate(fastrand-2/default) >= 2.4.1
BuildRequires:  crate(futures-util-0.3/io) >= 0.3.32
BuildRequires:  crate(futures-util-0.3/std) >= 0.3.32
BuildRequires:  crate(gbm-0.18/drm-support) >= 0.18.0
BuildRequires:  crate(gbm-0.18/import-wayland) >= 0.18.0
BuildRequires:  crate(git-version-0.3/default) >= 0.3.9
BuildRequires:  crate(gl-generator-0.14/default) >= 0.14.0
BuildRequires:  crate(glam-0.32/default) >= 0.32.1
BuildRequires:  crate(gtk4-0.10/default) >= 0.10.3
BuildRequires:  crate(gtk4-0.10/v4-12) >= 0.10.3
BuildRequires:  crate(indexmap-2/default) >= 2.14.0
BuildRequires:  crate(input-0.10/default) >= 0.10.0
BuildRequires:  crate(input-0.10/libinput-1-19) >= 0.10.0
BuildRequires:  crate(input-0.10/libinput-1-21) >= 0.10.0
BuildRequires:  crate(input-0.10/udev) >= 0.10.0
BuildRequires:  crate(keyframe-1) >= 1.1.1
BuildRequires:  crate(knuffel-3/default) >= 3.2.0
BuildRequires:  crate(libadwaita-0.8/default) >= 0.8.1
BuildRequires:  crate(libadwaita-0.8/v1-4) >= 0.8.1
BuildRequires:  crate(libc-0.2/default) >= 0.2.186
BuildRequires:  crate(libdisplay-info-0.3/default) >= 0.3.0
BuildRequires:  crate(libloading-0.8/default) >= 0.8.9
BuildRequires:  crate(libseat-0.2) >= 0.2.4
BuildRequires:  crate(log-0.4/default) >= 0.4.30
BuildRequires:  crate(log-0.4/max-level-trace) >= 0.4.30
BuildRequires:  crate(log-0.4/release-max-level-debug) >= 0.4.30
BuildRequires:  crate(miette-5/default) >= 5.10.0
BuildRequires:  crate(miette-5/fancy-no-backtrace) >= 5.10.0
BuildRequires:  crate(ordered-float-5/default) >= 5.3.0
BuildRequires:  crate(pango-0.21/default) >= 0.21.5
BuildRequires:  crate(pango-0.21/v1-44) >= 0.21.5
BuildRequires:  crate(pangocairo-0.21/default) >= 0.21.5
BuildRequires:  crate(pipewire-0.9/default) >= 0.9.2
BuildRequires:  crate(pipewire-0.9/v0-3-33) >= 0.9.2
BuildRequires:  crate(pixman-0.2/default) >= 0.2.1
BuildRequires:  crate(pixman-0.2/drm-fourcc) >= 0.2.1
BuildRequires:  crate(pixman-0.2/sync) >= 0.2.1
BuildRequires:  crate(pkg-config-0.3/default) >= 0.3.33
BuildRequires:  crate(png-0.18/default) >= 0.18.1
BuildRequires:  crate(profiling-1/default) >= 1.0.18
BuildRequires:  crate(rand-0.9/default) >= 0.9.4
BuildRequires:  crate(regex-1/default) >= 1.12.3
BuildRequires:  crate(rustix-1/default) >= 1.1.4
BuildRequires:  crate(rustix-1/event) >= 1.1.4
BuildRequires:  crate(rustix-1/fs) >= 1.1.4
BuildRequires:  crate(rustix-1/mm) >= 1.1.4
BuildRequires:  crate(rustix-1/net) >= 1.1.4
BuildRequires:  crate(rustix-1/pipe) >= 1.1.4
BuildRequires:  crate(rustix-1/process) >= 1.1.4
BuildRequires:  crate(rustix-1/shm) >= 1.1.4
BuildRequires:  crate(rustix-1/time) >= 1.1.4
BuildRequires:  crate(sd-notify-0.5/default) >= 0.5.0
BuildRequires:  crate(serde-1/default) >= 1.0.228
BuildRequires:  crate(serde-1/derive) >= 1.0.228
BuildRequires:  crate(serde-json-1/default) >= 1.0.150
BuildRequires:  crate(sha2-0.10/default) >= 0.10.9
BuildRequires:  crate(smallvec-1/default) >= 1.15.1
BuildRequires:  crate(tempfile-3/default) >= 3.27.0
BuildRequires:  crate(thiserror-2/default) >= 2.0.18
BuildRequires:  crate(tracing-0.1/default) >= 0.1.44
BuildRequires:  crate(tracing-0.1/max-level-trace) >= 0.1.44
BuildRequires:  crate(tracing-0.1/release-max-level-debug) >= 0.1.44
BuildRequires:  crate(tracing-subscriber-0.3/default) >= 0.3.23
BuildRequires:  crate(tracing-subscriber-0.3/env-filter) >= 0.3.23
BuildRequires:  crate(tracy-client-0.18) >= 0.18.4
BuildRequires:  crate(udev-0.9/default) >= 0.9.3
BuildRequires:  crate(wayland-backend-0.3/default) >= 0.3.15
BuildRequires:  crate(wayland-backend-0.3/server-system) >= 0.3.15
BuildRequires:  crate(wayland-client-0.31/default) >= 0.31.14
BuildRequires:  crate(wayland-cursor-0.31/default) >= 0.31.14
BuildRequires:  crate(wayland-egl-0.32/default) >= 0.32.11
BuildRequires:  crate(wayland-protocols-0.32/default) >= 0.32.12
BuildRequires:  crate(wayland-protocols-0.32/server) >= 0.32.12
BuildRequires:  crate(wayland-protocols-0.32/staging) >= 0.32.12
BuildRequires:  crate(wayland-protocols-0.32/unstable) >= 0.32.12
BuildRequires:  crate(wayland-protocols-misc-0.3/default) >= 0.3.12
BuildRequires:  crate(wayland-protocols-misc-0.3/server) >= 0.3.12
BuildRequires:  crate(wayland-protocols-wlr-0.3/default) >= 0.3.12
BuildRequires:  crate(wayland-protocols-wlr-0.3/server) >= 0.3.12
BuildRequires:  crate(wayland-scanner-0.31/default) >= 0.31.10
BuildRequires:  crate(wayland-server-0.31/default) >= 0.31.13
BuildRequires:  crate(wayland-sys-0.31/default) >= 0.31.11
BuildRequires:  crate(winit-0.30/rwh-06) >= 0.30.13
BuildRequires:  crate(winit-0.30/wayland) >= 0.30.13
BuildRequires:  crate(winit-0.30/wayland-dlopen) >= 0.30.13
BuildRequires:  crate(winit-0.30/x11) >= 0.30.13
BuildRequires:  crate(xcursor-0.3/default) >= 0.3.10
BuildRequires:  crate(xkbcommon-0.9/default) >= 0.9.0
BuildRequires:  crate(xkbcommon-0.9/wayland) >= 0.9.0
BuildRequires:  crate(zbus-5/default) >= 5.15.0

Requires:       wayland
Requires:       xkeyboard-config

# required for portal support
# Recommends:     gnome-keyring
# Recommends:     xdg-desktop-portal-gnome
# Recommends:     xdg-desktop-portal-gtk

# applications bound by keyboard shortcuts in default configuration
# Recommends:     alacritty
# Recommends:     swaylock

%description
niri is a scrollable-tiling Wayland compositor. Windows are arranged in
columns on an infinite strip that extends horizontally.

%prep -a
tar xf %{SOURCE1}
rm -rf Cargo.lock

%build -a
target/release/niri completions bash > niri.bash
target/release/niri completions fish > niri.fish
target/release/niri completions zsh > _niri

%install
install -Dm0755 target/release/niri %{buildroot}%{_bindir}/niri
install -Dm0755 resources/niri-session %{buildroot}%{_bindir}/niri-session
install -Dm0644 resources/niri.desktop %{buildroot}%{_datadir}/wayland-sessions/niri.desktop
install -Dm0644 resources/niri-portals.conf %{buildroot}%{_datadir}/xdg-desktop-portal/niri-portals.conf
install -Dm0644 resources/niri.service %{buildroot}%{_userunitdir}/niri.service
install -Dm0644 resources/niri-shutdown.target %{buildroot}%{_userunitdir}/niri-shutdown.target

install -Dm0644 niri.bash %{buildroot}%{bash_completions_dir}/niri
install -Dm0644 niri.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/niri.fish
install -Dm0644 _niri %{buildroot}%{_datadir}/zsh/site-functions/_niri

%check
# limit test parallelism
export RAYON_NUM_THREADS=1
# skip tests that require a running session or EGL display
check_args=(--test-threads 1 --skip ::egl)
%ifarch riscv64
check_args+=(--skip tests::window_opening::target_output_and_workspaces)
%endif
cargo test --locked --offline --workspace --exclude niri-visual-tests --features default --jobs 1 -- "${check_args[@]}"

%post
%systemd_user_post niri.service

%preun
%systemd_user_preun niri.service

%files
%doc README.md
%license LICENSE
%{_bindir}/niri
%{_bindir}/niri-session
%{_datadir}/wayland-sessions/niri.desktop
%{_datadir}/xdg-desktop-portal/niri-portals.conf
%{_userunitdir}/niri.service
%{_userunitdir}/niri-shutdown.target
%{bash_completions_dir}/niri
%{_datadir}/fish/vendor_completions.d/niri.fish
%{_datadir}/zsh/site-functions/_niri

%changelog
%autochangelog
