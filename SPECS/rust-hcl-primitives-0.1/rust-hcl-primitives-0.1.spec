# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hcl-primitives
%global full_version 0.1.12
%global pkgname hcl-primitives-0.1

Name:           rust-hcl-primitives-0.1
Version:        0.1.12
Release:        %autorelease
Summary:        Rust crate "hcl-primitives"
License:        MIT OR Apache-2.0
URL:            https://github.com/martinohmann/hcl-rs
#!RemoteAsset:  sha256:bd662a8afeca01b5b5318f35baed70017b9f854bfa38bdcdadb87de946a49071
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(itoa-1/default) >= 1.0.14
Requires:       crate(ryu-1/default) >= 1.0.18
Requires:       crate(unicode-ident-1/default) >= 1.0.14

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "hcl-primitives"

%package     -n %{name}+perf
Summary:        Primitives used by the HCL sub-languages - feature "perf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(kstring-2/default) >= 2.0.2
Requires:       crate(kstring-2/max-inline) >= 2.0.2
Provides:       crate(%{pkgname}/perf) = %{version}

%description -n %{name}+perf
This metapackage enables feature "perf" for the Rust hcl-primitives crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Primitives used by the HCL sub-languages - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(kstring-2/max-inline) >= 2.0.2
Requires:       crate(kstring-2/serde) >= 2.0.2
Requires:       crate(serde-1/alloc) >= 1.0.217
Requires:       crate(serde-1/derive) >= 1.0.217
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust hcl-primitives crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Primitives used by the HCL sub-languages - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.217
Requires:       crate(serde-1/derive) >= 1.0.217
Requires:       crate(serde-1/std) >= 1.0.217
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust hcl-primitives crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
