# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ldns
Version:        1.8.4
Release:        %autorelease
Summary:        A library for developing the Domain Name System
License:        BSD-3-Clause
URL:            https://www.nlnetlabs.nl/projects/ldns/
VCS:            git:https://github.com/NLnetLabs/ldns
#!RemoteAsset
Source:         https://www.nlnetlabs.nl/downloads/ldns/ldns-%{version}.tar.gz
BuildSystem:    autotools

Patch:          0001-ldns-1.8.4-swig-4.3.patch

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-rrtype-ninfo
BuildOption(conf):  --enable-rrtype-rkey
BuildOption(conf):  --enable-rrtype-cds
BuildOption(conf):  --enable-rrtype-uri
BuildOption(conf):  --enable-rrtype-ta
BuildOption(conf):  --with-pyldns
BuildOption(conf):  --with-pyldnsx
BuildOption(conf):  --with-drill
BuildOption(conf):  --with-examples
BuildOption(conf):  --with-ca-path=%{_sysconfdir}/ssl/certs/
BuildOption(conf):  PYTHON_VERSION=3
BuildOption(install):  install-drill
BuildOption(install):  install-examples
BuildOption(install):  install-pyldns
BuildOption(install):  install-pyldnsx

BuildRequires:  doxygen
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3
BuildRequires:  swig
BuildRequires:  pkgconfig(openssl)

%description
ldns is a C library for DNS development, supporting DNSSEC and other RFCs.

%package        devel
Summary:        Development files for ldns
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       pkgconfig(openssl)

%description    devel
This package contains the header files and development files for ldns.

%package     -n python-ldns
Summary:        Python extensions for ldns
Provides:       python3-ldns = %{version}-%{release}
%python_provide python3-ldns
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-ldns
Python extensions for ldns

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

%files -n python-ldns
%license LICENSE
%{python3_sitearch}/*

%changelog
%autochangelog
