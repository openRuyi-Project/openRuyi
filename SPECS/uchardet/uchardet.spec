# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           uchardet
Version:        0.0.8
Release:        %autorelease
Summary:        uchardet is an encoding detector library
License:        MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.0-or-later
URL:            https://www.freedesktop.org/wiki/Software/uchardet/
VCS:            git:https://gitlab.freedesktop.org/uchardet/uchardet
#!RemoteAsset:  sha256:e97a60cfc00a1c147a674b097bb1422abd9fa78a2d9ce3f3fdcc2e78a34ac5f0
Source:         https://www.freedesktop.org/software/uchardet/releases/uchardet-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
BuildOption(conf):  -DBUILD_STATIC=OFF

BuildRequires:  cmake

%description
uchardet is an encoding detector library,
which takes a sequence of bytes in an unknown character encoding without any additional information,
and attempts to determine the encoding of the text. Returned encoding names are iconv-compatible.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/uchardet
%{_libdir}/libuchardet.so.*
%{_mandir}/man1/uchardet.1*

%files devel
%{_includedir}/uchardet/
%{_libdir}/cmake/uchardet
%{_libdir}/libuchardet.so
%{_libdir}/pkgconfig/uchardet.pc

%changelog
%autochangelog
