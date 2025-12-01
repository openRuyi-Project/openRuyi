# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libfastjson
Version:        1.2304.0
Release:        %autorelease
Summary:        Fast JSON library for C
License:        MIT
URL:            https://github.com/rsyslog/libfastjson
#!RemoteAsset
Source0:        https://download.rsyslog.com/libfastjson/libfastjson-%{version}.tar.gz
BuildSystem:    autotools
BuildOption(conf):    --disable-static
%description
libfastjson is a fork from json-c aiming to provide: a small library
with essential JSON handling functions, sufficiently good JSON support (not
100% standards compliant), and very fast processing.

%package        devel
Summary:        Development files for libfastjson
Requires:       libfastjson = %{version}-%{release}

%description    devel
provide development files for libfastjson

%files
%license COPYING
%doc AUTHORS ChangeLog README.html
%{_libdir}/libfastjson.so*

%files devel
%{_includedir}/libfastjson
%{_libdir}/libfastjson.so
%{_libdir}/pkgconfig/libfastjson.pc

%changelog
%{?autochangelog}
