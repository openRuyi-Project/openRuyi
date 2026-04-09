# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libaio
Version:        0.3.113
Release:        %autorelease
Summary:        Linux-Native Asynchronous I/O Access Library
License:        LGPL-2.1-or-later
URL:            https://pagure.io/libaio
VCS:            git:https://pagure.io/libaio.git
#!RemoteAsset
Source0:        https://releases.pagure.org/libaio/libaio-%{version}.tar.gz

# test failing for multilib
Patch0:         libaio-fix-test-off64_t.patch

BuildSystem:    autotools

BuildOption(install):  libdir=%{_libdir}

BuildRequires:  gcc
BuildRequires:  make

%description
The Linux-native asynchronous I/O (AIO) facility has a richer API and
capability set than the POSIX AIO facility. This library provides the
Linux-native API for AIO.

%package        devel
Summary:        Development Files for Linux-native Asynchronous I/O Access
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides the header files and libraries needed to develop
applications using the Linux-native asynchronous I/O facility.

# No conf
%conf

%install -a
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/libaio.pc << EOF
prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: libaio
Description: Linux-native asynchronous I/O access library
Version: %{version}
Libs: -laio
Cflags: -I\${includedir}
EOF

rm %{buildroot}%{_libdir}/*.a
mkdir -p %{buildroot}%{_mandir}/man3
install -p -m 0644 man/*.3 %{buildroot}%{_mandir}/man3/

# qemu-linux-user does not emulate io_setup syscall, so none of the testsuite makes sense
%check

%files
%license COPYING
%{_libdir}/libaio.so.1
%{_libdir}/libaio.so.1.*

%files devel
%doc TODO
%{_includedir}/libaio.h
%{_libdir}/libaio.so
%{_libdir}/pkgconfig/libaio.pc
%{_mandir}/man3/*

%changelog
%autochangelog
