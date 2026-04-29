# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pathdiff
%global full_version 0.2.3
%global pkgname pathdiff-0.2

Name:           rust-pathdiff-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "pathdiff"
License:        MIT/Apache-2.0
URL:            https://github.com/Manishearth/pathdiff
#!RemoteAsset:  sha256:df94ce210e5bc13cb6651479fa48d14f601d9858cfe0467f43ae157023b938d3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "pathdiff"

%package     -n %{name}+camino
Summary:        Diffing paths to obtain relative paths - feature "camino"
Requires:       crate(%{pkgname})
Requires:       crate(camino-1.0/default) >= 1.0.5
Provides:       crate(%{pkgname}/camino)

%description -n %{name}+camino
This metapackage enables feature "camino" for the Rust pathdiff crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
