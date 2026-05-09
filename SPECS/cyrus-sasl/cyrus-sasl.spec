# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cyrus-sasl
Version:        2.1.28
Release:        %autorelease
Summary:        A framework for authentication and security in network protocols
License:        BSD-4-Clause AND (GPL-2.0-or-later OR MPL-1.1)
URL:            https://github.com/cyrusimap/cyrus-sasl/
#!RemoteAsset:  sha256:7ccfc6abd01ed67c1a0924b353e526f1b766b21f42d4562ee635a8ebfc5bb38c
Source:         https://github.com/cyrusimap/cyrus-sasl/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

Patch0:         0001-cyrus-sasl-lfs.patch
Patch1:         0002-fix_libpq-fe_include.patch
Patch2:         0003-Fix-time.h-check.patch
Patch3:         0004-cyrus-sasl-make-digestmd5-work-ssl3.patch

BuildOption(conf):  --with-pic
BuildOption(conf):  --with-plugindir=%{_libdir}/sasl2
BuildOption(conf):  --with-configdir=%{_sysconfdir}/sasl2/
BuildOption(conf):  --with-saslauthd=/run/sasl2/
BuildOption(conf):  --with-dblib=gdbm
BuildOption(conf):  --enable-login
BuildOption(conf):  --enable-gssapi
BuildOption(conf):  --enable-ntlm
BuildOption(conf):  --with-devrandom=/dev/urandom

BuildRequires:  gdbm-devel
BuildRequires:  pkgconfig(krb5)
BuildRequires:  libtool
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig

%description
The Cyrus SASL (Simple Authentication and Security Layer) is a framework for
authentication and data security in Internet protocols. It can be used on the
client or server side to provide authentication. This package contains the main
library and all standard authentication mechanism plugins.

%package        devel
Summary:        Development files for the Cyrus SASL library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, pkg-config files, and development
documentation needed to build applications that use the Cyrus SASL API.

%conf -p
autoreconf -fi
export CFLAGS="%{optflags} -fno-strict-aliasing -std=gnu17"

%install -a
mkdir -p %{buildroot}%{_sysconfdir}/sasl2

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
%{_libdir}/pkgconfig/libsasl2.pc

%changelog
%autochangelog
