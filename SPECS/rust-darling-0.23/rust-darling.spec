# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name darling
%global full_version 0.23.0
%global pkgname darling-0.23

Name:           rust-darling-0.23
Version:        0.23.0
Release:        %autorelease
Summary:        Rust crate "darling"
License:        MIT
URL:            https://github.com/TedDriggs/darling
#!RemoteAsset:  sha256:25ae13da2f202d56bd7f91c25fba009e7717a1e4a1cc98a76d844b65ae912e9d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-core-0.23/default) >= 0.23.0
Requires:       crate(darling-macro-0.23/default) >= 0.23.0
Provides:       crate(darling) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "darling"

%package     -n %{name}+diagnostics
Summary:        Proc-macro library for reading attributes into structs when implementing custom derives - feature "diagnostics"
Requires:       crate(%{pkgname})
Requires:       crate(darling-core-0.23/diagnostics) >= 0.23.0
Provides:       crate(%{pkgname}/diagnostics)

%description -n %{name}+diagnostics
This metapackage enables feature "diagnostics" for the Rust darling crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Proc-macro library for reading attributes into structs when implementing custom derives - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(darling-core-0.23/serde) >= 0.23.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust darling crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+suggestions
Summary:        Proc-macro library for reading attributes into structs when implementing custom derives - feature "suggestions" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(darling-core-0.23/suggestions) >= 0.23.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/suggestions)

%description -n %{name}+suggestions
This metapackage enables feature "suggestions" for the Rust darling crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
