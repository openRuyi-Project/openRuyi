# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond extstore        1
%bcond seccomp         1
%bcond sasl            0
%bcond sasl_pwdb       0
%bcond dtrace          0

Name:           memcached
Version:        1.6.28
Release:        %autorelease
Summary:        In-memory caching service
License:        BSD-3-Clause
URL:            https://memcached.org/
#!RemoteAsset
Source:         https://memcached.org/files/memcached-%{version}.tar.gz

BuildSystem:    autotools

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  autoconf
BuildRequires:  automake
%if %{with sasl}
BuildRequires:  cyrus-sasl-devel
%endif
%if %{with extstore}
BuildOption(conf): --enable-extstore
%endif
%if %{with seccomp}
BuildOption(conf): --enable-seccomp
%endif
%if %{with sasl}
BuildOption(conf): --enable-sasl
%endif
%if %{with sasl_pwdb}
BuildOption(conf): --enable-pwdb
%endif
%if %{with dtrace}
BuildOption(conf): --enable-dtrace
%endif


%description
Memcached is an in-memory key-value store.  It has a small
and generic API, and was originally intended for use with dynamic web
applications.

%install -a
rm -f %{buildroot}/%{_bindir}/memcached-debug
install -Dp -m0755 scripts/memcached-tool %{buildroot}%{_bindir}/memcached-tool
# pid directory
mkdir -p %{buildroot}/%{_localstatedir}/run/%{name}

%files
%license COPYING
%{_bindir}/memcached-tool
%{_bindir}/memcached
%{_includedir}/memcached/*.h
%{_mandir}/man1/*.1*
%doc AUTHORS ChangeLog COPYING NEWS README.md doc/CONTRIBUTORS doc/*.txt
%dir %attr(750,nobody,nobody) %{_localstatedir}/run/%{name}

%changelog
%{?autochangelog}
