# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           hostname
Version:        3.25
Release:        %autorelease
Summary:        Utility to Set/Show the Host Name or Domain Name
License:        GPL-2.0-or-later
URL:            https://tracker.debian.org/pkg/hostname
VCS:            git:https://salsa.debian.org/meskes/hostname.git
#!RemoteAsset:  sha256:5bb5d1be011158090157c9e7587ae5606c262a5020ecdc5caac6686b9910592e
Source0:        https://deb.debian.org/debian/pool/main/h/hostname/hostname_%{version}.tar.xz#/hostname-%{version}.tar.xz
Source1:        nis-domainname
Source2:        nis-domainname.service.in
BuildSystem:    autotools

BuildOption(build):  CFLAGS="%{optflags} -D_GNU_SOURCE"
BuildOption(install):  prefix=%{_prefix}
BuildOption(install):  exec_prefix=%{_exec_prefix}
BuildOption(install):  bindir=%{_bindir}
BuildOption(install):  mandir=%{_mandir}

BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros

%description
This package provides commands which can be used to display the system's DNS
name, and to display or set its hostname or NIS domain name.

# No configure
%conf

%install -a
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE2} > nis-domainname.service
install -m 0755 -d %{buildroot}%{_libexecdir}/%{name}
install -m 0755 -d %{buildroot}%{_unitdir}
install -p -m 0755 %{SOURCE1} %{buildroot}%{_libexecdir}/%{name}/nis-domainname
install -p -m 0644 nis-domainname.service %{buildroot}%{_unitdir}

%check
# No tests here.

%post
%systemd_post nis-domainname.service

%preun
%systemd_preun nis-domainname.service

%files
%license COPYRIGHT
%doc debian/changelog
%{_bindir}/hostname
%{_bindir}/domainname
%{_bindir}/dnsdomainname
%{_bindir}/nisdomainname
%{_bindir}/ypdomainname
%{_mandir}/man1/hostname.1%{?ext_man}
%{_mandir}/man1/domainname.1%{?ext_man}
%{_mandir}/man1/dnsdomainname.1%{?ext_man}
%{_mandir}/man1/nisdomainname.1%{?ext_man}
%{_mandir}/man1/ypdomainname.1%{?ext_man}
%{_unitdir}/nis-domainname.service
%{_libexecdir}/hostname/

%changelog
%autochangelog
