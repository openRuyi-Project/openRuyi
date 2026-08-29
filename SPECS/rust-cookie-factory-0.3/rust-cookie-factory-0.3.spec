# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cookie-factory
%global full_version 0.3.3
%global pkgname cookie-factory-0.3

Name:           rust-cookie-factory-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "cookie-factory"
License:        MIT
URL:            https://github.com/rust-bakery/cookie-factory
#!RemoteAsset:  sha256:9885fa71e26b8ab7855e2ec7cae6e9b380edff76cd052e07c683a0319d51b3a2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "cookie-factory"

%package     -n %{name}+default
Summary:        Nom inspired serialization library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust cookie-factory crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Nom inspired serialization library - feature "futures" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3/default) >= 0.3.16
Provides:       crate(%{pkgname}/async) = %{version}
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust cookie-factory crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "async" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
