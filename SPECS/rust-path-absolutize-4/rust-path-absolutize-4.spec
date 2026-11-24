# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name path-absolutize
%global full_version 4.0.1
%global pkgname path-absolutize-4

Name:           rust-path-absolutize-4
Version:        4.0.1
Release:        %autorelease
Summary:        Rust crate "path-absolutize"
License:        MIT
URL:            https://magiclen.org/path-absolutize
#!RemoteAsset:  sha256:f808742975794703469f67a28dd14b1d1009a1743c18b0353b4b951dbb0068ad
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(path-dedot-4/default) >= 4.0.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "path-absolutize"

%package     -n %{name}+fixed-workdir
Summary:        Extending `Path` and `PathBuf` in order to get an absolute path and remove the containing dots - feature "fixed_workdir"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(path-dedot-4/fixed-workdir) >= 4.0.1
Provides:       crate(%{pkgname}/fixed-workdir) = %{version}

%description -n %{name}+fixed-workdir
This metapackage enables feature "fixed_workdir" for the Rust path-absolutize crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
