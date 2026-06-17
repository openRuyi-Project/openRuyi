# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name globset
%global full_version 0.4.18
%global pkgname globset-0.4

Name:           rust-globset-0.4
Version:        0.4.18
Release:        %autorelease
Summary:        Rust crate "globset"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/ripgrep/tree/master/crates/globset
#!RemoteAsset:  sha256:52dfc19153a48bde0cbd630453615c8151bce3a5adfac7a0aebfbf0a1e1f57e3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aho-corasick-1/default) >= 1.1.1
Requires:       crate(bstr-1/std) >= 1.6.2
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.0
Requires:       crate(regex-automata-0.4/meta) >= 0.4.0
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.0
Requires:       crate(regex-automata-0.4/perf) >= 0.4.0
Requires:       crate(regex-automata-0.4/std) >= 0.4.0
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.0
Requires:       crate(regex-syntax-0.8/std) >= 0.8.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/simd-accel) = %{version}

%description
Glob set matching is the process of matching one or more glob patterns against a single candidate path simultaneously, and returning all of the globs that matched.
Source code for takopackized Rust crate "globset"

%package     -n %{name}+arbitrary
Summary:        Cross platform single glob and glob set matching - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.3.2
Requires:       crate(arbitrary-1/derive) >= 1.3.2
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
Glob set matching is the process of matching one or more glob patterns against a single candidate path simultaneously, and returning all of the globs that matched.
This metapackage enables feature "arbitrary" for the Rust globset crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Cross platform single glob and glob set matching - feature "log" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.20
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
Glob set matching is the process of matching one or more glob patterns against a single candidate path simultaneously, and returning all of the globs that matched.
This metapackage enables feature "log" for the Rust globset crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+serde
Summary:        Cross platform single glob and glob set matching - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.188
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde1) = %{version}

%description -n %{name}+serde
Glob set matching is the process of matching one or more glob patterns against a single candidate path simultaneously, and returning all of the globs that matched.
This metapackage enables feature "serde" for the Rust globset crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde1" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
