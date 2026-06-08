# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           wiiuse
Version:        0.15.7
Release:        %autorelease
Summary:        WiiUse "feature complete" cross-platform Wii Remote access library
License:        GPL-3.0-or-later
URL:            https://github.com/wiiuse/wiiuse
#!RemoteAsset:  sha256:d16dbe3b38e3c1dbe3e9a2c5b0a32a801710da2aca66581500ef2b98eba1d8ff
Source:         https://github.com/wiiuse/wiiuse/archive/%{version}/wiiuse-%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  pkgconfig(bluez)

%description
Wiiuse is a library written in C that connects with several
Nintendo Wii remotes. Supports motion sensing, IR tracking,
nunchuk, classic controller, Balance Board, and the Guitar
Hero 3 controller. Single threaded and nonblocking makes
a light weight and clean API.

%package        devel
Summary:        Development files for %{name}
Requires:       pkgconfig(bluez)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a
rm -rf %{buildroot}%{_datadir}/doc/wiiuse

%files
%doc CHANGELOG.mkd README.mkd
%license LICENSE
%{_libdir}/libwiiuse.so.*

%files devel
%{_includedir}/wiiuse.h
%{_libdir}/libwiiuse.so
%{_bindir}/wiiuseexample
%{_libdir}/pkgconfig/wiiuse.pc

%changelog
%autochangelog
