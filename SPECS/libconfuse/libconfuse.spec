# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libconfuse
Version:        3.3
Release:        %autorelease
Summary:        A configuration file parser library
License:        ISC
URL:            https://github.com/martinh/libconfuse
#!RemoteAsset
Source0:        https://github.com/martinh/libconfuse/releases/download/v%{version}/confuse-%{version}.tar.gz

BuildSystem:    autotools

BuildOption(conf): --enable-shared
BuildOption(conf): --disable-static

BuildRequires:  gcc check-devel pkgconfig make

%description
libConfuse is an easy-to-use configuration file parser library written in C.
It supports sections, lists of values, and other features like environment
variable expansion and nested includes.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       pkgconfig

%description devel
This package contains the header files, libraries, and documentation
needed to develop applications that use libconfuse.

%install -a
rm -f %{buildroot}%{_libdir}/*.la
mkdir -p %{buildroot}%{_mandir}/man3/
cp -p doc/man/man3/*.3 %{buildroot}%{_mandir}/man3/
mkdir -p ex2/examples
cp -p examples/{ftpconf.c,ftp.conf,simple.c,simple.conf,reread.c,reread.conf} \
    ex2/examples/
rm -rf %{buildroot}%{_datadir}/doc/confuse
%find_lang confuse --generate-subpackages

%files
%license LICENSE
%doc %{_docdir}/%{name}
%doc doc/html
%{_libdir}/libconfuse.so.2*
%{_mandir}/man?/*.*

%files devel
%doc ex2/examples
%{_includedir}/confuse.h
%{_libdir}/libconfuse.so
%{_libdir}/pkgconfig/libconfuse.pc

%changelog
%{?autochangelog}
