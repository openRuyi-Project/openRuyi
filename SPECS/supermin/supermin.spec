# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           supermin
Version:        5.3.5
Release:        %autorelease
Summary:        Tool for creating supermin appliances
License:        GPL-2.0-or-later
URL:            https://github.com/libguestfs/supermin
VCS:            git:https://github.com/libguestfs/supermin.git
#!RemoteAsset:  sha256:58d6e2262cb2ade036d3da4080331066888efede401c7f9fecd2317518947b4e
Source0:        https://github.com/libguestfs/supermin/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

# Downstream openRuyi distro detection and RPM handler tests.
Patch2000:      2000-recognize-openruyi.patch
# Downstream support for the configured RPM database path and NDB.
Patch2001:      2001-use-configured-rpm-database.patch

# OBS and similar environments have no outbound package-download access.
BuildOption(conf):  --disable-network-tests

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  augeas
BuildRequires:  dnf5
BuildRequires:  glibc-static
BuildRequires:  hivex
BuildRequires:  linux
BuildRequires:  libtool
BuildRequires:  ocaml
BuildRequires:  ocaml-devel
BuildRequires:  ocaml-findlib
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(com_err)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  perl
BuildRequires:  e2fsprogs
BuildRequires:  zstd

Requires:       cpio
Requires:       dnf5
Requires:       e2fsprogs
Requires:       rpm
Requires:       xz
Requires:       zstd

%description
Supermin is a tool for building supermin appliances. These are tiny
appliances which get fully instantiated on the fly when you need to
boot one of them. libguestfs uses supermin to construct its appliance.

%prep -a
autoreconf -fi

%check
rpm --eval 'RPM database: %{_dbpath} (%{_db_backend})'
# The offline suite prepares appliances from installed RPMs and builds
# both chroots and ext2 images, including their kernel and initrd.
%make_build check

%files
%doc README examples
%license COPYING
%{_bindir}/supermin
%{_mandir}/man1/supermin.1*

%changelog
%autochangelog
