# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing-flame
%global full_version 0.2.0
%global pkgname tracing-flame-0.2

Name:           rust-tracing-flame-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "tracing-flame"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:0bae117ee14789185e129aaee5d93750abe67fdc5a9a62650452bfe4e122a3a9
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1.0/default) >= 1.3.0
Requires:       crate(tracing-0.1/std) >= 0.1.12
Requires:       crate(tracing-subscriber-0.3/fmt) >= 0.3.0
Requires:       crate(tracing-subscriber-0.3/registry) >= 0.3.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "tracing-flame"

%package     -n %{name}+smallvec
Summary:        Tracing layer for creating flamegraphs from span timings - feature "smallvec" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(tracing-subscriber-0.3/fmt) >= 0.3.0
Requires:       crate(tracing-subscriber-0.3/registry) >= 0.3.0
Requires:       crate(tracing-subscriber-0.3/smallvec) >= 0.3.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/smallvec)

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust tracing-flame crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
