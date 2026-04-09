# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global appstream_id org.kernel.software.network.ethtool

Name:           ethtool
Version:        6.15
Release:        %autorelease
Summary:        Settings tool for Ethernet NICs
License:        GPL-2.0-only AND GPL-2.0-or-later
URL:            https://www.kernel.org/pub/software/network/ethtool
VCS:            git:https://git.kernel.org/pub/scm/network/ethtool/ethtool.git
#!RemoteAsset
Source0:        https://www.kernel.org/pub/software/network/%{name}/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://www.kernel.org/pub/software/network/%{name}/%{name}-%{version}.tar.sign
BuildSystem:    autotools

Patch1:         0001-netlink-fix-missing-headers-in-text-output.patch
Patch2:         0002-netlink-fix-print_string-when-the-value-is-NULL.patch

BuildOption(conf):  --disable-static

BuildRequires:  xz
BuildRequires:  gcc
BuildRequires:  pkgconfig(libmnl)

%description
Ethtool is the standard Linux utility for controlling network drivers and
hardware, particularly for wired Ethernet devices. It can be used to:

  - Get identification and diagnostic information
  - Get extended device statistics
  - Control speed, duplex, autonegotiation and flow control for Ethernet devices
  - Control checksum offload and other hardware offload features
  - Control DMA ring sizes and interrupt moderation
  - Control receive queue selection for multiqueue devices
  - Upgrade firmware in flash memory

# TODO: make test pass.
%check

%files
%defattr(-,root,root)
%license COPYING LICENSE
%doc AUTHORS ChangeLog* NEWS README
%{_sbindir}/ethtool
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/ethtool
%{_mandir}/man8/ethtool.8*
%{_datadir}/metainfo/%{appstream_id}.metainfo.xml

%changelog
%autochangelog
