# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name link-section
%global full_version 0.18.2
%global pkgname link-section-0.18

Name:           rust-link-section-0.18
Version:        0.18.2
Release:        %autorelease
Summary:        Rust crate "link-section"
License:        Apache-2.0 OR MIT
URL:            https://github.com/mmastrac/linktime
#!RemoteAsset:  sha256:c2b1dd6fe32e55c0fc0ea9493aa57459ca3cf4ff3c857c7d0302290150da6e4f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "link-section"

%package     -n %{name}+default
Summary:        Link-time initialized slices for Rust, with full support for Linux, macOS, Windows, WASM and many more platforms - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proc-macro) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust link-section crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro
Summary:        Link-time initialized slices for Rust, with full support for Linux, macOS, Windows, WASM and many more platforms - feature "proc_macro"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(linktime-proc-macro-0.2/default) >= 0.2.0
Requires:       crate(linktime-proc-macro-0.2/link-section) >= 0.2.0
Provides:       crate(%{pkgname}/proc-macro) = %{version}

%description -n %{name}+proc-macro
This metapackage enables feature "proc_macro" for the Rust link-section crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
