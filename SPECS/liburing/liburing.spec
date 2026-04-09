# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           liburing
Version:        2.12
Release:        %autorelease
Summary:        High-performance async I/O library for the Linux kernel
License:        (GPL-2.0-only WITH Linux-syscall-note OR MIT) AND (LGPL-2.0-or-later OR MIT)
URL:            https://github.com/axboe/liburing
#!RemoteAsset
Source0:        https://brick.kernel.dk/snaps/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++

%description
liburing provides a simplified, high-level interface for applications to use
the powerful and efficient io_uring asynchronous I/O facility of the
Linux kernel. This package also includes a handy tool, 'io_uring_probe',
to check the features supported by the current system kernel.

%package        devel
Summary:        Development files for the io_uring library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, pkg-config files, and man pages
needed to develop applications using liburing.

%conf
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --libdevdir=%{_libdir} \
    --mandir=%{_mandir} \
    --includedir=%{_includedir} \
    --use-libc

%install -a
# Adhering to openRuyi's policy of preferring dynamic libraries.
rm -f %{buildroot}%{_libdir}/*.a
# Providing a value-add tool for developers.
install -Dm 755 test/probe.t %{buildroot}%{_bindir}/io_uring_probe

# Tests are dependent on kernel version and features
%check

%files
%license COPYING
%{_bindir}/io_uring_probe
%{_libdir}/liburing.so.*
%{_libdir}/liburing-ffi.so.*

%files devel
%doc README
%{_includedir}/liburing/
%{_includedir}/liburing.h
%{_libdir}/liburing.so
%{_libdir}/liburing-ffi.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man*/*

%changelog
%autochangelog
