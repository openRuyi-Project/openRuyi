# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ydotool
Version:        1.0.4
Release:        %autorelease
Summary:        Generic Linux command-line input automation tool
License:        AGPL-3.0-or-later AND CC0-1.0
URL:            https://github.com/ReimuNotMoe/ydotool
#!RemoteAsset:  sha256:ba075a43aa6ead51940e892ecffa4d0b8b40c241e4e2bc4bd9bd26b61fde23bd
Source0:        https://github.com/ReimuNotMoe/ydotool/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        README.openRuyi
Source2:        70-ydotool-uinput.rules
BuildSystem:    cmake

# Set the release version without requiring Git metadata in source archives.
Patch2000:      2000-allow-setting-the-version-without-Git-metadata.patch

# Upstream declares CMake 3.4 compatibility, which CMake 4 no longer supports.
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
BuildOption(conf):  -DYDOTOOL_VERSION=%{version}

BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
BuildRequires:  scdoc
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemd-udev

# The upstream user service invokes this command for ExecReload.
Requires:       %{_bindir}/kill
# kmod-static-nodes.service prepares the uinput node for module autoloading.
Requires:       kmod
Requires:       systemd
Requires:       systemd-udev

%description
ydotool simulates keyboard and mouse input through the Linux uinput
interface. It works with Wayland, X11, and text consoles without depending
on a display server protocol. The ydotoold daemon maintains the virtual
input device and accepts commands from the ydotool client.

%install -a
install -m 0644 %{SOURCE1} README.openRuyi
install -D -m 0644 %{SOURCE2} %{buildroot}%{_udevrulesdir}/70-ydotool-uinput.rules

%check
%{_bindir}/udevadm verify %{SOURCE2}
# Input injection needs /dev/uinput and a target session; check CLI startup here.
%{__cmake_builddir}/ydotool --help
test "$(%{__cmake_builddir}/ydotoold --version)" = '%{version}'
%{__cmake_builddir}/ydotoold --help

%post
%systemd_user_post ydotool.service

%preun
%systemd_user_preun ydotool.service

%postun
%systemd_user_postun_with_restart ydotool.service

%files
%doc README.md README.openRuyi
%license LICENSE
%{_bindir}/ydotool
%{_bindir}/ydotoold
%{_mandir}/man1/ydotool.1*
%{_mandir}/man8/ydotoold.8*
%{_udevrulesdir}/70-ydotool-uinput.rules
%{_userunitdir}/ydotool.service

%changelog
%autochangelog
