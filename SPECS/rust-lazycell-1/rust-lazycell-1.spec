# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lazycell
%global full_version 1.3.0
%global pkgname lazycell-1

Name:           rust-lazycell-1
Version:        1.3.0
Release:        %autorelease
Summary:        Rust crate "lazycell"
License:        MIT OR Apache-2.0
URL:            https://github.com/indiv0/lazycell
#!RemoteAsset:  sha256:830d08ce1d1d941e6b30645f1a0eb5643013d835ce3779a5fc208261dbe10f55
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "lazycell"

%package     -n %{name}+clippy
Summary:        Library providing a lazily filled Cell struct - feature "clippy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clippy-0.0.0/default) >= 0.0.0
Provides:       crate(%{pkgname}/clippy) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust lazycell crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly-testing
Summary:        Library providing a lazily filled Cell struct - feature "nightly-testing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clippy) = %{version}
Requires:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/nightly-testing) = %{version}

%description -n %{name}+nightly-testing
This metapackage enables feature "nightly-testing" for the Rust lazycell crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Library providing a lazily filled Cell struct - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust lazycell crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
