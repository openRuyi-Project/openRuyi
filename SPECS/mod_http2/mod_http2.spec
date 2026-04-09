# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%{!?_httpd_mmn: %global _httpd_mmn %(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}

Name:           mod_http2
Version:        2.0.39
Release:        %autorelease
Summary:        HTTP/2 module for Apache httpd
License:        Apache-2.0
URL:            https://icing.github.io/mod_h2/
VCS:            git:https://github.com/icing/mod_h2
#!RemoteAsset
Source0:        https://github.com/icing/mod_h2/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --with-apxs=%{_bindir}/apxs

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  httpd-devel
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  hostname

Requires:       httpd-mmn = %{_httpd_mmn}

%description
The mod_h2 Apache httpd module implements the HTTP2 protocol (h2+h2c) on
top of libnghttp2 for httpd 2.4 servers.

%conf -p
autoreconf -i

%install -a
rm -rf %{buildroot}%{_docdir}/%{name}

%check
make check

%files
%license LICENSE
%doc AUTHORS ChangeLog README.md
%{_httpd_moddir}/*.so

%changelog
%autochangelog
