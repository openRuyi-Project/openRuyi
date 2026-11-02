# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_fmt
%global full_version 1.1.0
%global pkgname serde-fmt-1

Name:           rust-serde-fmt-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "serde_fmt"
License:        Apache-2.0 OR MIT
URL:            https://github.com/KodrAus/serde_fmt.git
#!RemoteAsset:  sha256:6e497af288b3b95d067a23a4f749f2861121ffcb2f6d8379310dcda040c345ed
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-core-1) >= 1.0.220

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde_fmt"

%package     -n %{name}+std
Summary:        Write any serde::Serialize using the standard formatting APIs - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1/std) >= 1.0.220
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust serde_fmt crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
