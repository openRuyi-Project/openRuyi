# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:        libssh2
Version:     1.11.1
Release:     %autorelease
Summary:     A library implementing the SSH2 protocol
License:     BSD-3-Clause
URL:         https://www.libssh2.org/
#!RemoteAsset
Source:      https://libssh2.org/download/%{name}-%{version}.tar.gz
BuildSystem: autotools

BuildOption(conf): --disable-silent-rules
BuildOption(conf): --enable-shared
BuildOption(conf): --disable-docker-tests
BuildOption(conf): --disable-static

BuildRequires:  coreutils findutils zlib-devel
BuildRequires:  gcc make sed openssl-devel
BuildRequires:  groff

%description
libssh2 is a library implementing the SSH2 protocol. It supports
authenticated key exchange, arbitrary channel communication, and a variety
of SFTP and SCP operations.

%package    devel
Summary:    Development files for libssh2
Requires:   pkgconfig
Requires:   %{name} = %{version}

%description    devel
The libssh2-devel package contains libraries, header files, API documentation,
and examples for developing applications that use libssh2.

%install -a
make -C example clean
rm -rf example/.deps
find example/ -type f '(' -name '*.am' -o -name '*.in' ')' -delete
mv -v example example.%{_arch}

find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc docs/AUTHORS NEWS README RELEASE-NOTES
%{_libdir}/*.so.*

%files devel
%doc docs/BINDINGS.md docs/HACKING.md docs/TODO
%doc example.%{_arch}/
%{_mandir}/man3/libssh2_*.3*
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%{?autochangelog}
