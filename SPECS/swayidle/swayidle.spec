# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           swayidle
Version:        1.9.0
Release:        %autorelease
Summary:        Idle management daemon for Wayland compositors
License:        MIT
URL:            https://github.com/swaywm/swayidle
VCS:            git:https://github.com/swaywm/swayidle.git
#!RemoteAsset:  sha256:6c1b769038b60250c88e47380cbb021cfa57a65f872bf4d6c340b5e3057096ac
Source0:        https://github.com/swaywm/swayidle/releases/download/v%{version}/swayidle-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dwerror=false
BuildOption(conf):  -Dman-pages=enabled
BuildOption(conf):  -Dlogind=enabled
BuildOption(conf):  -Dlogind-provider=systemd

%global fish_completions_dir %{_datadir}/fish/vendor_completions.d
%global zsh_completions_dir %{_datadir}/zsh/site-functions

BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.40
BuildRequires:  pkgconfig(wayland-scanner) >= 1.14.91
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  scdoc

%description
swayidle is an idle management daemon for Wayland compositors. It can run
commands when the user is idle, before sleep, or after resume.

%files
%doc README.md
%license LICENSE
%{_bindir}/swayidle
%{bash_completions_dir}/swayidle
%{fish_completions_dir}/swayidle.fish
%{zsh_completions_dir}/_swayidle
%{_mandir}/man1/swayidle.1*

%changelog
%autochangelog
