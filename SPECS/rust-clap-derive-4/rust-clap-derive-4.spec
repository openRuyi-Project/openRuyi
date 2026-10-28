# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_derive
%global full_version 4.6.4
%global pkgname clap-derive-4

Name:           rust-clap-derive-4
Version:        4.6.4
Release:        %autorelease
Summary:        Rust crate "clap_derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap
#!RemoteAsset:  sha256:d012d2b9d65aca7f18f4d9878a045bc17899bba951561ba5ec3c2ba1eed9a061
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-3/default) >= 3.0.2
Requires:       crate(syn-3/full) >= 3.0.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/deprecated) = %{version}
Provides:       crate(%{pkgname}/raw-deprecated) = %{version}
Provides:       crate(%{pkgname}/unstable-v5) = %{version}

%description
Source code for takopackized Rust crate "clap_derive"

%package     -n %{name}+unstable-markdown
Summary:        Parse command line argument by defining a struct, derive crate - feature "unstable-markdown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anstyle-1/default) >= 1.0.14
Requires:       crate(pulldown-cmark-0.13) >= 0.13.3
Provides:       crate(%{pkgname}/unstable-markdown) = %{version}

%description -n %{name}+unstable-markdown
This metapackage enables feature "unstable-markdown" for the Rust clap_derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
