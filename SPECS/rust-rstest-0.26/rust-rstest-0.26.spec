# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rstest
%global full_version 0.26.0
%global pkgname rstest-0.26

Name:           rust-rstest-0.26
Version:        0.26.0
Release:        %autorelease
Summary:        Rust crate "rstest"
License:        MIT OR Apache-2.0
URL:            https://github.com/la10736/rstest
#!RemoteAsset:  sha256:c721f131ce14d37eb6365d6848fe38703fff9b961c83038a926673e91769d1ef
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rstest-macros-0.26) >= 0.26.0

Provides:       crate(%{pkgname}) = %{version}

%description
It use procedural macro to implement fixtures and table based tests.
Source code for takopackized Rust crate "rstest"

%package     -n %{name}+async-timeout
Summary:        Rust fixture based test framework - feature "async-timeout"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-timer-3/default) >= 3.0.3
Requires:       crate(futures-util-0.3/default) >= 0.3.30
Requires:       crate(rstest-macros-0.26/async-timeout) >= 0.26.0
Provides:       crate(%{pkgname}/async-timeout) = %{version}

%description -n %{name}+async-timeout
It use procedural macro to implement fixtures and table based tests.
This metapackage enables feature "async-timeout" for the Rust rstest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crate-name
Summary:        Rust fixture based test framework - feature "crate-name"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rstest-macros-0.26/crate-name) >= 0.26.0
Provides:       crate(%{pkgname}/crate-name) = %{version}

%description -n %{name}+crate-name
It use procedural macro to implement fixtures and table based tests.
This metapackage enables feature "crate-name" for the Rust rstest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rust fixture based test framework - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-timeout) = %{version}
Requires:       crate(%{pkgname}/crate-name) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
It use procedural macro to implement fixtures and table based tests.
This metapackage enables feature "default" for the Rust rstest crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
