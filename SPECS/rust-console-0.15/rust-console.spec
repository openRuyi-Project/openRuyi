# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name console
%global full_version 0.15.11
%global pkgname console-0.15

Name:           rust-console-0.15
Version:        0.15.11
Release:        %autorelease
Summary:        Rust crate "console"
License:        MIT
URL:            https://github.com/console-rs/console
#!RemoteAsset:  sha256:054ccb5b10f9f2cbf51eb355ca1d05c2d279ce1804688d0db74b4733a5aeafd8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(encode-unicode-1.0/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(once-cell-1.0/default) >= 1.21.4
Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-storage-filesystem) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-console) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-ui-input-keyboardandmouse) >= 0.59.0
Provides:       crate(console) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/ansi-parsing)
Provides:       crate(%{pkgname}/windows-console-colors)

%description
Source code for takopackized Rust crate "console"

%package     -n %{name}+default
Summary:        Terminal and console abstraction for Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/ansi-parsing)
Requires:       crate(%{pkgname}/unicode-width)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust console crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-width
Summary:        Terminal and console abstraction for Rust - feature "unicode-width"
Requires:       crate(%{pkgname})
Requires:       crate(unicode-width-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/unicode-width)

%description -n %{name}+unicode-width
This metapackage enables feature "unicode-width" for the Rust console crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
