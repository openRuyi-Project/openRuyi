# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           iputils
Version:        20250605
Release:        %autorelease
Summary:        Network monitoring tools including ping
License:        BSD-4-Clause-UC AND GPL-2.0-or-later
URL:            https://github.com/iputils/iputils
#!RemoteAsset
Source0:        %{url}/releases/download/%{version}/iputils-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  libxslt
BuildRequires:  docbook-xsl
BuildRequires:  systemd
BuildRequires:  iproute2

%description
The iputils package contains basic utilities for monitoring a network,
including ping. The ping command sends a series of ICMP protocol
ECHO_REQUEST packets to a specified network host to discover whether
the target machine is alive and receiving network traffic.

%install -a
# We don't want these
rm -fv %{buildroot}/usr/share/iputils/*.html

%find_lang %{name} --generate-subpackages

ln -sf --relative ${RPM_BUILD_ROOT}%{_bindir}/ping ${RPM_BUILD_ROOT}%{_bindir}/ping6
ln -sf --relative ${RPM_BUILD_ROOT}%{_bindir}/tracepath ${RPM_BUILD_ROOT}%{_bindir}/tracepath6
echo ".so man8/ping.8" > ${RPM_BUILD_ROOT}%{_mandir}/man8/ping6.8
echo ".so man8/tracepath.8" > ${RPM_BUILD_ROOT}%{_mandir}/man8/tracepath6.8

%files
%attr(0755,root,root) %caps(cap_net_raw=p) %{_bindir}/clockdiff
%attr(0755,root,root) %caps(cap_net_raw=p) %{_bindir}/arping
%attr(0755,root,root) %caps(cap_net_raw=p) %{_bindir}/ping6
%attr(0755,root,root) %caps(cap_net_raw=p) %{_bindir}/ping
%{_bindir}/tracepath
%{_bindir}/tracepath6
%attr(644,root,root) %{_mandir}/man8/clockdiff.8*
%attr(644,root,root) %{_mandir}/man8/arping.8*
%attr(644,root,root) %{_mandir}/man8/ping.8*
%{_mandir}/man8/ping6.8*
%attr(644,root,root) %{_mandir}/man8/tracepath.8*
%{_mandir}/man8/tracepath6.8*

%changelog
%autochangelog
