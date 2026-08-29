# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ratatui-termwiz
%global full_version 0.1.1
%global pkgname ratatui-termwiz-0.1

Name:           rust-ratatui-termwiz-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "ratatui-termwiz"
License:        MIT
URL:            https://ratatui.rs
#!RemoteAsset:  sha256:386b8ff8f74ed749509391c56d549761a2fcdb408e1f42e467286bcb7dac8967
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ratatui-core-0.1/default) >= 0.1.1
Requires:       crate(termwiz-0.23/default) >= 0.23.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ratatui-termwiz"

%package     -n %{name}+document-features
Summary:        Termwiz backend for the Ratatui Terminal UI library - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust ratatui-termwiz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scrolling-regions
Summary:        Termwiz backend for the Ratatui Terminal UI library - feature "scrolling-regions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ratatui-core-0.1/scrolling-regions) >= 0.1.1
Provides:       crate(%{pkgname}/scrolling-regions) = %{version}

%description -n %{name}+scrolling-regions
This metapackage enables feature "scrolling-regions" for the Rust ratatui-termwiz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Termwiz backend for the Ratatui Terminal UI library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(termwiz-0.23/use-serde) >= 0.23.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ratatui-termwiz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+underline-color
Summary:        Termwiz backend for the Ratatui Terminal UI library - feature "underline-color"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ratatui-core-0.1/underline-color) >= 0.1.1
Provides:       crate(%{pkgname}/underline-color) = %{version}

%description -n %{name}+underline-color
This metapackage enables feature "underline-color" for the Rust ratatui-termwiz crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
