# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# By default, build the optional Python bindings.
%bcond python 1

Name:           libseccomp
Version:        2.6.0
Release:        %autorelease
Summary:        Enhanced library for the Linux syscall filtering mechanism
License:        LGPL-2.1-only
URL:            https://github.com/seccomp/libseccomp
#!RemoteAsset
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

Patch0:         make-python-build.patch
Patch1:         fix-murmur-hash-strict-aliasing-violation.patch

BuildOption(conf):  --disable-static
%if %{with python}
BuildOption(conf):  --enable-python
%else
BuildOption(conf):  --disable-python
%endif
BuildOption(check):  LIBSECCOMP_TSTCFG_JOBS=0
BuildOption(check):  LIBSECCOMP_TSTCFG_TYPE=live
BuildOption(check):  LIBSECCOMP_TSTCFG_MODE_LIST=c
BuildOption(check):  LIBSECCOMP_TSTCFG_ARCH_LIST=native
BuildOption(check):  LIBSECCOMP_TSTCFG_LOG_LEVEL=2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  gperf
%if %{with python}
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools
BuildRequires:  cython
%endif

%description
The libseccomp library provides an easy-to-use interface to the Linux
kernel seccomp syscall filtering mechanism. It is a fundamental building
block for creating secure, sandboxed applications and containers.

%if %{with python}
%package     -n python-%{name}
Summary:        Python bindings for the libseccomp library
Provides:       python3-%{name}
%python_provide python3-%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-%{name}
This package provides the Python 3 bindings for libseccomp, allowing Python
applications to create and manage seccomp filters.
%endif

%package        devel
Summary:        Development files for libseccomp
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files, pkg-config files, and documentation for developing applications
that link against libseccomp.

%conf -p
autoreconf -fiv

%install -a
rm -f %{buildroot}%{_libdir}/libseccomp.la

%files
%license LICENSE
%doc README.md CHANGELOG
%{_libdir}/libseccomp.so.*

%if %{with python}
%files -n python-libseccomp
%{python3_sitearch}/*
%endif

%files devel
%doc CREDITS CONTRIBUTING.md src/syscalls.csv
%{_bindir}/scmp_sys_resolver
%{_includedir}/seccomp.h
%{_includedir}/seccomp-syscalls.h
%{_libdir}/libseccomp.so
%{_libdir}/pkgconfig/libseccomp.pc
%{_mandir}/man1/scmp_sys_resolver.1*
%{_mandir}/man3/*

%changelog
%autochangelog
