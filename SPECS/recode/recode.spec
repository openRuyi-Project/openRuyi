# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           recode
Version:        3.7.15
Release:        %autorelease
Summary:        Conversion between character sets and surfaces
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND BSD-2-Clause
URL:            https://github.com/rrthomas/recode
#!RemoteAsset:  sha256:f590407fc51badb351973fc1333ee33111f05ec83a8f954fd8cf0c5e30439806
Source0:        https://github.com/rrthomas/recode/releases/download/v%{version}/recode-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --without-dmalloc
BuildOption(conf):  --disable-gcc-warnings
BuildOption(conf):  --enable-largefile
BuildOption(conf):  --enable-nls
BuildOption(conf):  --disable-rpath
BuildOption(conf):  --enable-shared
BuildOption(conf):  --disable-static
BuildOption(conf):  PYTHON=%{__python3}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  python3dist(cython)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

%description
The recode tool and library convert files between character sets and surfaces.
It recognizes or produces over 200 different character sets.

%package        devel
Summary:        Header files for development using recode library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides the header files for a recode library.

%install -a
rm -f %{buildroot}%{_infodir}/dir
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*

%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%license COPYING COPYING-LIB
%doc AUTHORS NEWS README THANKS TODO
%{_bindir}/recode
%{_libdir}/librecode.so.3*
%{_mandir}/man1/recode.1*
%{_infodir}/recode.info*

%files devel
%{_libdir}/*.so
%{_includedir}/recode.h
%{_includedir}/recodext.h

%changelog
%autochangelog
