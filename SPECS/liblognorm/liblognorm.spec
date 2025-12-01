# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           liblognorm
Version:        2.0.6
Release:        %autorelease
Summary:        A tool to normalize log data
License:        LGPL-2.1-or-later
URL:            http://www.liblognorm.com
#!RemoteAsset
Source0:        http://www.liblognorm.com/files/download/%{name}-%{version}.tar.gz
Patch:          0001-Port-pcre-dependency-to-pcre2.patch
BuildSystem:    autotools

BuildOption(conf): --enable-regexp
BuildOption(conf): --disable-docs
# Avoid contaminating the include directory
BuildOption(conf): --includedir=%{_includedir}/%{name}/
BuildOption(conf): --disable-rpath

BuildRequires:  chrpath libfastjson-devel libestr-devel pcre2-devel gcc
BuildRequires:  autoconf automake libtool
# sphinx-build is required to build documentation
# BuildRequires:  python-sphinx

%description
liblognorm is a tool to normalize log data. It can extract structured data
from different log formats into a common set of well-defined fields.

%package     devel
Summary:     Development files for the liblognorm library
Requires:    %{name} = %{version}
Requires:    json-c-devel libestr-devel

%description devel
This package provides the development tools, header files, and documentation
for programs using the liblognorm library.

%conf -p
autoreconf -vfi

%install -a
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "*.a" -delete -print

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/lib*.so.*
%{_bindir}/lognormalizer

%files devel
%{_libdir}/lib*.so
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc

%changelog
%{?autochangelog}
