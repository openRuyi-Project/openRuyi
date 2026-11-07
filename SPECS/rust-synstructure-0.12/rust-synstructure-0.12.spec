# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name synstructure
%global full_version 0.12.6
%global pkgname synstructure-0.12

Name:           rust-synstructure-0.12
Version:        0.12.6
Release:        %autorelease
Summary:        Rust crate "synstructure"
License:        MIT
URL:            https://github.com/mystor/synstructure
#!RemoteAsset:  sha256:f36bdaa60a83aca3921b5259d5400cbf5e90fc51931376a9bd4a0eb79aa7210f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1) >= 1.0.0
Requires:       crate(quote-1) >= 1.0.0
Requires:       crate(syn-1/clone-impls) >= 1.0.0
Requires:       crate(syn-1/derive) >= 1.0.0
Requires:       crate(syn-1/extra-traits) >= 1.0.0
Requires:       crate(syn-1/parsing) >= 1.0.0
Requires:       crate(syn-1/printing) >= 1.0.0
Requires:       crate(syn-1/visit) >= 1.0.0
Requires:       crate(unicode-xid-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "synstructure"

%package     -n %{name}+proc-macro
Summary:        Helper methods and macros for custom derives - feature "proc-macro" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro2-1/proc-macro) >= 1.0.0
Requires:       crate(quote-1/proc-macro) >= 1.0.0
Requires:       crate(syn-1/clone-impls) >= 1.0.0
Requires:       crate(syn-1/derive) >= 1.0.0
Requires:       crate(syn-1/extra-traits) >= 1.0.0
Requires:       crate(syn-1/parsing) >= 1.0.0
Requires:       crate(syn-1/printing) >= 1.0.0
Requires:       crate(syn-1/proc-macro) >= 1.0.0
Requires:       crate(syn-1/visit) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/proc-macro) = %{version}

%description -n %{name}+proc-macro
This metapackage enables feature "proc-macro" for the Rust synstructure crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
