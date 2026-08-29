# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           swaylock
Version:        1.8.5
Release:        %autorelease
Summary:        Screen locker for Wayland compositors
License:        MIT
URL:            https://github.com/swaywm/swaylock
VCS:            git:https://github.com/swaywm/swaylock.git
#!RemoteAsset:  sha256:ebd02c3c6a755d63102779c2c2430a4aab32d22bed0d73d6353974c1e5ad18a8
Source0:        https://github.com/swaywm/swaylock/releases/download/v%{version}/swaylock-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dwerror=false
BuildOption(conf):  -Dpam=enabled
BuildOption(conf):  -Dgdk-pixbuf=enabled
BuildOption(conf):  -Dman-pages=enabled

%global fish_completions_dir %{_datadir}/fish/vendor_completions.d
%global zsh_completions_dir %{_datadir}/zsh/site-functions

BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client) >= 1.20.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.25
BuildRequires:  pkgconfig(wayland-scanner) >= 1.15.0
BuildRequires:  pkgconfig(xkbcommon)

%description
swaylock is a screen locking utility for Wayland compositors implementing the
ext-session-lock-v1 Wayland protocol.

%files
%doc README.md
%license LICENSE
%config(noreplace) %{_sysconfdir}/pam.d/swaylock
%{_bindir}/swaylock
%{bash_completions_dir}/swaylock
%{fish_completions_dir}/swaylock.fish
%{zsh_completions_dir}/_swaylock
%{_mandir}/man1/swaylock.1*

%changelog
%autochangelog
