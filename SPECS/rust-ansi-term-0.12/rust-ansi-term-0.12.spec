# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ansi_term
%global full_version 0.12.1
%global pkgname ansi-term-0.12

Name:           rust-ansi-term-0.12
Version:        0.12.1
Release:        %autorelease
Summary:        Rust crate "ansi_term"
License:        MIT
URL:            https://github.com/ogham/rust-ansi-term
#!RemoteAsset:  sha256:d52a9bb7ec0cf484c551830a7ce27bd20d67eac647e1befb56b0be4ee39a55d2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(winapi-0.3/consoleapi) >= 0.3.4
Requires:       crate(winapi-0.3/default) >= 0.3.4
Requires:       crate(winapi-0.3/errhandlingapi) >= 0.3.4
Requires:       crate(winapi-0.3/fileapi) >= 0.3.4
Requires:       crate(winapi-0.3/handleapi) >= 0.3.4
Requires:       crate(winapi-0.3/processenv) >= 0.3.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ansi_term"

%package     -n %{name}+serde
Summary:        ANSI terminal colours and styles (bold, underline) - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.90
Requires:       crate(serde-1/derive) >= 1.0.90
Provides:       crate(%{pkgname}/derive-serde-style) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ansi_term crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive_serde_style" feature.

%files
%license LICENCE
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
