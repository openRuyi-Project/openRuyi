# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rstest_macros
%global full_version 0.25.0
%global pkgname rstest-macros-0.25

Name:           rust-rstest-macros-0.25
Version:        0.25.0
Release:        %autorelease
Summary:        Rust crate "rstest_macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/la10736/rstest
#!RemoteAsset:  sha256:1f168d99749d307be9de54d23fd226628d99768225ef08f6ffb52e0182a27746
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.1
Requires:       crate(glob-0.3/default) >= 0.3.2
Requires:       crate(proc-macro2-1.0/default) >= 1.0.95
Requires:       crate(quote-1.0/default) >= 1.0.40
Requires:       crate(regex-1.0/default) >= 1.11.1
Requires:       crate(relative-path-1.0/default) >= 1.9.3
Requires:       crate(rustc-version-0.4/default) >= 0.4.1
Requires:       crate(syn-2.0/default) >= 2.0.104
Requires:       crate(syn-2.0/extra-traits) >= 2.0.104
Requires:       crate(syn-2.0/full) >= 2.0.104
Requires:       crate(syn-2.0/parsing) >= 2.0.104
Requires:       crate(syn-2.0/visit) >= 2.0.104
Requires:       crate(syn-2.0/visit-mut) >= 2.0.104
Requires:       crate(unicode-ident-1.0/default) >= 1.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/async-timeout)

%description
It use procedural macro to implement fixtures and table based tests.
Source code for takopackized Rust crate "rstest_macros"

%package     -n %{name}+crate-name
Summary:        Rust fixture based test framework - feature "crate-name"
Requires:       crate(%{pkgname})
Requires:       crate(proc-macro-crate-3.0/default) >= 3.3.0
Provides:       crate(%{pkgname}/crate-name)

%description -n %{name}+crate-name
It use procedural macro to implement fixtures and table based tests.
This metapackage enables feature "crate-name" for the Rust rstest_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rust fixture based test framework - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async-timeout)
Requires:       crate(%{pkgname}/crate-name)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
It use procedural macro to implement fixtures and table based tests.
This metapackage enables feature "default" for the Rust rstest_macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
