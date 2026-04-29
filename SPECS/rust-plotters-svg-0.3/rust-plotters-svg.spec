# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name plotters-svg
%global full_version 0.3.7
%global pkgname plotters-svg-0.3

Name:           rust-plotters-svg-0.3
Version:        0.3.7
Release:        %autorelease
Summary:        Rust crate "plotters-svg"
License:        MIT
URL:            https://plotters-rs.github.io
#!RemoteAsset:  sha256:51bae2ac328883f7acdfea3d66a7c35751187f870bc81f94563733a154d7a670
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(plotters-backend-0.3/default) >= 0.3.7
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/debug)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "plotters-svg"

%package     -n %{name}+image
Summary:        Plotters SVG backend - feature "image" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(image-0.24/bmp) >= 0.24.2
Requires:       crate(image-0.24/jpeg) >= 0.24.2
Requires:       crate(image-0.24/png) >= 0.24.2
Provides:       crate(%{pkgname}/bitmap-encoder)
Provides:       crate(%{pkgname}/image)

%description -n %{name}+image
This metapackage enables feature "image" for the Rust plotters-svg crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bitmap_encoder" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
