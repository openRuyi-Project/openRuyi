# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0

Name:           libbytesize
Version:        2.12
Release:        %autorelease
Summary:        A library for working with sizes in bytes
License:        LGPL-2.1-or-later
URL:            https://github.com/storaged-project/libbytesize
#!RemoteAsset
Source0:        https://github.com/storaged-project/libbytesize/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --with-python3
BuildOption(conf):  --with-tools
%if %{with doc}
BuildOption(conf):  --enable-gtk-doc
%else
BuildOption(conf):  --disable-gtk-doc
%endif

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  gettext-devel
%if %{with doc}
BuildRequires:  gtk-doc
%endif

%description
The libbytesize is a C library that facilitates work with sizes in
bytes. It handles parsing input from users and producing human readable
representation of sizes, taking localization into account.

%package        devel
Summary:        Development files for libbytesize
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains header files and pkg-config files needed for development
with the libbytesize library.

%package     -n python-bytesize
Summary:        Python 3 bindings for libbytesize
Requires:       %{name} = %{version}-%{release}
Provides:       python3-bytesize
%python_provide python3-bytesize

%description -n python-bytesize
This package contains Python 3 bindings for libbytesize.

%conf -p
./autogen.sh

%check
# skip the translation test as we don't have python3-polib yet.
make check TESTS=libbytesize_unittest.sh

%install -a
# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files
%doc README.md
%license LICENSE
%{_libdir}/libbytesize.so.*
%{_bindir}/bscalc
%{_mandir}/man1/bscalc.1*

%files devel
%{_libdir}/libbytesize.so
%dir %{_includedir}/bytesize
%{_includedir}/bytesize/bs_size.h
%{_libdir}/pkgconfig/bytesize.pc
%if %{with doc}
%{_datadir}/gtk-doc/html/libbytesize
%endif

%files -n python-bytesize
%dir %{python3_sitearch}/bytesize
%{python3_sitearch}/bytesize/*

%changelog
%autochangelog
