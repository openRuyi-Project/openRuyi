# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ordered-channel
%global full_version 1.2.0
%global pkgname ordered-channel-1

Name:           rust-ordered-channel-1
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "ordered-channel"
License:        MIT OR Apache-2.0
URL:            https://gitlab.com/kornelski/ordered-channel
#!RemoteAsset:  sha256:95be4d57809897b5a7539fc15a7dfe0e84141bc3dfaa2e9b1b27caa90acf61ab
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ordered-channel"

%package     -n %{name}+crossbeam-channel
Summary:        Channel that always receives messages in the correct order, even if they were sent out of order - feature "crossbeam-channel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.14
Provides:       crate(%{pkgname}/crossbeam-channel) = %{version}

%description -n %{name}+crossbeam-channel
This metapackage enables feature "crossbeam-channel" for the Rust ordered-channel crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
