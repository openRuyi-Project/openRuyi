# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-refspec
%global full_version 0.31.0
%global pkgname gix-refspec-0.31

Name:           rust-gix-refspec-0.31
Version:        0.31.0
Release:        %autorelease
Summary:        Rust crate "gix-refspec"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:7d29cae1ae31108826e7156a5e60bffacab405f4413f5bc0375e19772cce0055
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-revision-0.35) >= 0.35.0
Requires:       crate(gix-validate-0.10/default) >= 0.10.0
Requires:       crate(smallvec-1/default) >= 1.15.1
Requires:       crate(thiserror-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gix-refspec"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
