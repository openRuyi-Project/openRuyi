# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dotconf
Version:        1.4.1
Release:        %autorelease
Summary:        Libraries to parse configuration files
License:        LGPL-2.1-only AND Apache-1.1
URL:            https://github.com/williamh/dotconf/
#!RemoteAsset
Source:         https://github.com/williamh/dotconf/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  findutils

%description
Dotconf is a library used to handle configuration files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf -p
autoreconf -fiv

%install -a
for file in AUTHORS doc/dotconf-features.txt; do
    iconv -f iso-8859-2 -t utf-8 -o iconv.tmp $file
    mv iconv.tmp $file
done

%files
%license COPYING
%doc README AUTHORS
%{_docdir}/dotconf
%{_libdir}/libdotconf*.so.*

%files devel
%doc doc/* examples/
%{_libdir}/libdotconf*.so
%{_includedir}/dotconf.h
%{_libdir}/pkgconfig/dotconf.pc

%changelog
%autochangelog
