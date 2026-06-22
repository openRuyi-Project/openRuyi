# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing-error
%global full_version 0.2.1
%global pkgname tracing-error-0.2

Name:           rust-tracing-error-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "tracing-error"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:8b1581020d7a273442f5b45074a6a57d5757ad0a47dac0e9f0bd57b81936f3db
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(tracing-0.1/std) >= 0.1.35
Requires:       crate(tracing-subscriber-0.3/fmt) >= 0.3.0
Requires:       crate(tracing-subscriber-0.3/registry) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/traced-error) = %{version}

%description
Source code for takopackized Rust crate "tracing-error"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
