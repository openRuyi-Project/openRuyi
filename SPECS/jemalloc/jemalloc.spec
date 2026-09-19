# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jemalloc
Version:        5.4.0
Release:        %autorelease
Summary:        general purpose malloc(3) implementation
License:        BSD-2-Clause
URL:            https://jemalloc.net/
VCS:            git:https://github.com/jemalloc/jemalloc
#!RemoteAsset:  sha256:200776fac271093e7c2f21edd6d62657ecd2be578d9328633f2a86bfa6ef4f1d
Source0:        https://github.com/jemalloc/jemalloc/releases/download/5.4.0/jemalloc-5.4.0.tar.bz2
BuildSystem:    autotools

# Use Zihintpause for CPU_SPINWAIT
Patch2000:      2000-fix-riscv-build-without-zihintpause.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

%description
jemalloc is a general purpose malloc(3) implementation that emphasizes fragmentation avoidance and scalable concurrency support.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing
applications that use %{name}.

%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
Static libraries for developing applications that use %{name}.

%conf -p
autoreconf -fiv

%files
%doc README VERSION
%doc %{_docdir}/jemalloc/jemalloc.html
%license COPYING
%{_bindir}/jemalloc.sh
%{_bindir}/jeprof
%{_libdir}/libjemalloc.so
%{_libdir}/libjemalloc.so.2

%files devel
%{_bindir}/jemalloc-config
%{_includedir}/jemalloc/jemalloc.h
%{_libdir}/pkgconfig/jemalloc.pc
%{_mandir}/man3/jemalloc.3*

%files static
%{_libdir}/libjemalloc.a
%{_libdir}/libjemalloc_pic.a

%changelog
%autochangelog
