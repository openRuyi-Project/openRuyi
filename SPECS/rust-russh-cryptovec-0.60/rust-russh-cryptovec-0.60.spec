# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name russh-cryptovec
%global full_version 0.60.3
%global pkgname russh-cryptovec-0.60

Name:           rust-russh-cryptovec-0.60
Version:        0.60.3
Release:        %autorelease
Summary:        Rust crate "russh-cryptovec"
License:        Apache-2.0
URL:            https://github.com/warp-tech/russh
#!RemoteAsset:  sha256:37cb4d0360bdd8935392a306d8b5edb539cc455b30e8bf13dd213a0cf7879b40
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.11
Requires:       crate(nix-0.31/default) >= 0.31.0
Requires:       crate(nix-0.31/mman) >= 0.31.0
Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-memory) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-systeminformation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "russh-cryptovec"

%package     -n %{name}+ssh-encoding
Summary:        Vector which zeroes its memory on clears and reallocations - feature "ssh-encoding"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ssh-encoding-0.2/bytes) >= 0.2.0
Requires:       crate(ssh-encoding-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/ssh-encoding) = %{version}

%description -n %{name}+ssh-encoding
This metapackage enables feature "ssh-encoding" for the Rust russh-cryptovec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
