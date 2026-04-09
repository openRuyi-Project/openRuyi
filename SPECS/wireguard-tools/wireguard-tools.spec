# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           wireguard-tools
Version:        1.0.20250521
Release:        %autorelease
Summary:        Fast, modern, secure VPN tunnel
License:        GPL-2.0-only
URL:            https://www.wireguard.com/
VCS:            git:https://git.zx2c4.com/wireguard-tools
#!RemoteAsset
Source0:        https://git.zx2c4.com/wireguard-tools/snapshot/wireguard-tools-%{version}.tar.xz
#!RemoteAsset
Source1:        https://git.zx2c4.com/wireguard-tools/snapshot/wireguard-tools-%{version}.tar.asc
BuildSystem:    autotools

BuildOption(build):  RUNSTATEDIR=%{_rundir}
BuildOption(build):  -C src
BuildOption(install):  BINDIR=%{_bindir}
BuildOption(install):  MANDIR=%{_mandir}
BuildOption(install):  RUNSTATEDIR=%{_rundir}
BuildOption(install):  WITH_BASHCOMPLETION=yes
BuildOption(install):  WITH_WGQUICK=yes
BuildOption(install):  WITH_SYSTEMDUNITS=yes
BuildOption(install):  -C src
BuildOption(check):  -C src

BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  gcc
%{?systemd_requires}

%description
WireGuard is a novel VPN that runs inside the Linux Kernel and uses
state-of-the-art cryptography (the "Noise" protocol). It aims to be
faster, simpler, leaner, and more useful than IPSec, while avoiding
the massive headache. It intends to be considerably more performant
than OpenVPN. WireGuard is designed as a general purpose VPN for
running on embedded interfaces and super computers alike, fit for
many different circumstances. It runs over UDP.

This package provides the wg binary for controlling WireGuard.

# no configure script.
%conf

%build -p
%set_build_flags

## Start DNS Hatchet
pushd contrib/dns-hatchet
./apply.sh
popd
## End DNS Hatchet

# test require scan-build
%check

%post
%systemd_post service_add_post wg-quick.target wg-quick@.service

%preun
%systemd_preun wg-quick.target wg-quick@.service

%postun
%systemd_postun wg-quick.target wg-quick@.service

%files
%license COPYING
%doc README.md contrib
%{_bindir}/wg
%{_bindir}/wg-quick
%{_sysconfdir}/wireguard/
%{_datadir}/bash-completion/completions/wg
%{_datadir}/bash-completion/completions/wg-quick
%{_unitdir}/wg-quick@.service
%{_unitdir}/wg-quick.target
%{_mandir}/man8/wg.8*
%{_mandir}/man8/wg-quick.8*

%changelog
%autochangelog
