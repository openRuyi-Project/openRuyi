# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libabigail
Version:        2.10
Release:        %autorelease
Summary:        Application Binary Interface Generic Analysis and Instrumentation Library
License:        Apache-2.0 WITH LLVM-exception
URL:            https://sourceware.org/libabigail/
VCS:            git://sourceware.org/git/libabigail.git
#!RemoteAsset:  sha256:0cc10e6471398330e001b9fe37f1e8c5108a9ab632b08ca9634d6c64bc380b78
Source0:        https://mirrors.kernel.org/sourceware/libabigail/libabigail-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --disable-static

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  doxygen
BuildRequires:  python3-sphinx
BuildRequires:  texinfo
BuildRequires:  binutils-devel
BuildRequires:  pkgconfig(libbpf)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxxhash)

%description
This libabigail package aims at providing a C++ library for constructing,
manipulating, serializing and de-serializing ABI-relevant artifacts.
The set of artifacts that we are interested in is made of constructions
like types, variables, functions and declarations of a given library or
program. For a given program or library, this set of constructions is
called an ABI corpus. The library provides a way to compare two ABI corpuses,
provide detailed information about their differences and help build tools
to infer interesting conclusions about these differences.

%package        devel
Summary:        Shared library and header files for libabigail
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains a shared library and the associated header files to write ABI analysis tools for libabigail.

%build -a
make -C doc/manuals man info -j1

%install -a
make -C doc/manuals install-man-and-info-doc DESTDIR=%{buildroot}

%files
%doc README AUTHORS ChangeLog
%license LICENSE.txt license-change-2020.txt
%{_bindir}/abicompat
%{_bindir}/abidiff
%{_bindir}/abidw
%{_bindir}/abilint
%{_bindir}/abipkgdiff
%{_bindir}/kmidiff
%{_libdir}/libabigail.so.9
%{_libdir}/libabigail.so.9.*
%{_libdir}/libabigail/default.abignore
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_infodir}/abigail.info*

%files devel
%{_libdir}/libabigail.so
%{_libdir}/pkgconfig/libabigail.pc
%{_includedir}/*
%{_datadir}/aclocal/abigail.m4

%changelog
%autochangelog
