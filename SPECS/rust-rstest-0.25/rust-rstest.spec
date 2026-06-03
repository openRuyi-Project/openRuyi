# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rstest
%global full_version 0.25.0
%global pkgname rstest-0.25

Name:           rust-rstest-0.25
Version:        0.25.0
Release:        %autorelease
Summary:        Rust crate "rstest"
License:        MIT OR Apache-2.0
URL:            https://github.com/la10736/rstest
#!RemoteAsset:  sha256:6fc39292f8613e913f7df8fa892b8944ceb47c247b78e1b1ae2f09e019be789d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rstest-macros-0.25) >= 0.25.0
Requires:       crate(rustc-version-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname})

%description
It use procedural macro to implement fixtures and table based tests.
Source code for takopackized Rust crate "rstest"

%package     -n %{name}+async-timeout
Summary:        Rust fixture based test framework - feature "async-timeout"
Requires:       crate(%{pkgname})
Requires:       crate(futures-timer-3.0/default) >= 3.0.3
Requires:       crate(futures-util-0.3/default) >= 0.3.31
Requires:       crate(rstest-macros-0.25/async-timeout) >= 0.25.0
Provides:       crate(%{pkgname}/async-timeout)

%description -n %{name}+async-timeout
It use procedural macro to implement fixtures and table based tests.
This metapackage enables feature "async-timeout" for the Rust rstest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crate-name
Summary:        Rust fixture based test framework - feature "crate-name"
Requires:       crate(%{pkgname})
Requires:       crate(rstest-macros-0.25/crate-name) >= 0.25.0
Provides:       crate(%{pkgname}/crate-name)

%description -n %{name}+crate-name
It use procedural macro to implement fixtures and table based tests.
This metapackage enables feature "crate-name" for the Rust rstest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rust fixture based test framework - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async-timeout)
Requires:       crate(%{pkgname}/crate-name)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
It use procedural macro to implement fixtures and table based tests.
This metapackage enables feature "default" for the Rust rstest crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
