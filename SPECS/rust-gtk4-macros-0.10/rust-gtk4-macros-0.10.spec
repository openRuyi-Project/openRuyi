# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gtk4-macros
%global full_version 0.10.3
%global pkgname gtk4-macros-0.10

Name:           rust-gtk4-macros-0.10
Version:        0.10.3
Release:        %autorelease
Summary:        Rust crate "gtk4-macros"
License:        MIT
URL:            https://gtk-rs.org/gtk4-rs
#!RemoteAsset:  sha256:3ccfb5a14a3d941244815d5f8101fa12d4577b59cc47245778d8d907b0003e42
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro-crate-3/default) >= 3.3.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/blueprint) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gtk4-macros"

%package     -n %{name}+quick-xml
Summary:        Macros helpers for GTK 4 bindings - feature "quick-xml" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quick-xml-0.38/default) >= 0.38.0
Provides:       crate(%{pkgname}/quick-xml) = %{version}
Provides:       crate(%{pkgname}/xml-validation) = %{version}

%description -n %{name}+quick-xml
This metapackage enables feature "quick-xml" for the Rust gtk4-macros crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "xml_validation" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
