# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ratatui-termion
%global full_version 0.1.1
%global pkgname ratatui-termion-0.1

Name:           rust-ratatui-termion-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "ratatui-termion"
License:        MIT
URL:            https://ratatui.rs
#!RemoteAsset:  sha256:5c16cc35a9d9114e0b2bb4b22018b96ae7f5fe60e2595dc73e622b4e78624835
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(instability-0.3/default) >= 0.3.0
Requires:       crate(ratatui-core-0.1/default) >= 0.1.1
Requires:       crate(termion-4/default) >= 4.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}
Provides:       crate(%{pkgname}/unstable-backend-writer) = %{version}

%description
Source code for takopackized Rust crate "ratatui-termion"

%package     -n %{name}+document-features
Summary:        Termion backend for the Ratatui Terminal UI library - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust ratatui-termion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scrolling-regions
Summary:        Termion backend for the Ratatui Terminal UI library - feature "scrolling-regions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ratatui-core-0.1/scrolling-regions) >= 0.1.1
Provides:       crate(%{pkgname}/scrolling-regions) = %{version}

%description -n %{name}+scrolling-regions
This metapackage enables feature "scrolling-regions" for the Rust ratatui-termion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Termion backend for the Ratatui Terminal UI library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(termion-4/serde) >= 4.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ratatui-termion crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
