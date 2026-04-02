# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lazycell
%global full_version 1.3.0
%global pkgname lazycell-1.0

Name:           rust-lazycell-1.0
Version:        1.3.0
Release:        %autorelease
Summary:        Rust crate "lazycell"
License:        MIT/Apache-2.0
URL:            https://github.com/indiv0/lazycell
#!RemoteAsset:  sha256:830d08ce1d1d941e6b30645f1a0eb5643013d835ce3779a5fc208261dbe10f55
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)

%description
Source code for takopackized Rust crate "lazycell"

%package     -n %{name}+clippy
Summary:        Library providing a lazily filled Cell struct - feature "clippy"
Requires:       crate(%{pkgname})
Requires:       crate(clippy-0.0.0/default) >= 0.0.0
Provides:       crate(%{pkgname}/clippy)

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust lazycell crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly-testing
Summary:        Library providing a lazily filled Cell struct - feature "nightly-testing"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/clippy)
Requires:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/nightly-testing)

%description -n %{name}+nightly-testing
This metapackage enables feature "nightly-testing" for the Rust lazycell crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Library providing a lazily filled Cell struct - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust lazycell crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
