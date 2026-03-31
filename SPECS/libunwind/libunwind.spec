# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libunwind
Version:        1.8.3
Release:        %autorelease
Summary:        An unwinding library
License:        MIT
URL:            https://www.nongnu.org/libunwind/
VCS:            git:https://github.com/libunwind/libunwind
#!RemoteAsset
Source:         https://github.com/libunwind/libunwind/archive/refs/tags/v%{version}.tar.gz
Patch0000:      0001-Fix-bad-prototype-for-malloc-in-test.patch
# This patch is from fedora.
Patch3000:      3000-libunwind-no-dl-iterate-phdr.patch
BuildSystem:    autotools

BuildOption(conf):  --enable-shared
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-documentation

BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)

%description
Libunwind provides a C ABI to determine the call-chain of a program.

%package        devel
Summary:        Development files for libunwind
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the libraries, header files, and documentation
needed for developing applications that use libunwind.

%conf -p
autoreconf -fiv

%install -a
# Remove test files.
rm -rf %{buildroot}%{_libexecdir}

%files
%license COPYING
%doc README NEWS
%{_libdir}/libunwind*.so.*

%files devel
%{_libdir}/libunwind*.so
%{_libdir}/pkgconfig/libunwind-coredump.pc
%{_libdir}/pkgconfig/libunwind-generic.pc
%{_libdir}/pkgconfig/libunwind-ptrace.pc
%{_libdir}/pkgconfig/libunwind-setjmp.pc
%{_libdir}/pkgconfig/libunwind.pc
%{_includedir}/unwind.h
%{_includedir}/libunwind*.h

%changelog
%{?autochangelog}
