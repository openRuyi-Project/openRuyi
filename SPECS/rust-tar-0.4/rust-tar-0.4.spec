# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tar
%global full_version 0.4.46
%global pkgname tar-0.4

Name:           rust-tar-0.4
Version:        0.4.46
Release:        %autorelease
Summary:        Rust crate "tar"
License:        MIT OR Apache-2.0
URL:            https://github.com/composefs/tar-rs
#!RemoteAsset:  sha256:3f6221d9a6003c78398e3b239969f352578258df48c8eb051caadae0015bc840
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(filetime-0.2/default) >= 0.2.8
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}

%description
This library does not currently handle compression, but it is abstract over all I/O readers and writers. Additionally, great lengths are taken to ensure that the entire contents are never required to be entirely resident in memory all at once.
Source code for takopackized Rust crate "tar"

%package     -n %{name}+xattr
Summary:        A TAR file reader and writer - feature "xattr" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(xattr-1/default) >= 1.1.3
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/xattr) = %{version}

%description -n %{name}+xattr
This library does not currently handle compression, but it is abstract over all I/O readers and writers. Additionally, great lengths are taken to ensure that the entire contents are never required to be entirely resident in memory all at once.
This metapackage enables feature "xattr" for the Rust tar crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
