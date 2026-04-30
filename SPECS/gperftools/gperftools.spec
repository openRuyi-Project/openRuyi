# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gperftools
Version:        2.18.1
Release:        %autorelease
Summary:        Very fast malloc and performance analysis tools
License:        BSD-3-Clause
URL:            https://github.com/gperftools/gperftools
#!RemoteAsset:  sha256:d18d919175f9e4d740ace6b52f0f4f91284160c454e91b36ffd6456282a02206
Source:         %{url}/releases/download/gperftools-%{version}/gperftools-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-libunwind

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libunwind)

%description
gperftools is a collection of a high-performance multi-threaded malloc()
implementation (tcmalloc), plus heap-checker, heap-profiler, and
cpu-profiler libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, shared library symlinks and
pkg-config files needed to develop applications that link against
%{name}.

%conf -p
autoreconf -fiv

%install -a
# Drop upstream noise: generic INSTALL, Windows-only README, old changelog.
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL
rm -f %{buildroot}%{_docdir}/%{name}/README_windows.txt
rm -f %{buildroot}%{_docdir}/%{name}/ChangeLog.old

%files
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/NEWS
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/*.adoc
%doc %{_docdir}/%{name}/*.dot
%doc %{_docdir}/%{name}/*.gif
%doc %{_docdir}/%{name}/*.png
%license %{_docdir}/%{name}/COPYING
%{_libdir}/libprofiler.so.*
%{_libdir}/libtcmalloc.so.*
%{_libdir}/libtcmalloc_and_profiler.so.*
%{_libdir}/libtcmalloc_debug.so.*
%{_libdir}/libtcmalloc_minimal.so.*
%{_libdir}/libtcmalloc_minimal_debug.so.*

%files devel
%{_includedir}/gperftools/
%{_libdir}/libprofiler.so
%{_libdir}/libtcmalloc.so
%{_libdir}/libtcmalloc_and_profiler.so
%{_libdir}/libtcmalloc_debug.so
%{_libdir}/libtcmalloc_minimal.so
%{_libdir}/libtcmalloc_minimal_debug.so
%{_libdir}/pkgconfig/libprofiler.pc
%{_libdir}/pkgconfig/libtcmalloc.pc
%{_libdir}/pkgconfig/libtcmalloc_debug.pc
%{_libdir}/pkgconfig/libtcmalloc_minimal.pc
%{_libdir}/pkgconfig/libtcmalloc_minimal_debug.pc

%changelog
%autochangelog
