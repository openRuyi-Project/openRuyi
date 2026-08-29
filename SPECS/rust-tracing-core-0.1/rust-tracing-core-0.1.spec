# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing-core
%global full_version 0.1.36
%global pkgname tracing-core-0.1

Name:           rust-tracing-core-0.1
Version:        0.1.36
Release:        %autorelease
Summary:        Rust crate "tracing-core"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:db97caf9d906fbde555dd62fa95ddba9eecfd14cb388e4f491a66d74cd5fb79a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tracing-core"

%package     -n %{name}+default
Summary:        Core primitives for application-level tracing - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(valuable-0.1/std) >= 0.1.0
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tracing-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Core primitives for application-level tracing - feature "once_cell" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.13.0
Provides:       crate(%{pkgname}/once-cell) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust tracing-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std" feature.

%package     -n %{name}+valuable
Summary:        Core primitives for application-level tracing - feature "valuable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(valuable-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/valuable) = %{version}

%description -n %{name}+valuable
This metapackage enables feature "valuable" for the Rust tracing-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
