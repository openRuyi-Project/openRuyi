# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           liblognorm
Version:        2.0.6
Release:        %autorelease
Summary:        A tool to normalize log data
License:        LGPL-2.1-or-later
URL:            http://www.liblognorm.com
VCS:            git:https://github.com/rsyslog/liblognorm.git
#!RemoteAsset
Source0:        http://www.liblognorm.com/files/download/%{name}-%{version}.tar.gz
BuildSystem:    autotools

Patch:          0001-Port-pcre-dependency-to-pcre2.patch

BuildOption(conf):  --enable-regexp
BuildOption(conf):  --disable-docs
# Avoid contaminating the include directory
BuildOption(conf):  --includedir=%{_includedir}/%{name}/
BuildOption(conf):  --disable-rpath

BuildRequires:  chrpath
BuildRequires:  pkgconfig(libfastjson)
BuildRequires:  pkgconfig(libestr)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
# sphinx-build is required to build documentation
# BuildRequires:  python-sphinx

%description
liblognorm is a tool to normalize log data. It can extract structured data
from different log formats into a common set of well-defined fields.

%package        devel
Summary:        Development files for the liblognorm library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(json-c)
Requires:       pkgconfig(libestr)

%description    devel
This package provides the development tools, header files, and documentation
for programs using the liblognorm library.

%conf -p
autoreconf -vfi

%install -a
find %{buildroot} -type f -name "*.a" -delete -print

%check -p
# One test at a time for tmp.rulebase file access
%define _smp_mflags -j1

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/lib*.so.*
%{_bindir}/lognormalizer

%files devel
%{_libdir}/lib*.so
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/lognorm.pc

%changelog
%{?autochangelog}
