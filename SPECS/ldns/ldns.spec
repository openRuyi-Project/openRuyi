# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ldns
Version:        1.8.4
Release:        %autorelease
Summary:        A library for developing the Domain Name System
License:        BSD-3-Clause
URL:            https://www.nlnetlabs.nl/projects/ldns/
#!RemoteAsset
Source:         https://www.nlnetlabs.nl/downloads/ldns/ldns-%{version}.tar.gz
Patch:          0001-ldns-1.8.4-swig-4.3.patch
BuildSystem:    autotools

BuildOption(conf): --disable-rpath
BuildOption(conf): --disable-static
BuildOption(conf): --enable-rrtype-ninfo
BuildOption(conf): --enable-rrtype-rkey
BuildOption(conf): --enable-rrtype-cds
BuildOption(conf): --enable-rrtype-uri
BuildOption(conf): --enable-rrtype-ta
BuildOption(conf): --with-pyldns
BuildOption(conf): --with-pyldnsx
BuildOption(conf): --with-drill
BuildOption(conf): --with-examples
BuildOption(conf): --with-ca-path=%{_sysconfdir}/ssl/certs/
BuildOption(conf): PYTHON_VERSION=3

BuildOption(install): install-drill
BuildOption(install): install-examples
BuildOption(install): install-pyldns
BuildOption(install): install-pyldnsx

BuildRequires:  doxygen libpcap-devel python3-devel python3 swig
BuildRequires:  openssl-devel

%description
ldns is a C library for DNS development, supporting DNSSEC and other RFCs.

%package        devel
Summary:        Development files for ldns
Requires:       %{name} = %{version}
Requires:       pkgconfig openssl-devel

%description    devel
This package contains the header files and development files for ldns.

%package -n python3-ldns
Summary:    Python3 extensions for ldns
Requires:   %{name} = %{version}

%description -n python3-ldns
Python3 extensions for ldns

%install -a
find %{buildroot} -type f -name "*.la" -delete -print

# no tests.
%check

%files
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%license LICENSE
%doc libdns.vim README*
%{_bindir}/ldns-config
%{_includedir}/ldns/
%{_libdir}/libldns.so*
%{_libdir}/pkgconfig/ldns.pc
%{_mandir}/man3/*

%files -n python3-ldns
%license LICENSE
%{python3_sitearch}/*

%changelog
%{?autochangelog}
