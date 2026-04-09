# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           iptraf-ng
Version:        1.2.2
Release:        %autorelease
Summary:        A console-based network monitoring utility
License:        GPL-2.0-or-later
URL:            https://github.com/iptraf-ng/iptraf-ng/
#!RemoteAsset
Source0:        https://github.com/iptraf-ng/iptraf-ng/archive/refs/tags/v%{version}.tar.gz
Source1:        iptraf-ng.logrotate
BuildSystem:    autotools

BuildOption(build):  V=1
BuildOption(build):  CFLAGS="-g -O2 -Wall -W -std=gnu99 -Werror=format-security %{optflags}"
BuildOption(build):  LDFLAGS="%{build_ldflags}"
BuildOption(install):  prefix=%{_prefix}
BuildOption(install):  sbindir=%{_sbindir}
BuildOption(install):  DESTDIR=%{buildroot}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(ncurses)

%description
IPTraf-ng is a console-based network monitoring utility. It gathers data like
TCP connection packet and byte counts, interface statistics and activity
indicators.

# No configure.
%conf

%check
# No tests here.

%install -a
install -D -m 0644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/iptraf-ng

install -d -m 0755 %{buildroot}%{_localstatedir}/{log,lib}/iptraf-ng
mkdir -p %{buildroot}/run
install -d -m 0755 %{buildroot}/run/%{name}/

%files
%doc CHANGES FAQ LICENSE README* Documentation
%{_sbindir}/iptraf-ng
%{_mandir}/man8/iptraf-ng.8*
%{_localstatedir}/log/iptraf-ng
%{_localstatedir}/lib/iptraf-ng
%config(noreplace) %{_sysconfdir}/logrotate.d/iptraf-ng
%dir /run/iptraf-ng/

%changelog
%autochangelog
