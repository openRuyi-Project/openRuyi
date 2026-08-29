# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libspa
%global full_version 0.9.2
%global pkgname libspa-0.9

Name:           rust-libspa-0.9
Version:        0.9.2
Release:        %autorelease
Summary:        Rust crate "libspa"
License:        MIT
URL:            https://pipewire.org
#!RemoteAsset:  sha256:b6b8cfa2a7656627b4c92c6b9ef929433acd673d5ab3708cda1b18478ac00df4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(cc-1) >= 1.0.66
Requires:       crate(convert-case-0.8/default) >= 0.8.0
Requires:       crate(cookie-factory-0.3/std) >= 0.3.3
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(libspa-sys-0.9/default) >= 0.9.0
Requires:       crate(nix-0.30/default) >= 0.30.1
Requires:       crate(nom-8/default) >= 8.0.0
Requires:       crate(system-deps-7) >= 7.0.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/v0-3-33) = %{version}
Provides:       crate(%{pkgname}/v0-3-40) = %{version}

%description
Source code for takopackized Rust crate "libspa"

%package     -n %{name}+v0-3-65
Summary:        Rust bindings for libspa - feature "v0_3_65" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v0-3-40) = %{version}
Requires:       crate(libspa-sys-0.9/v0-3-65) >= 0.9.0
Provides:       crate(%{pkgname}/v0-3-65) = %{version}
Provides:       crate(%{pkgname}/v0-3-75) = %{version}

%description -n %{name}+v0-3-65
This metapackage enables feature "v0_3_65" for the Rust libspa crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "v0_3_75" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
