# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-error2
%global full_version 2.0.1
%global pkgname proc-macro-error2-2

Name:           rust-proc-macro-error2-2
Version:        2.0.1
Release:        %autorelease
Summary:        Rust crate "proc-macro-error2"
License:        MIT OR Apache-2.0
URL:            https://github.com/GnomedDev/proc-macro-error-2
#!RemoteAsset:  sha256:11ec05c52be0a07b08061f7dd003e7d7092e0472bc731b4af7bb1ef876109802
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro-error-attr2-2/default) >= 2.0.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "proc-macro-error2"

%package     -n %{name}+syn-error
Summary:        Almost drop-in replacement to panics in proc-macros - feature "syn-error" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-2) >= 2.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/syn-error) = %{version}

%description -n %{name}+syn-error
This metapackage enables feature "syn-error" for the Rust proc-macro-error2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
