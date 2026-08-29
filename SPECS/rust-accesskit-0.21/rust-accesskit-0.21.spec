# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name accesskit
%global full_version 0.21.1
%global pkgname accesskit-0.21

Name:           rust-accesskit-0.21
Version:        0.21.1
Release:        %autorelease
Summary:        Rust crate "accesskit"
License:        MIT OR Apache-2.0
URL:            https://github.com/AccessKit/accesskit
#!RemoteAsset:  sha256:cf203f9d3bd8f29f98833d1fbef628df18f759248a547e7e01cfbf63cda36a99
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "accesskit"

%package     -n %{name}+enumn
Summary:        UI accessibility infrastructure across platforms - feature "enumn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(enumn-0.1/default) >= 0.1.6
Provides:       crate(%{pkgname}/enumn) = %{version}

%description -n %{name}+enumn
This metapackage enables feature "enumn" for the Rust accesskit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pyo3
Summary:        UI accessibility infrastructure across platforms - feature "pyo3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-0.26/default) >= 0.26.0
Provides:       crate(%{pkgname}/pyo3) = %{version}

%description -n %{name}+pyo3
This metapackage enables feature "pyo3" for the Rust accesskit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars
Summary:        UI accessibility infrastructure across platforms - feature "schemars"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(schemars-0.8/default) >= 0.8.7
Provides:       crate(%{pkgname}/schemars) = %{version}

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust accesskit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        UI accessibility infrastructure across platforms - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/enumn) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust accesskit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
