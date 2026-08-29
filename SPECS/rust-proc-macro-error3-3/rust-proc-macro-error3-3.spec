# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-error3
%global full_version 3.0.2
%global pkgname proc-macro-error3-3

Name:           rust-proc-macro-error3-3
Version:        3.0.2
Release:        %autorelease
Summary:        Rust crate "proc-macro-error3"
License:        MIT OR Apache-2.0
URL:            https://github.com/gamma0987/proc-macro-error3
#!RemoteAsset:  sha256:5ee475e440453418ff1335189eddf7101ba502cd818ab7ae04209bc83aa925aa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro-error-attr3-3/default) >= 3.0.2
Requires:       crate(proc-macro2-1/default) >= 1.0.74
Requires:       crate(quote-1/default) >= 1.0.35

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/ui-tests) = %{version}

%description
Source code for takopackized Rust crate "proc-macro-error3"

%package     -n %{name}+syn-error
Summary:        Almost drop-in replacement to panics in proc-macros - feature "syn-error" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-2) >= 2.0.46
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/syn-error) = %{version}

%description -n %{name}+syn-error
This metapackage enables feature "syn-error" for the Rust proc-macro-error3 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
