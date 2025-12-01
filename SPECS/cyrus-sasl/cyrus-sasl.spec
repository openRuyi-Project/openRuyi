# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cyrus-sasl
Version:        2.1.28
Release:        %autorelease
Summary:        A framework for authentication and security in network protocols
License:        BSD-4-Clause AND (GPL-2.0-or-later OR MPL-1.1)
URL:            https://github.com/cyrusimap/cyrus-sasl/
#!RemoteAsset
Source:         https://github.com/cyrusimap/cyrus-sasl/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-cyrus-sasl-lfs.patch
Patch1:         0002-fix_libpq-fe_include.patch
Patch2:         0003-Fix-time.h-check.patch
Patch3:         0004-cyrus-sasl-make-digestmd5-work-ssl3.patch

BuildSystem:    autotools
BuildOption(conf): --with-pic --with-plugindir=%{_libdir}/sasl2 --with-configdir=%{_sysconfdir}/sasl2/
BuildOption(conf): --with-saslauthd=/run/sasl2/ --with-dblib=gdbm --enable-login
BuildOption(conf): --enable-gssapi --enable-ntlm --with-devrandom=/dev/urandom

BuildRequires:  gdbm-devel
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig

%description
The Cyrus SASL (Simple Authentication and Security Layer) is a framework for
authentication and data security in Internet protocols. It can be used on the
client or server side to provide authentication. This package contains the main
library and all standard authentication mechanism plugins.

%package devel
Summary:        Development files for the Cyrus SASL library
Requires:       %{name} = %{version}

%description devel
This package contains the header files, pkg-config files, and development
documentation needed to build applications that use the Cyrus SASL API.

%conf -p
autoreconf -fi
export CFLAGS="%{optflags} -fno-strict-aliasing -std=gnu17"

%install -a
mkdir -p %{buildroot}%{_sysconfdir}/sasl2
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%{_libdir}/libsasl2.so.*
%dir %{_libdir}/sasl2
%{_libdir}/sasl2/*.so*
%dir %{_sysconfdir}/sasl2/
%{_sbindir}/saslpasswd2
%{_sbindir}/pluginviewer
%{_sbindir}/saslauthd
%{_sbindir}/sasldblistusers2
%{_sbindir}/testsaslauthd
%{_mandir}/man8/saslpasswd2.8*
%{_mandir}/man8/pluginviewer.8*
%{_mandir}/man8/saslauthd.8*
%{_mandir}/man8/sasldblistusers2.8*
%{_mandir}/man8/testsaslauthd.8*

%files devel
%license COPYING
%doc AUTHORS ChangeLog README doc
%{_includedir}/sasl/
%{_mandir}/man3/sasl*.3*
%{_libdir}/libsasl2.so
%{_libdir}/pkgconfig/*

%changelog
%{?autochangelog}
