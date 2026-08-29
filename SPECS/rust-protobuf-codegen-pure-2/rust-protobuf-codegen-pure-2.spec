# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name protobuf-codegen-pure
%global full_version 2.28.0
%global pkgname protobuf-codegen-pure-2

Name:           rust-protobuf-codegen-pure-2
Version:        2.28.0
Release:        %autorelease
Summary:        Rust crate "protobuf-codegen-pure"
License:        MIT
URL:            https://github.com/stepancheg/rust-protobuf/tree/master/protobuf-codegen-pure/
#!RemoteAsset:  sha256:95a29399fc94bcd3eeaa951c715f7bea69409b2445356b00519740bcd6ddd865
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(protobuf-2/default) >= 2.28.0
Requires:       crate(protobuf-codegen-2/default) >= 2.28.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
WIP
Source code for takopackized Rust crate "protobuf-codegen-pure"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
