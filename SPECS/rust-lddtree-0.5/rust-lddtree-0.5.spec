# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lddtree
%global full_version 0.5.0
%global pkgname lddtree-0.5

Name:           rust-lddtree-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "lddtree"
License:        MIT
URL:            https://github.com/messense/lddtree-rs
#!RemoteAsset:  sha256:39f71c5bd42adf4ee8e6b24da58c1f00a2817d27f618b169399f5adbf9e74492
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fs-err-3/default) >= 3.0.0
Requires:       crate(glob-0.3/default) >= 0.3.0
Requires:       crate(goblin-0.10/default) >= 0.10.3
Requires:       crate(memmap2-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "lddtree"

%install -p
# Remove prebuilt binary test fixtures from the noarch crate provider.
rm -f tests/*.elf
rm -f tests/*.macho
rm -f tests/*.pe

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
