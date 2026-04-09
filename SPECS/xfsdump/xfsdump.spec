# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xfsdump
Version:        3.2.0
Release:        %autorelease
Summary:        Backup and restore utilities for the XFS filesystem
License:        GPL-1.0-or-later
URL:            https://xfs.wiki.kernel.org
VCS:            git:https://git.kernel.org/pub/scm/fs/xfs/xfsdump-dev.git
#!RemoteAsset
Source0:        http://kernel.org/pub/linux/utils/fs/xfs/%{name}/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  gawk
BuildRequires:  xfsprogs-devel
BuildRequires:  util-linux-devel
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  gnupg

Requires:       xfsprogs
Requires:       attr

%description
The xfsdump package contains xfsdump, xfsrestore and a number of
other utilities for administering XFS filesystems.

xfsdump examines files in a filesystem, determines which need to be
backed up, and copies those files to a specified disk, tape or other
storage medium.     It uses XFS-specific directives for optimizing the
dump of an XFS filesystem, and also knows how to backup XFS extended
attributes.  Backups created with xfsdump are "endian safe" and can
thus be transfered between Linux machines of different architectures
and also between IRIX machines.

xfsrestore performs the inverse function of xfsdump; it can restore a
full backup of a filesystem.  Subsequent incremental backups can then
be layered on top of the full backup.  Single files and directory
subtrees may be restored from full or partial backups.

%install -a
# remove non-versioned docs location
rm -rf %{buildroot}/%{_datadir}/doc/xfsdump/

(cd %{buildroot}/%{_sbindir}; mv ../../sbin/xfsdump .)
(cd %{buildroot}/%{_sbindir}; mv ../../sbin/xfsrestore .)

# Create inventory dir (otherwise created @ runtime)
mkdir -p %{buildroot}/%{_sharedstatedir}/xfsdump/inventory

%find_lang %{name} --generate-subpackages

# No check
%check

%files -f %{name}.lang
%doc README doc/COPYING doc/CHANGES doc/README.xfsdump doc/xfsdump_ts.txt
%{_mandir}/man8/*
%{_sbindir}/*
%{_sharedstatedir}/xfsdump/inventory

%changelog
%autochangelog
