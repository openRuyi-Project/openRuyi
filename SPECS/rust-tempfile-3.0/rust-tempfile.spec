# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tempfile
%global full_version 3.27.0
%global pkgname tempfile-3.0

Name:           rust-tempfile-3.0
Version:        3.27.0
Release:        %autorelease
Summary:        Rust crate "tempfile"
License:        MIT OR Apache-2.0
URL:            https://stebalien.com/projects/tempfile-rs/
#!RemoteAsset:  sha256:32497e9a4c7b38532efcdebeef879707aa9f794296a4f0244f6f69e9bc8574bd
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fastrand-2.0/default) >= 2.3.0
Requires:       crate(once-cell-1.0/std) >= 1.21.4
Requires:       crate(rustix-1.0/default) >= 1.1.4
Requires:       crate(rustix-1.0/fs) >= 1.1.4
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/nightly)

%description
Source code for takopackized Rust crate "tempfile"

%package     -n %{name}+getrandom
Summary:        Managing temporary files and directories - feature "getrandom" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(getrandom-0.4) >= 0.4.2
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust tempfile crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
