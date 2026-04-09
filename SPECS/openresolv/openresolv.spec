# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openresolv
Version:        3.17.0
Release:        %autorelease
Summary:        A framework for managing DNS resolution
License:        BSD-2-Clause
URL:            https://roy.marples.name/projects/openresolv
VCS:            git:https://github.com/NetworkConfiguration/openresolv
#!RemoteAsset
Source:         https://github.com/NetworkConfiguration/openresolv/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --sbindir=%{_sbindir}
BuildOption(conf):  --libexecdir=%{_prefix}/lib/resolvconf

BuildRequires:  make
BuildRequires:  gcc

Provides:       resolvconf = %{version}-%{release}

Requires(post):  update-alternatives
Requires(postun): update-alternatives

%description
openresolv provides a framework for managing /etc/resolv.conf, ensuring
that multiple processes (like DHCP clients and VPNs) can update DNS settings
without overwriting each other's changes.

%prep -a
for F in *.in; do
  [ "$F" != "resolvconf.in" ] && sed -i -e '1 s,^#!/bin/sh$,#,' $F
done

%install -a
mv %{buildroot}%{_sbindir}/resolvconf{,.%{name}}
mv %{buildroot}%{_mandir}/man8/resolvconf{,.%{name}}.8
touch %{buildroot}%{_sbindir}/resolvconf
touch %{buildroot}%{_mandir}/man8/resolvconf.8

%post
%{_sbindir}/update-alternatives \
  --install %{_sbindir}/resolvconf resolvconf %{_sbindir}/resolvconf.%{name} 30 \
  --slave %{_mandir}/man8/resolvconf.8%{?ext_man} resolvconf.8%{?ext_man} %{_mandir}/man8/resolvconf.%{name}.8%{?ext_man}

%postun
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove resolvconf %{_sbindir}/resolvconf.%{name}
fi
# no tests
%check

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/resolvconf.conf
%dir %{_prefix}/lib/resolvconf
%{_prefix}/lib/resolvconf/*
%{_sbindir}/resolvconf.%{name}
%{_mandir}/man5/resolvconf.conf.5*
%{_mandir}/man8/resolvconf.%{name}.8*
%ghost %{_sbindir}/resolvconf
%ghost %{_mandir}/man8/resolvconf.8*

%changelog
%autochangelog
