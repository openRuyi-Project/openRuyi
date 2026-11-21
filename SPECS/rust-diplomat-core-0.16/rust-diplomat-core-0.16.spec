# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name diplomat_core
%global full_version 0.16.0
%global pkgname diplomat-core-0.16

Name:           rust-diplomat-core-0.16
Version:        0.16.0
Release:        %autorelease
Summary:        Rust crate "diplomat_core"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-diplomat/diplomat
#!RemoteAsset:  sha256:f4ede23809e2fcc555d8b2e10ffa7a1c31331ebca8e5477f4f2b48ab8a0a9a6b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(proc-macro2-1/span-locations) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(smallvec-1/default) >= 1.9.0
Requires:       crate(strck-1/default) >= 1.0.0
Requires:       crate(strck-1/ident) >= 1.0.0
Requires:       crate(syn-3/default) >= 3.0.0
Requires:       crate(syn-3/extra-traits) >= 3.0.0
Requires:       crate(syn-3/full) >= 3.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "diplomat_core"

%package     -n %{name}+annotate-snippets
Summary:        Shared utilities between Diplomat macros and code generation - feature "annotate-snippets" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(annotate-snippets-0.12/default) >= 0.12.13
Provides:       crate(%{pkgname}/annotate-snippets) = %{version}
Provides:       crate(%{pkgname}/pretty-print) = %{version}

%description -n %{name}+annotate-snippets
This metapackage enables feature "annotate-snippets" for the Rust diplomat_core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "pretty-print" feature.

%package     -n %{name}+either
Summary:        Shared utilities between Diplomat macros and code generation - feature "either" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(either-1) >= 1.9.0
Provides:       crate(%{pkgname}/either) = %{version}
Provides:       crate(%{pkgname}/hir) = %{version}

%description -n %{name}+either
This metapackage enables feature "either" for the Rust diplomat_core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "hir" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
