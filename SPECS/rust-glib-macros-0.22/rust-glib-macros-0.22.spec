# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name glib-macros
%global full_version 0.22.6
%global pkgname glib-macros-0.22

Name:           rust-glib-macros-0.22
Version:        0.22.6
Release:        %autorelease
Summary:        Rust crate "glib-macros"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:506d23499707c7142898429757e8d9a3871d965239a2cb66dfa05052be6d6f19
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.113
Requires:       crate(syn-2/full) >= 2.0.113
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "glib-macros"

%package     -n %{name}+proc-macro-crate
Summary:        Rust bindings for the GLib library, proc macros crate - feature "proc_macro_crate" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro-crate-3/default) >= 3.3.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/proc-macro-crate) = %{version}

%description -n %{name}+proc-macro-crate
This metapackage enables feature "proc_macro_crate" for the Rust glib-macros crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
