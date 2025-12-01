# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define libname libdwarves

Name:          dwarves
Version:       1.30
Release:       %autorelease
Summary:       Debugging Information Manipulation Tools (pahole & friends)
License:       GPL-2.0-only
URL:           https://git.kernel.org/pub/scm/devel/pahole/pahole.git
#!RemoteAsset
Source0:       https://fedorapeople.org/~acme/%{name}/%{name}-%{version}.tar.xz

BuildSystem:   cmake

BuildOption(conf): -DCMAKE_INSTALL_PREFIX=%{_prefix}
BuildOption(conf): -DLIBBPF_EMBEDDED=OFF
BuildOption(conf): -DCMAKE_BUILD_TYPE=Release

BuildRequires: make, gcc-c++, cmake
BuildRequires: zlib-devel, libelf-devel, libdw-devel
BuildRequires: python3-devel, openssl-devel
# For modern builds, it's good to have libbpf support.
BuildRequires: pkgconfig(libbpf)

%description
This package contains the core dwarves toolset, including pahole, codiff,
pfunct, and their associated documentation and data files.

Provides:      pahole = %{version}-%{release}

%package devel
Summary:       Development files for the libdwarves library
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development libraries for
compiling applications that use the libdwarves API.

%package -n ostra-cg
Summary:       Generate call graphs from encoded traces
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description -n ostra-cg
The ostra-cg tool can be used to generate call graphs from traces
encoded by pahole.

%install -p
rm -Rf %{buildroot}

%files
%license COPYING
%doc README NEWS
# Core libraries
%{_libdir}/%{libname}.so.*
%{_libdir}/%{libname}_emit.so.*
%{_libdir}/%{libname}_reorganize.so.*
# Core CLI tools
%{_bindir}/btfdiff
%{_bindir}/codiff
%{_bindir}/ctracer
%{_bindir}/dtagnames
%{_bindir}/fullcircle
%{_bindir}/pahole
%{_bindir}/pdwtags
%{_bindir}/pfunct
%{_bindir}/pglobal
%{_bindir}/prefcnt
%{_bindir}/scncopy
%{_bindir}/syscse
# Man pages for the core tools
%{_mandir}/man1/*
# Exclude files that belong to the ostra-cg subpackage.
%exclude %{_bindir}/ostra-cg

%files devel
%{_includedir}/dwarves/*.h
# Development symlinks
%{_libdir}/%{libname}.so
%{_libdir}/%{libname}_emit.so
%{_libdir}/%{libname}_reorganize.so

%files -n ostra-cg
%{_bindir}/ostra-cg
%dir %{_datadir}/dwarves/
%dir %{_datadir}/dwarves/runtime/
%dir %{_datadir}/dwarves/runtime/python/
%defattr(0644,root,root,0755)
%{_datadir}/dwarves/runtime/Makefile
%{_datadir}/dwarves/runtime/linux.blacklist.cu
%{_datadir}/dwarves/runtime/ctracer_relay.c
%{_datadir}/dwarves/runtime/ctracer_relay.h
%attr(0755,root,root) %{_datadir}/dwarves/runtime/python/ostra.py*

%changelog
%{?autochangelog}
