# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name darling
%global full_version 0.20.11
%global pkgname darling-0.20

Name:           rust-darling-0.20
Version:        0.20.11
Release:        %autorelease
Summary:        Rust crate "darling"
License:        MIT
URL:            https://github.com/TedDriggs/darling
#!RemoteAsset:  sha256:fc7f46116c46ff9ab3eb1597a45688b6715c6e628b5c133e288e709a29bcb4ee
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-core-0.20/default) >= 0.20.11
Requires:       crate(darling-macro-0.20/default) >= 0.20.11
Provides:       crate(darling) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "darling"

%package     -n %{name}+diagnostics
Summary:        Proc-macro library for reading attributes into structs when implementing custom derives - feature "diagnostics"
Requires:       crate(%{pkgname})
Requires:       crate(darling-core-0.20/diagnostics) >= 0.20.11
Provides:       crate(%{pkgname}/diagnostics)

%description -n %{name}+diagnostics
This metapackage enables feature "diagnostics" for the Rust darling crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+suggestions
Summary:        Proc-macro library for reading attributes into structs when implementing custom derives - feature "suggestions" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(darling-core-0.20/suggestions) >= 0.20.11
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/suggestions)

%description -n %{name}+suggestions
This metapackage enables feature "suggestions" for the Rust darling crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
