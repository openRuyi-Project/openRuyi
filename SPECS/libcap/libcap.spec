# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test
%global buildvariables RAISE_SETFCAP=no prefix=%{_prefix} lib=%{_lib} SHARED=yes LIBDIR=%{_libdir} SBINDIR=%{_sbindir} PKGCONFIGDIR=%{_libdir}/pkgconfig/ INCDIR=%{_includedir} MANDIR=%{_mandir} SHARED=yes COPTS="%{optflags} %{_lto_cflags} -ffat-lto-objects"

Name:           libcap
Version:        2.76
Release:        %autorelease
Summary:        Library for Capabilities (linux-privs) Support
License:        BSD-3-Clause OR GPL-2.0-only
URL:            https://sites.google.com/site/fullycapable/
VCS:            git:https://git.kernel.org/pub/scm/libs/libcap/libcap.git
#!RemoteAsset:  sha256:629da4ab29900d0f7fcc36227073743119925fd711c99a1689bbf5c9b40c8e6f
Source:         https://mirrors.edge.kernel.org/pub/linux/libs/security/linux-privs/libcap2/%{name}-%{version}.tar.xz
#!RemoteAsset:  sha256:04ac58ad1cb220df031e17b8cc38ae550642b74ecb53b3c8ddfab95f97e54585
Source1:        https://mirrors.edge.kernel.org/pub/linux/libs/security/linux-privs/libcap2/%{name}-%{version}.tar.sign
#!RemoteAsset:  sha256:fe4c1f6257512f3b02ee175f736ce118b02d0ca5caad7e47933bb5c8f546d89a
Source2:        https://git.kernel.org/pub/scm/libs/libcap/libcap.git/plain/pgp.keys.asc#/%{name}.keyring
BuildSystem:    autotools

BuildOption(build):  %{buildvariables}
BuildOption(install):  %{buildvariables}

BuildRequires:  glibc-static
BuildRequires:  pkgconfig
BuildRequires:  binutils
BuildRequires:  pkgconfig(pam)

%description
Capabilities are a measure to limit the omnipotence of the superuser.
Currently a program started by root or setuid root has the power to do
anything. Capabilities (Linux-Privs) provide a more fine-grained access
control. Without kernel patches, you can use this library to drop
capabilities within setuid binaries. If you use patches, this can be
done automatically by the kernel.

%package        devel
Summary:        Development files for libcap
Requires:       glibc-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files (Headers, libraries for static linking, etc) for
libcap.

libcap is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.

Install libcap-devel if you want to develop or compile applications
using libcap.

%package        progs
Summary:        Libcap utility programs
Requires:       %{name} = %{version}-%{release}

%description    progs
This package contains utility programs handling capabilities via
libcap.

# No configure
%conf

%install -a
rm %{buildroot}%{_libdir}/libcap.a

%files
%license License
%{_libdir}/libcap.so.*
%{_libdir}/libpsx.so.2*
%{_libdir}/security/pam_cap.so

%files progs
%license License
%{_mandir}/man1/*
%{_mandir}/man8/*
%{_sbindir}/*

%files devel
%license License
%doc README CHANGELOG
%{_includedir}/sys/capability.h
%{_includedir}/sys/psx_syscall.h
%{_libdir}/*.so
%{_libdir}/libpsx.a
%{_libdir}/pkgconfig/libcap.pc
%{_libdir}/pkgconfig/libpsx.pc
%{_mandir}/man3/*.3%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}
%{_mandir}/man7/*.7*

%changelog
%{?autochangelog}
