# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           minizip-ng
Version:        4.1.0
Release:        %autorelease
Summary:        Minizip library with latest bug fixes and advanced features
License:        Zlib
URL:            https://github.com/zlib-ng/minizip-ng
VCS:            git:https://github.com/zlib-ng/minizip-ng
#!RemoteAsset
Source0:        https://github.com/zlib-ng/minizip-ng/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DMZ_BUILD_TESTS:BOOL=ON
BuildOption(conf):  -DMZ_COMPAT:BOOL=ON
BuildOption(conf):  -DMZ_FORCE_FETCH_LIBS:BOOL=OFF
BuildOption(conf):  -DSKIP_INSTALL_BINARIES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
Minizip-ng is a zip manipulation library derived from zlib's minizip project.
It provides modernized APIs and additional features including AES support.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license LICENSE
%doc README.md
%{_libdir}/libminizip.so.*

%files devel
%{_includedir}/minizip/
%{_libdir}/libminizip.so
%{_libdir}/pkgconfig/minizip.pc
%{_libdir}/cmake/minizip/

%changelog
%autochangelog
