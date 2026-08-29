# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cbindgen
%global full_version 0.29.2
%global pkgname cbindgen-0.29

Name:           rust-cbindgen-0.29
Version:        0.29.2
Release:        %autorelease
Summary:        Rust crate "cbindgen"
License:        MPL-2.0
URL:            https://github.com/mozilla/cbindgen
#!RemoteAsset:  sha256:befbfd072a8e81c02f8c507aefce431fe5e7d051f83d48a23ffc9b9fe5a11799
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(indexmap-2/default) >= 2.1.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(proc-macro2-1/default) >= 1.0.60
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.103
Requires:       crate(serde-1/std) >= 1.0.103
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(syn-2/clone-impls) >= 2.0.85
Requires:       crate(syn-2/extra-traits) >= 2.0.85
Requires:       crate(syn-2/fold) >= 2.0.85
Requires:       crate(syn-2/full) >= 2.0.85
Requires:       crate(syn-2/parsing) >= 2.0.85
Requires:       crate(syn-2/printing) >= 2.0.85
Requires:       crate(tempfile-3/default) >= 3.0.0
Requires:       crate(toml-0.9/parse) >= 0.9.0
Requires:       crate(toml-0.9/serde) >= 0.9.0
Requires:       crate(toml-0.9/std) >= 0.9.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unstable-ir) = %{version}

%description
Source code for takopackized Rust crate "cbindgen"

%package     -n %{name}+clap
Summary:        Generating C bindings to Rust code - feature "clap" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/default) >= 4.3.0
Provides:       crate(%{pkgname}/clap) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust cbindgen crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
