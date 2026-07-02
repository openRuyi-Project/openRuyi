# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sway
Version:        1.12
Release:        %autorelease
Summary:        i3-compatible Wayland compositor
License:        MIT
URL:            https://github.com/swaywm/sway
VCS:            git:https://github.com/swaywm/sway.git
#!RemoteAsset:  sha256:a7b1becc217433c11c6284d36bcea0687b87b77b0ed26a384565292ec321f2b1
Source0:        https://github.com/swaywm/sway/releases/download/%{version}/sway-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dwerror=false
BuildOption(conf):  -Dman-pages=enabled
BuildOption(conf):  -Dtray=enabled
BuildOption(conf):  -Dsd-bus-provider=libsystemd
BuildOption(conf):  -Dgdk-pixbuf=enabled

BuildRequires:  meson >= 1.3
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(json-c) >= 0.13
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput) >= 1.26.0
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libsystemd) >= 239
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc) >= 1.9.2
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server) >= 1.21.0
BuildRequires:  pkgconfig(wlroots-0.20) >= 0.20.0
BuildRequires:  pkgconfig(xkbcommon) >= 1.5.0

Requires:       xkeyboard-config
Recommends:     foot
Recommends:     pipewire
Recommends:     swaybg
Recommends:     xdg-desktop-portal-wlr

%description
Sway is an i3-compatible Wayland compositor.

%install -a
install -d %{buildroot}%{_sysconfdir}/sway/config.d

%files
%doc README.md
%license LICENSE assets/LICENSE
%dir %{_sysconfdir}/sway
%dir %{_sysconfdir}/sway/config.d
%config(noreplace) %{_sysconfdir}/sway/config
%{_bindir}/sway
%{_bindir}/swaybar
%{_bindir}/swaymsg
%{_bindir}/swaynag
%{_datadir}/backgrounds/sway/
%{bash_completions_dir}/sway
%{bash_completions_dir}/swaybar
%{bash_completions_dir}/swaymsg
%{fish_completions_dir}/sway.fish
%{fish_completions_dir}/swaymsg.fish
%{fish_completions_dir}/swaynag.fish
%{_datadir}/wayland-sessions/sway.desktop
%{zsh_completions_dir}/_sway
%{zsh_completions_dir}/_swaymsg
%{_mandir}/man1/sway.1*
%{_mandir}/man1/swaymsg.1*
%{_mandir}/man1/swaynag.1*
%{_mandir}/man5/sway.5*
%{_mandir}/man5/sway-bar.5*
%{_mandir}/man5/sway-input.5*
%{_mandir}/man5/sway-output.5*
%{_mandir}/man5/swaynag.5*
%{_mandir}/man7/sway-ipc.7*
%{_mandir}/man7/swaybar-protocol.7*

%changelog
%autochangelog
