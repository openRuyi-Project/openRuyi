# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Parallel compilation of this package will fail.
%global _smp_mflags -j1

Name:           libffcall
Version:        2.5
Release:        %autorelease
Summary:        Foreign function calls from interpreters
License:        GPL-2.0-or-later
URL:            https://www.gnu.org/software/libffcall/
#!RemoteAsset
Source:         https://ftpmirror.gnu.org/gnu/libffcall/libffcall-%{version}.tar.gz
#!RemoteAsset
Source:         https://ftpmirror.gnu.org/gnu/libffcall/libffcall-%{version}.tar.gz.sig

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildSystem:    autotools
BuildOption(conf): --disable-static

%description
GNU Libffcall is a collection of libraries that can be used to build
foreign function call interfaces in embedded interpreters.

%package        devel
Summary:        Development files for the libffcall library
Requires:       %{name} = %{version}

%description    devel
This package contains the C++ header files, libraries, and build system files
needed to develop applications that use the libffcall library.

%install -a
find %{buildroot} -type f -name "*.a" -delete

%files
%license COPYING
%doc README
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_mandir}/man3/*.3.*
%{_datadir}/html/*.html

%changelog
%{?autochangelog}
