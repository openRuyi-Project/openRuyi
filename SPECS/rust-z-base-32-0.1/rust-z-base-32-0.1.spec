# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name z-base-32
%global full_version 0.1.5
%global pkgname z-base-32-0.1

Name:           rust-z-base-32-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "z-base-32"
License:        MIT
URL:            https://github.com/matusf/z-base-32
#!RemoteAsset:  sha256:44f94003b56f8f812c88dd188d9bafc71d8e3786fd04812c2d8cdb176810ceb4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "z-base-32"

%package     -n %{name}+cli
Summary:        Z-base-32: human-oriented base-32 encoding - feature "cli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/default) >= 4.0.0
Requires:       crate(clap-4/derive) >= 4.0.0
Provides:       crate(%{pkgname}/cli) = %{version}

%description -n %{name}+cli
This metapackage enables feature "cli" for the Rust z-base-32 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+python
Summary:        Z-base-32: human-oriented base-32 encoding - feature "python"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-0.29/default) >= 0.29.0
Requires:       crate(pyo3-0.29/extension-module) >= 0.29.0
Provides:       crate(%{pkgname}/python) = %{version}

%description -n %{name}+python
This metapackage enables feature "python" for the Rust z-base-32 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
