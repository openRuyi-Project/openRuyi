# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name palette_derive
%global full_version 0.7.6
%global pkgname palette-derive-0.7

Name:           rust-palette-derive-0.7
Version:        0.7.6
Release:        %autorelease
Summary:        Rust crate "palette_derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/Ogeon/palette
#!RemoteAsset:  sha256:f5030daf005bface118c096f510ffb781fc28f9ab6a32ab224d8631be6851d30
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(by-address-1/default) >= 1.2.1
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/clone-impls) >= 2.0.13
Requires:       crate(syn-2/derive) >= 2.0.13
Requires:       crate(syn-2/extra-traits) >= 2.0.13
Requires:       crate(syn-2/parsing) >= 2.0.13
Requires:       crate(syn-2/printing) >= 2.0.13
Requires:       crate(syn-2/proc-macro) >= 2.0.13
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "palette_derive"

%package     -n %{name}+find-crate
Summary:        Automatically implement traits from the palette crate - feature "find-crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(find-crate-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/find-crate) = %{version}

%description -n %{name}+find-crate
This metapackage enables feature "find-crate" for the Rust palette_derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
