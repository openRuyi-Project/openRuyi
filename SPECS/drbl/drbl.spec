# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           drbl
Version:        5.11.23
Release:        %autorelease
Summary:        Diskless Remote Boot in Linux
License:        GPL-2.0-only
URL:            https://drbl.org/
VCS:            git:https://github.com/stevenshiau/drbl.git
#!RemoteAsset:  sha256:3d5e0f6d037aeca26f2451648f58cf2c04c0a7403ea0a0f31b6642b0b2da52e9
Source:         https://github.com/stevenshiau/drbl/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  bash
BuildRequires:  findutils
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  perl

Recommends:     curl
Recommends:     nmap
Recommends:     openssh-server
Recommends:     rsync
Recommends:     tftp-server
Recommends:     wget

Requires:       bash
Requires:       coreutils
Requires:       gawk
Requires:       grep
Requires:       ipcalc
Requires:       perl
Requires:       procps-ng
Requires:       psmisc
Requires:       sed
Requires:       util-linux

%description
DRBL (Diskless Remote Boot in Linux) provides a diskless or systemless
environment for client machines. It uses distributed hardware resources
and makes it possible for clients to fully access local hardware.

DRBL is the framework Clonezilla is built on. It also contains the
clonezilla command line tools used to save and restore partitions over the
network.

%prep
%autosetup

%build
%make_build drbl-sbin-link languages

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_prefix}/sbin/* %{buildroot}%{_bindir}/
rmdir %{buildroot}%{_prefix}/sbin

%check
%make_build -C lang check

%files
%doc README
%doc %{_datadir}/drbl/doc
%license LICENSE
%{_bindir}/*
%{_datadir}/drbl/bin
%{_datadir}/drbl/image
%{_datadir}/drbl/lang
%{_datadir}/drbl/pkg
%{_datadir}/drbl/pki
%{_datadir}/drbl/postrun/drbl
%{_datadir}/drbl/prerun/drbl
%{_datadir}/drbl/sbin
%{_datadir}/drbl/setup/files/DBN
%{_datadir}/drbl/setup/files/LinuxMint
%{_datadir}/drbl/setup/files/RH
%{_datadir}/drbl/setup/files/SUSE
%{_datadir}/drbl/setup/files/Ubuntu
%{_datadir}/drbl/setup/files/boinc
%{_datadir}/drbl/setup/files/misc
%{_datadir}/drbl/setup/rpm-md-repos
%{_datadir}/drbl/setup/yum-repos
%{_datadir}/gdm/themes/drbl-gdm
%config(noreplace) %{_sysconfdir}/drbl/*

%changelog
%autochangelog
