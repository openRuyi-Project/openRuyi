# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sd-notify
%global full_version 0.5.0
%global pkgname sd-notify-0.5

Name:           rust-sd-notify-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "sd-notify"
License:        MIT OR Apache-2.0
URL:            https://github.com/lnicola/sd-notify
#!RemoteAsset:  sha256:3e4ef7359e694bfaf1dd27a30f9d760b54c00dfae9f19bd0c05a39bc9128fe76
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sd-notify"

%package     -n %{name}+fdstore
Summary:        Lightweight crate for systemd service state notifications - feature "fdstore"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sendfd-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/fdstore) = %{version}

%description -n %{name}+fdstore
This metapackage enables feature "fdstore" for the Rust sd-notify crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
