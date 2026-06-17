# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nu-ansi-term
%global full_version 0.50.3
%global pkgname nu-ansi-term-0.50

Name:           rust-nu-ansi-term-0.50
Version:        0.50.3
Release:        %autorelease
Summary:        Rust crate "nu-ansi-term"
License:        MIT
URL:            https://github.com/nushell/nu-ansi-term
#!RemoteAsset:  sha256:7957b9740744892f114936ab4a57b3f487491bbeafaf8083688b16841a4240e5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-security) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-storage-filesystem) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-console) >= 0.59.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/gnu-legacy) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "nu-ansi-term"

%package     -n %{name}+serde
Summary:        ANSI terminal colors and styles (bold, underline) - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.152
Requires:       crate(serde-1/derive) >= 1.0.152
Provides:       crate(%{pkgname}/derive-serde-style) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust nu-ansi-term crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive_serde_style" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
