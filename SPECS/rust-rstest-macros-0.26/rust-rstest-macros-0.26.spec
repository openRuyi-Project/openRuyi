# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rstest_macros
%global full_version 0.26.0
%global pkgname rstest-macros-0.26

Name:           rust-rstest-macros-0.26
Version:        0.26.0
Release:        %autorelease
Summary:        Rust crate "rstest_macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/la10736/rstest
#!RemoteAsset:  sha256:af1954176ab4f2ced085ad2c7a1b257be46299aa0093dabaa4e078b4af25eb3c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(glob-0.3/default) >= 0.3.1
Requires:       crate(proc-macro2-1/default) >= 1.0.86
Requires:       crate(quote-1/default) >= 1.0.37
Requires:       crate(regex-1/default) >= 1.10.6
Requires:       crate(relative-path-1/default) >= 1.9.3
Requires:       crate(rustc-version-0.4) >= 0.4.1
Requires:       crate(syn-2/default) >= 2.0.79
Requires:       crate(syn-2/extra-traits) >= 2.0.79
Requires:       crate(syn-2/full) >= 2.0.79
Requires:       crate(syn-2/parsing) >= 2.0.79
Requires:       crate(syn-2/visit) >= 2.0.79
Requires:       crate(syn-2/visit-mut) >= 2.0.79
Requires:       crate(unicode-ident-1/default) >= 1.0.13

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/async-timeout) = %{version}

%description
It use procedural macro to implement fixtures and table based tests.
Source code for takopackized Rust crate "rstest_macros"

%package     -n %{name}+crate-name
Summary:        Rust fixture based test framework - feature "crate-name"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro-crate-3/default) >= 3.2.0
Provides:       crate(%{pkgname}/crate-name) = %{version}

%description -n %{name}+crate-name
It use procedural macro to implement fixtures and table based tests.
This metapackage enables feature "crate-name" for the Rust rstest_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rust fixture based test framework - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-timeout) = %{version}
Requires:       crate(%{pkgname}/crate-name) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
It use procedural macro to implement fixtures and table based tests.
This metapackage enables feature "default" for the Rust rstest_macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
