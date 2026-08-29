# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define minor dev9

Name:           haproxy
Version:        3.3
Release:        %autorelease
Summary:        The Reliable, High Performance TCP/HTTP Load Balancer
License:        GPL-2.0-or-later
URL:            https://www.haproxy.org/
VCS:            git:https://github.com/haproxy/haproxy
#!RemoteAsset:  sha256:8e83364938b26602102f746127a2fe8f92929d8bb5f671f7780caa23cf9686f3
Source0:        https://www.haproxy.org/download/3.3/src/devel/%{name}-%{version}-%{minor}.tar.gz
Source1:        %{name}.cfg
Source2:        %{name}.logrotate
Source3:        %{name}.sysconfig
Source4:        %{name}.service
BuildSystem:    autotools

BuildOption(build):  CPU="generic"
BuildOption(build):  TARGET="linux-glibc"
BuildOption(build):  USE_OPENSSL=1
BuildOption(build):  USE_PCRE2=1
BuildOption(build):  USE_SLZ=1
BuildOption(build):  USE_LUA=1
BuildOption(build):  USE_CRYPT_H=1
BuildOption(build):  USE_SYSTEMD=1
BuildOption(build):  USE_LINUX_TPROXY=1
BuildOption(build):  USE_GETADDRINFO=1
BuildOption(build):  USE_PROMEX=1
BuildOption(build):  DEFINE=-DMAX_SESS_STKCTR=12
BuildOption(build):  CFLAGS="%{build_cflags}"
BuildOption(build):  LDFLAGS="%{build_ldflags}"

BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  SBINDIR=%{_sbindir}
BuildOption(install):  MANDIR=%{_mandir}
BuildOption(install):  DOCDIR=%{_docdir}/%{name}

BuildRequires:  lua-devel
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  libatomic_ops-devel
BuildRequires:  pkgconfig(libxcrypt)
BuildRequires:  pkgconfig(libsystemd)

Requires(pre):  shadow
%{?systemd_requires}

%description
HAProxy is a free, very fast and reliable solution offering high availability, load balancing,
and proxying for TCP and HTTP-based applications.

%package        doc
Summary:        Documentation for haproxy
BuildArch:      noarch

%description    doc
This package contains the documentation and examples for haproxy.

# No configure
%conf

%build -a
%make_build admin/halog/halog
%make_build -C admin/iprange

%install -a
mkdir   -p %{buildroot}%{_bindir}
install -p -m 0755 admin/halog/halog %{buildroot}%{_bindir}/halog
install -p -m 0755 admin/iprange/iprange %{buildroot}%{_bindir}/
install -p -m 0755 admin/iprange/ip6range %{buildroot}%{_bindir}/

install -d -m 0755 %{buildroot}%{_localstatedir}/lib/haproxy
install -d -m 0755 %{buildroot}%{_sysconfdir}/haproxy/conf.d
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/haproxy/%{name}.cfg
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service

install -d -m 0755 %{buildroot}%{_datadir}/haproxy
install -p -m 0644 examples/errorfiles/* %{buildroot}%{_datadir}/haproxy/

# No check
%check

%pre
getent group haproxy >/dev/null || groupadd -r haproxy
getent passwd haproxy >/dev/null || useradd -r -g haproxy -d \
    %{_localstatedir}/lib/haproxy -s /sbin/nologin -c "haproxy" haproxy
exit 0

%post
%systemd_post haproxy.service

%preun
%systemd_preun haproxy.service

%postun
%systemd_postun_with_restart haproxy.service

%files
%license LICENSE
%dir %{_sysconfdir}/haproxy
%config(noreplace) %{_sysconfdir}/haproxy/haproxy.cfg
%config(noreplace) %{_sysconfdir}/logrotate.d/haproxy
%config(noreplace) %{_sysconfdir}/sysconfig/haproxy
%{_sbindir}/haproxy
%{_unitdir}/haproxy.service
%dir %{_sysconfdir}/haproxy/conf.d
%dir %{_localstatedir}/lib/haproxy
%{_bindir}/halog
%{_bindir}/iprange
%{_bindir}/ip6range

%files doc
%doc %{_docdir}/haproxy
%doc doc/* examples/* CHANGELOG VERSION
%dir %{_datadir}/haproxy
%{_datadir}/haproxy/*
%{_mandir}/man1/*

%changelog
%autochangelog
