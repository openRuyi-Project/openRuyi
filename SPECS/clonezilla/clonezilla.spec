# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           clonezilla
Version:        5.19.21
Release:        %autorelease
Summary:        Partition and disk imaging and cloning tool
License:        GPL-2.0-or-later
URL:            https://clonezilla.org/
VCS:            git:https://gitlab.com/stevenshiau/clonezilla.git
#!RemoteAsset:  sha256:c0d0f858a95c745e84aaebd5e1caf901cc78732c195944ee5d2e9fde4c8daed6
Source:         https://github.com/stevenshiau/clonezilla/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  bash
BuildRequires:  findutils
BuildRequires:  grep
BuildRequires:  make

Recommends:     btrfs-progs
Recommends:     cifs-utils
Recommends:     cryptsetup
Recommends:     curl
Recommends:     dhcpcd
Recommends:     dosfstools
Recommends:     f2fs-tools
Recommends:     lvm2
Recommends:     mdadm
Recommends:     nmap
Recommends:     partimage
Recommends:     pigz
Recommends:     smartmontools
Recommends:     squashfs-tools
Recommends:     xfsprogs
Recommends:     xorriso

Requires:       bash
Requires:       bc
Requires:       bzip2
Requires:       coreutils
Requires:       dialog
Requires:       drbl >= 5.11.23
Requires:       e2fsprogs
Requires:       findutils
Requires:       gawk
Requires:       gptfdisk
Requires:       grep
Requires:       gzip
Requires:       jq
Requires:       lz4
Requires:       lzop
Requires:       ntfs-3g
Requires:       parted
Requires:       partclone >= 0.3.52
Requires:       pbzip2
Requires:       perl
Requires:       perl(Logfile::Rotate)
Requires:       procps-ng
Requires:       psmisc
Requires:       python3
Requires:       sed
Requires:       tar
Requires:       udpcast
Requires:       util-linux
Requires:       wget
Requires:       xz
Requires:       zstd

%description
Clonezilla is a partition and disk imaging and cloning tool. It is based
on DRBL, Partclone and udpcast and can save and restore only the used
blocks of a partition.

Clonezilla supports many file systems, including ext2/3/4, XFS, Btrfs,
NTFS, FAT, exFAT, F2FS and HFS+, and can clone a single machine or many
machines at once over multicast.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_prefix}/sbin/* %{buildroot}%{_bindir}/
rmdir %{buildroot}%{_prefix}/sbin

%check
#no check

%files
%doc README
%doc %{_datadir}/clonezilla/doc
%license LICENSE
%{_bindir}/*
%{_datadir}/drbl/postrun/ocs
%{_datadir}/drbl/prerun/ocs
%{_datadir}/drbl/samples
%{_datadir}/drbl/sbin/ocs-chnthn-functions
%{_datadir}/drbl/sbin/ocs-functions
%{_datadir}/drbl/sbin/set-netboot-1st-efi-nvram
%{_datadir}/drbl/setup/files/gparted
%{_datadir}/drbl/setup/files/ocs
%{_datadir}/drbl/setup/files/riscv64
%{_mandir}/man8/ocs-onthefly.8*
%{_mandir}/man8/ocs-sr.8*
%config(noreplace) %{_sysconfdir}/drbl/drbl-ocs.conf

%changelog
%autochangelog
