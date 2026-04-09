# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Avoid: error: ‘_FORTIFY_SOURCE’ redefined
%global build_cflags $(echo "%{build_cflags}" | sed -e 's/-D_FORTIFY_SOURCE=3//')

%global commit b233050

Name:           fcoe-utils
Version:        1.0.34
Release:        %autorelease
Summary:        Fibre Channel over Ethernet utilities
License:        GPL-2.0-only
URL:            http://www.open-fcoe.org
VCS:            git:https://github.com/openSUSE/fcoe-utils
#!RemoteAsset:  sha256:826be5406753bac482b3a0533f582755d2847b4972714aaa56dc611418c1fde7
Source:         https://github.com/openSUSE/fcoe-utils/archive/%{commit}.tar.gz
BuildSystem:    autotools

Patch0:         0001-fcoemon-add-snprintf-string-precision-modifiers-in-f.patch
Patch1:         0002-Don-t-attempt-to-memcpy-zero-bytes.patch

BuildOption(conf):  --with-systemdsystemunitdir=%{_unitdir}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(lldpad)
BuildRequires:  systemd-rpm-macros
BuildRequires:  make
BuildRequires:  gcc
Requires:       lldpad
Requires:       iproute2
Requires:       multipath-tools
%{?systemd_requires}

%description
Fibre Channel over Ethernet utilities: fcoeadm for configuration and
fcoemon service for DCB Ethernet QOS filter management.

%conf -p
./bootstrap.sh

%install -a
rm -rf %{buildroot}/etc/init.d
install -d %{buildroot}%{_libexecdir}/fcoe
for file in contrib/*.sh debug/*sh; do
    install -m 755 ${file} %{buildroot}%{_libexecdir}/fcoe/
done

%post
%systemd_post fcoe.service fcoemon.socket

%preun
%systemd_preun fcoe.service fcoemon.socket

%postun
%systemd_postun_with_restart fcoe.service fcoemon.socket

%files
%doc README COPYING QUICKSTART
%{_sbindir}/*
%{_mandir}/man8/*
%{_unitdir}/fcoe.service
%{_unitdir}/fcoemon.socket
%config(noreplace) %{_sysconfdir}/fcoe/cfg-ethx
%config(noreplace) %{_sysconfdir}/fcoe/config
%{_datadir}/bash-completion/completions/*
%{_libexecdir}/fcoe/

%changelog
%autochangelog
