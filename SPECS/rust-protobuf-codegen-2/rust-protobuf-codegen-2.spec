# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name protobuf-codegen
%global full_version 2.28.0
%global pkgname protobuf-codegen-2

Name:           rust-protobuf-codegen-2
Version:        2.28.0
Release:        %autorelease
Summary:        Rust crate "protobuf-codegen"
License:        MIT
URL:            https://github.com/stepancheg/rust-protobuf/
#!RemoteAsset:  sha256:033460afb75cf755fcfc16dfaed20b86468082a2ea24e05ac35ab4a099a017d6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(protobuf-2/default) >= 2.28.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Includes a library and `protoc-gen-rust` binary.
See `protoc-rust` and `protobuf-codegen-pure` crates.
Source code for takopackized Rust crate "protobuf-codegen"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
