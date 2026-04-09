# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libssh2
Version:        1.11.1
Release:        %autorelease
Summary:        A library implementing the SSH2 protocol
License:        BSD-3-Clause
URL:            https://www.libssh2.org/
VCS:            git:https://github.com/libssh2/libssh2
#!RemoteAsset
Source:         https://libssh2.org/download/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --enable-shared
BuildOption(conf):  --disable-docker-tests
BuildOption(conf):  --disable-static
BuildOption(check):  -C tests

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  pkgconfig(zlib)
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  pkgconfig(openssl)
BuildRequires:  groff

%description
libssh2 is a library implementing the SSH2 protocol. It supports
authenticated key exchange, arbitrary channel communication, and a variety
of SFTP and SCP operations.

%package        devel
Summary:        Development files for libssh2
Requires:       pkgconfig
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libssh2-devel package contains libraries, header files, API documentation,
and examples for developing applications that use libssh2.

%install -a
make -C example clean
rm -rf example/.deps
find example/ -type f '(' -name '*.am' -o -name '*.in' ')' -delete
mv -v example example.%{_arch}

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
%{_libdir}/pkgconfig/libssh2.pc

%changelog
%autochangelog
